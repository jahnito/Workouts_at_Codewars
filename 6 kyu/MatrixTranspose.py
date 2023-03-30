from pprint import pprint

def transpose(matrix):
    return [[matrix[j][i] for j in range(len(matrix))] for i in range(len(matrix[0]))]


if __name__ == '__main__':
    matrixes = ([[1, 2, 3],[4, 5, 6]], [[1]], [[1, 2]])
    for m in matrixes:
        pprint(transpose(m))
