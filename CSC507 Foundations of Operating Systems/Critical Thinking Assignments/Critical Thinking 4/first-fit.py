memory_blocks = [500, 200, 400, 300, 700]
process_sizes = [213, 341, 900, 586, 152]

for i, process in enumerate(process_sizes):
    assigned = False
    for j, block in enumerate(memory_blocks):
        if process <= block:
            memory_blocks[j] -= process
            print(f'Process {process} assigned to block {j+1}. New size of block {j+1} is {memory_blocks[j]}')
            assigned = True
            break
    if not assigned:
        print(f'Process {process} can not be assigned. ')

print(f'\nFinal block sizes: {memory_blocks}')