import threading
import time
import random

# Create a lock to prevent race conditions
write_lock = threading.Lock()

def write_random_numbers(file_name, amount):
    """Generate random numbers and append them to a file safely."""
    with write_lock:  # Ensures only one thread writes at a time
        with open(file_name, "a") as file:
            for _ in range(amount):
                file.write(f"{random.randint(0, 32767)}\n")

def main():
    start_time = time.time()

    num_threads = 4
    numbers_per_thread = 1_000_000 // num_threads
    threads = []

    # Create multiple threads to generate numbers
    for _ in range(num_threads):
        thread = threading.Thread(target=write_random_numbers, args=("file2.txt", numbers_per_thread))
        threads.append(thread)
        thread.start()

    # Wait for all threads to finish
    for thread in threads:
        thread.join()

    end_time = time.time()
    print(f"Execution Time (Multithreading): {end_time - start_time:.2f} seconds")


if __name__ == "__main__":
    main()