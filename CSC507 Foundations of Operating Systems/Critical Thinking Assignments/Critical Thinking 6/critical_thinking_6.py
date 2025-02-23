import multiprocessing as mp
import pandas as pd
import os

INPUT_FILE = "large_input.csv"
OUTPUT_FILE = "processed_output.csv"
NUM_PARTITIONS = 5  # Adjust based on CPU cores
CHUNKSIZE = 2000000  # Adjust based on memory


def process_chunk(chunk, output_file):
    """Processes a chunk and writes to a temporary output file."""
    chunk["processed"] = chunk["value"] * 2  # Example processing
    chunk.to_csv(output_file, index=False)


def process_file_in_parallel(input_file, output_file, num_partitions, chunksize):
    """Splits the file into chunks and processes in parallel."""
    pool = mp.Pool(num_partitions)
    temp_files = []

    for i, chunk in enumerate(pd.read_csv(input_file, chunksize=chunksize)):
        temp_file = f"temp_output_{i}.csv"
        temp_files.append(temp_file)
        pool.apply_async(process_chunk, args=(chunk, temp_file))

    pool.close()
    pool.join()

    # Merge results
    with open(output_file, "w") as fout:
        for i, temp_file in enumerate(temp_files):
            with open(temp_file, "r") as f:
                if i > 0:  # Skip headers for all but the first file
                    next(f)
                fout.write(f.read())
            os.remove(temp_file)


if __name__ == "__main__":
    process_file_in_parallel(INPUT_FILE, OUTPUT_FILE, NUM_PARTITIONS, CHUNKSIZE)