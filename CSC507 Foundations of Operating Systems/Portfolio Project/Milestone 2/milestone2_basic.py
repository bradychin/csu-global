import time
import random

start_time = time.time()

# Write 1,000,000 random numbers to file2.txt
with open("file2.txt", "w") as f:
    for _ in range(1_000_000):
        f.write(f"{random.randint(0, 32767)}\n")

end_time = time.time()
print(f"Time taken: {end_time - start_time:.2f} seconds")