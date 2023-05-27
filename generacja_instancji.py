import sys
import random

# random seed
SEED = None


def add_children(n, mean, std_dev):
    children_sets = list()
    for i in range(n):
        children_sets.append(list())

    parent = 1
    last_child = 1
    while last_child < n:
        parent += 1
        if parent > last_child:
            parent = parent % last_child + 1

        number_of_children = round(random.normalvariate(mu=mean, sigma=std_dev))
        number_of_children = min(n - last_child, max(number_of_children, 0))

        for i in range(number_of_children):
            last_child += 1
            children_sets[parent - 1].append(last_child)

        if last_child == n:
            break

    return children_sets


def write_to_file(filename, children_sets, n):
    f = open(filename, "w")
    f.write(str(n) + " 1\n")

    for i in range(len(children_sets)):
        f.write(str(i + 1) + " ")
        for j in range(len(children_sets[i])):
            f.write(str(children_sets[i][j]) + " ")

        f.write("\n")
    f.close()


def main():
    if len(sys.argv) < 2:
        print("Enter number of vertices.")
        return -1
    random.seed(SEED)
    n = int(sys.argv[1])
    if n < 1:
        print("Invalid number")
        return -1

    if len(sys.argv) > 2:
        filename = sys.argv[2]
    else:
        filename = "sample_tree.txt"

    if len(sys.argv) == 5:
        mean = int(sys.argv[3])
        std_dev = int(sys.argv[4])
    else:
        mean = 4
        std_dev = 2

    children_sets = add_children(n, mean, std_dev)
    write_to_file(filename, children_sets, n)


if __name__ == "__main__":
    main()
