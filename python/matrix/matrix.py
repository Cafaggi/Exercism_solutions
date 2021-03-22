class Matrix:
    def __init__(self, matrix_string):
        self._matrix = [list(map(int, row.split())) for row in matrix_string.split('\n')]
        self._transposed_matrix = [list(column) for column in zip(*self._matrix)]

    def row(self, index):
        return self._matrix[index-1]

    def column(self, index):
        return self._transposed_matrix[index-1]
