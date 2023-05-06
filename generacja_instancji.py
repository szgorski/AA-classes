import sys
import numpy as np
import random
SEED = None


def add_children(n):
    children_sets = [None] * n
    for i in range(n):
        children_sets[i] = []
    bfs_queue = [1]
    current_vertex = 1
    while len(bfs_queue) > 0:
        parent_vertex = bfs_queue[0]
        number_of_children = random.randint(0, n-current_vertex)
        if (number_of_children == 0 and n != current_vertex and len(bfs_queue) == 1):
            number_of_children = 1
        for i in range(number_of_children):
            current_vertex += 1
            children_sets[parent_vertex-1].append(current_vertex)
            bfs_queue.append(current_vertex)
        bfs_queue.pop(0)

    return children_sets


def write_to_file(filename, children_sets, n):
    f = open(filename, "w")
    f.write(str(n) + " 1\n")

    for i in range(len(children_sets)):
        f.write(str(i+1) + " ")
        for j in range(len(children_sets[i])):
            f.write(str(children_sets[i][j]) + " ")

        f.write("\n")
    f.close()


def main():
    if (len(sys.argv) < 2):
        print("Enter number of vertices.")
        return -1
    random.seed(SEED)
    n = int(sys.argv[1])
    if (n < 1):
        print("Invalid number")
        return -1

    children_sets = add_children(n)

    if (len(sys.argv) > 2):
        filename = sys.argv[2]
    else:
        filename = "sample_tree.txt"

    write_to_file(filename, children_sets, n)


if __name__ == "__main__":
    main()
