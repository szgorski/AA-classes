import re
import sys


def read_file(filename):
    try:
        file = open(filename, "r")
    except:
        print('Nie można otworzyć pliku wejściowgo')
        exit(1)

    try:
        first_line = file.readline()
        first_line = re.findall(r"\d+", first_line)
        first_line = [int(x) for x in first_line]

        tree = dict()
        for i in range(first_line[0]):
            line = file.readline()
            line = re.findall(r"\d+", line)
            line = [int(x) for x in line]
            tree.update([(line[0], line[1:])])

        file.close()
    except:
        print('Nie można odczytać pliku wejściowgo')
        exit(1)

    if len(tree) != first_line[0]:
        print('Nieprawidłowa liczba linii w pliku wejściowym')
        exit(1)

    return tree, first_line[1]


def save_file(filename, output):
    try:
        file = open(filename, "w")
        file.write(output)
        file.close()
    except:
        print('Nie można utworzyć pliku wyjściowgo')
        exit(1)


def count(tree, index):
    big_a = 1
    big_b = 1
    for child in tree[index]:
        small_a, small_b = count(tree, child)
        big_a *= small_b
        big_b *= (small_a + small_b)

    return big_a, big_b


if __name__ == '__main__':
    if len(sys.argv) != 3:
        print('Błędna liczba argumentów! Wymagane 2 argumenty:')
        print('    path_in  <string>: ścieżka pliku wejściowego')
        print('    path_out <string>: ścieżka pliku wyjściowego')
        exit(1)

    sys.set_int_max_str_digits(0)
    graph, root = read_file(sys.argv[1])
    a, b = count(graph, root)
    save_file(sys.argv[2], str(a + b))
