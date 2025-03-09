import threading
from concurrent.futures import ThreadPoolExecutor


def process_files(input_file1, input_file2, output_file, chunk_size=1000000):
    """Reads two large files in chunks, sums corresponding lines, and writes to output."""
    with open(input_file1, 'r') as f1, open(input_file2, 'r') as f2, open(output_file, 'w') as out:
        while True:
            lines1 = [f1.readline().strip() for _ in range(chunk_size)]
            lines2 = [f2.readline().strip() for _ in range(chunk_size)]

            if not lines1[0] or not lines2[0]:  # End of files
                break

            sums = [str(int(a) + int(b)) for a, b in zip(lines1, lines2) if a and b]
            out.write('\n'.join(sums) + '\n')


def multithreaded_processing(input_file1, input_file2, output_file, num_threads=4):
    """Uses multiple threads to process files in chunks."""
    with ThreadPoolExecutor(max_workers=num_threads) as executor:
        executor.submit(process_files, input_file1, input_file2, output_file)


def split_file(input_file, num_parts):
    """Splits a large file into num_parts smaller files."""
    with open(input_file, 'r') as f:
        lines = f.readlines()
    chunk_size = len(lines) // num_parts

    for i in range(num_parts):
        part_file = f"{input_file}.part{i}"
        with open(part_file, 'w') as f:
            f.writelines(lines[i * chunk_size: (i + 1) * chunk_size])


def parallel_processing(num_parts=10):
    """Splits files and processes them in parallel."""
    for i in range(num_parts):
        split_file('hugefile1.txt', num_parts)
        split_file('hugefile2.txt', num_parts)

    threads = []
    for i in range(num_parts):
        t = threading.Thread(target=process_files,
                             args=(f'hugefile1.txt.part{i}', f'hugefile2.txt.part{i}', f'totalfile.txt.part{i}'))
        t.start()
        threads.append(t)

    for t in threads:
        t.join()

    # Merge results
    with open('totalfile.txt', 'w') as outfile:
        for i in range(num_parts):
            with open(f'totalfile.txt.part{i}', 'r') as infile:
                outfile.write(infile.read())


if __name__ == "__main__":
    import time

    start_time = time.time()
    multithreaded_processing('hugefile1.txt', 'hugefile2.txt', 'totalfile.txt', num_threads=4)
    print(f"Multithreaded processing time: {time.time() - start_time} seconds")

    start_time = time.time()
    parallel_processing(10)
    print(f"Parallel processing time: {time.time() - start_time} seconds")
