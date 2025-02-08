import time
import random
import multiprocessing
import os
import shutil

# Method to generate random numbers
def generate_random_numbers(filename, count):
    with open(filename, "w") as f:
        f.writelines(f"{random.randint(0, 32767)}\n" for _ in range(count))

if __name__ == "__main__":
    start = time.time()

    num_processes = 4  # Adjust based on CPU cores
    chunk_size = 1_000_000 // num_processes
    temp_files = [f"file2_part{i}.txt" for i in range(num_processes)]

    processes = [multiprocessing.Process(target=generate_random_numbers, args=(temp_files[i], chunk_size)) for i in range(num_processes)]

    for p in processes:
        p.start()
    for p in processes:
        p.join()

    # Use shutil to merge files efficiently
    with open("file2.txt", "wb") as outfile:
        for temp_file in temp_files:
            with open(temp_file, "rb") as infile:
                shutil.copyfileobj(infile, outfile)
            os.remove(temp_file)

    end = time.time()
    print(f"Time taken (optimized merge): {end - start:.2f} seconds")

