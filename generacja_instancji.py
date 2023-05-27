import sys
import random

SEED = None


def add_children(number_of_vertices):
    children_sets = list()
    for i in range(number_of_vertices):
        children_sets.append(list())

    parent = 1
    last_child = 1
    while last_child < number_of_vertices:
        parent = parent % last_child + 1
        pow_base = 2 - 2 * parent / number_of_vertices
        number_of_children = round(2 * pow_base * pow_base * random.random())
        for i in range(number_of_children):
            last_child += 1
            children_sets[parent - 1].append(last_child)

    return children_sets


def write_to_file(filename, sets, number_of_vertices):
    try:
        f = open(filename, "w")
        f.write(str(number_of_vertices) + " 1\n")

        for i in range(len(sets)):
            f.write(str(i + 1) + " ")
            for j in range(len(sets[i])):
                f.write(str(sets[i][j]) + " ")
            f.write("\n")

        f.close()
    except:
        print('Nie można utworzyć pliku wyjściowgo')
        input('\nNaciśnij Enter, aby zakończyć program...')
        exit(1)


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print('Błędna liczba argumentów! Wymagane 2 argumenty uruchamiania:')
        print('    count       <int>: liczba wierzchołków w drzewie')
        print('    path_out <string>: ścieżka pliku wyjściowego')
        input('\nNaciśnij Enter, aby zakończyć program...')
        exit(1)

    random.seed(SEED)
    n = int(sys.argv[1])
    if n < 1:
        print('Błędna liczba wierzchołków')
        input('\nNaciśnij Enter, aby zakończyć program...')
        exit(1)

    children = add_children(n)
    path_out = str(sys.argv[2])
    write_to_file(path_out, children, n)

    print('Wygenerowane drzewo znajduje się pliku ' + path_out)
    input('\nNaciśnij Enter, aby zakończyć program...')
