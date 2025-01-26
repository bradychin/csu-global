import random

with open("file2.txt", "w") as file:
    for _ in range(1000):
        file.write(f'{random.randint(0, 32767)}\n')