from simulation import simulation, random_scheduler
import sys

# Loads the number of processors and the list of
# process runtimes from the file with the given
# filename.
def load_data(filename):
    # TO-DO: implement the function
    arr = []
    with open(filename, 'r') as file:
        for line in file:
            arr.append(int(line.strip()))
    # new_arr = tuple([arr[0], arr[1:]])
    return arr[0], arr[1:]

# A scheduler that assigns the next process with the shortest processing time.
# The next-available processor is assigned.
def shortest_process_first_scheduler(processes, processors):
    # TO-DO: complete the function
    return 0, 0

# A scheduler that assigns processes in the order they are
# presented, to the first available processor
def first_come_first_served_scheduler(processes, processors):
    # TO-DO: complete the function
    return 0, 0

# A program that runs the simulation using three different
# schedulers, and displays the wait time statistics for
# each one.
if __name__ == "__main__":
    num_processors, processes = load_data(sys.argv[1])

    print("SIM 1: random scheduler")
    processes_copy = [x for x in processes]
    final_time, total_wait_time, max_wait_time = simulation(num_processors, processes_copy, random_scheduler)
    print('%20s: %d' % ('Final Time', final_time))
    print('%20s: %d' % ('Total Wait Time', total_wait_time))
    print('%20s: %d' % ('Max Wait time', max_wait_time))
    print('%20s: %0.2f' % ('Average Wait Time', total_wait_time / num_processors))

    print()
    print("SIM 2: first-come-first-served scheduler")
    processes_copy = [x for x in processes]
    final_time, total_wait_time, max_wait_time = simulation(num_processors, processes_copy,
                                                            first_come_first_served_scheduler)
    print('%20s: %d' % ('Final Time', final_time))
    print('%20s: %d' % ('Total Wait Time', total_wait_time))
    print('%20s: %d' % ('Max Wait time', max_wait_time))
    print('%20s: %0.2f' % ('Average Wait Time', total_wait_time / num_processors))

    print()
    print("SIM 3: shortest-process-first scheduler")
    processes_copy = [x for x in processes]
    final_time, total_wait_time, max_wait_time = simulation(num_processors, processes_copy,
                                                            shortest_process_first_scheduler)
    print('%20s: %d' % ('Final Time', final_time))
    print('%20s: %d' % ('Total Wait Time', total_wait_time))
    print('%20s: %d' % ('Max Wait time', max_wait_time))
    print('%20s: %0.2f' % ('Average Wait Time', total_wait_time / num_processors))