"""
3366
sprawdz, czy sudoku
dziala, ale SPOJ nie akceptuje
"""


D = int(input())

for d in range(D):

    sudoku = [ [None] * 9 for i in range(9) ]

    for i in range(9):
        linia = input()
        linia = linia.split(" ")
        for j in range(9):
            sudoku[i][j] = int(linia[j])

    def czy_to_sudoku(sudoku):
        for i in range(9):
            for x in range(1, 10):
                czy_jest = False
                for j in range(9):
                    if sudoku[i][j] == x: czy_jest = True
                if not czy_jest: return False

        for j in range(9):
            for x in range(1, 10):
                czy_jest = False
                for i in range(9):
                    if sudoku[i][j] == x:
                        czy_jest = True
                if not czy_jest:
                    return False


        for k1 in range(3):
            for k2 in range(3):
                for x in range(1, 10):
                    czy_jest = False
                    for i in range(3):
                        for j in range(3):
                            if sudoku[k1 * 3 + i][k2 * 3 + j] == x: czy_jest = True
                    if not czy_jest: return False

        return True

    czy_sudoku = czy_to_sudoku(sudoku)

    if czy_sudoku: print("TAK")
    else: print("NIE")

    if d != D-1: f = input()
