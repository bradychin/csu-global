import time
import multiprocessing


# Method 1: Read entire file into memory
def method_1():
    start_time = time.time()

    with open("file1.txt", "r") as f:
        numbers = [int(line.strip()) * 2 for line in f]

    with open("newfile1.txt", "w") as f:
        f.writelines(f"{num}\n" for num in numbers)

    print(f"Method 1 (Read entire file): {time.time() - start_time:.2f} seconds")


# Method 2: Process line by line
def method_2():
    start_time = time.time()

    with open("file1.txt", "r") as infile, open("newfile1.txt", "w") as outfile:
        for line in infile:
            outfile.write(f"{int(line.strip()) * 2}\n")

    print(f"Method 2 (Process line by line): {time.time() - start_time:.2f} seconds")


# Method 3: Parallel processing by splitting the file
def process_chunk(chunk, output_file):
    with open(chunk, "r") as infile, open(output_file, "w") as outfile:
        for line in infile:
            outfile.write(f"{int(line.strip()) * 2}\n")


def method_3():
    start_time = time.time()

    # Split file1.txt into two parts
    with open("file1.txt", "r") as f:
        lines = f.readlines()

    mid = len(lines) // 2
    part1, part2 = "file1_part1.txt", "file1_part2.txt"

    with open(part1, "w") as f:
        f.writelines(lines[:mid])
    with open(part2, "w") as f:
        f.writelines(lines[mid:])

    # Process each half in parallel
    p1 = multiprocessing.Process(target=process_chunk, args=(part1, "newfile1_part1.txt"))
    p2 = multiprocessing.Process(target=process_chunk, args=(part2, "newfile1_part2.txt"))

    p1.start()
    p2.start()
    p1.join()
    p2.join()

    # Merge results
    with open("newfile1.txt", "w") as outfile:
        for part in ["newfile1_part1.txt", "newfile1_part2.txt"]:
            with open(part, "r") as infile:
                outfile.write(infile.read())

    print(f"Method 3 (Parallel processing): {time.time() - start_time:.2f} seconds")


if __name__ == "__main__":
    method_1()
    method_2()
    method_3()