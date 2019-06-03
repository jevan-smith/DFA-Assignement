'''
Group Members: Jevan Smith
Assignment: Project1, problems 1-2
'''


from queue import *
import numpy as np
from numpy.linalg import matrix_power


def findshortest(n, m, transMatrix, Final):
    visited = []
    parent = []
    label = []
    found = False
    q = Queue(maxsize=0)

    for i in range(n):
        visited.append(0)
        parent.append(0)
        label.append(0)

    q.put(0)
    visited[0] = 1
    counting = 0
    while not q.empty():
        current = q.get()
        counting += 1
        for i in range(m):
            next = transMatrix[current][i]
            if next == -9:
                continue
            elif Final[next] == 1:
                label[next] = i
                parent[next] = current
                found = True
                break
            else:
                if visited[next] == 0:
                    parent[next] = current
                    visited[next] = 1
                    label[next] = i
                    q.put(next)
        if found == True:
            break

    if found == False:
        print("False")

    else:
        string = str(label[0])
        current = parent[0]
        while current != 0:
            string += str(label[current])
            current = parent[current]

        print("Output: ", end="")
        print(string[::-1])

def my_transitionmatrix(k, digitsPermitted):
    counter = 0

    DFA2 = [[0 for x in range(10)] for y in range(k)]

    for i in range(k):
        for j in range(10):
            if counter == k:
                counter = 0
            DFA2[i][j] = counter
            counter += 1

    for i in range(k):
        for j in range(10):
            counter = 0
            flag = False

            while counter != len(digitsPermitted):
                if j == digitsPermitted[counter]:
                    flag = True
                counter += 1

            if flag == False:
                DFA2[i][j] = -9

            else:
                flag = False

    DFA2[0][0] = -9

    return DFA2

w, h = 3, 38
DFA = [[0 for x in range(w)] for y in range(h)]

DFA[0][0] = 1
DFA[0][1] = 13
DFA[0][2] = 25
DFA[1][0] = 2
DFA[1][1] = 3
DFA[1][2] = 4
DFA[2][0] = 37
DFA[2][1] = 5
DFA[2][2] = 6
DFA[3][0] = 7
DFA[3][1] = 8
DFA[3][2] = 9
DFA[4][0] = 10
DFA[4][1] = 11
DFA[4][2] = 12
DFA[5][0] = 37
DFA[5][1] = 37
DFA[5][2] = 9
DFA[6][0] = 37
DFA[6][1] = 11
DFA[6][2] = 37
DFA[7][0] = 37
DFA[7][1] = 37
DFA[7][2] = 19
DFA[8][0] = 37
DFA[8][1] = 37
DFA[8][2] = 21
DFA[9][0] = 22
DFA[9][1] = 23
DFA[9][2] = 24
DFA[10][0] = 37
DFA[10][1] = 30
DFA[10][2] = 37
DFA[11][0] = 32
DFA[11][1] = 33
DFA[11][2] = 34
DFA[12][0] = 37
DFA[12][1] = 36
DFA[12][2] = 37
DFA[13][0] = 14
DFA[13][1] = 15
DFA[13][2] = 16
DFA[14][0] = 17
DFA[14][1] = 18
DFA[14][2] = 19
DFA[15][0] = 20
DFA[15][1] = 37
DFA[15][2] = 21
DFA[16][0] = 22
DFA[16][1] = 23
DFA[16][2] = 24
DFA[17][0] = 37
DFA[17][1] = 37
DFA[17][2] = 6
DFA[18][0] = 37
DFA[18][1] = 37
DFA[18][2] = 9
DFA[19][0] = 10
DFA[19][1] = 11
DFA[19][2] = 12
DFA[20][0] = 37
DFA[20][1] = 37
DFA[20][2] = 19
DFA[21][0] = 22
DFA[21][1] = 37
DFA[21][2] = 37
DFA[22][0] = 29
DFA[22][1] = 30
DFA[22][2] = 31
DFA[23][0] = 32
DFA[23][1] = 37
DFA[23][2] = 37
DFA[24][0] = 35
DFA[24][1] = 37
DFA[24][2] = 37
DFA[25][0] = 26
DFA[25][1] = 27
DFA[25][2] = 28
DFA[26][0] = 29
DFA[26][1] = 30
DFA[26][2] = 31
DFA[27][0] = 32
DFA[27][1] = 33
DFA[27][2] = 34
DFA[28][0] = 35
DFA[28][1] = 36
DFA[28][2] = 37
DFA[29][0] = 37
DFA[29][1] = 5
DFA[29][2] = 37
DFA[30][0] = 7
DFA[30][1] = 8
DFA[30][2] = 9
DFA[31][0] = 37
DFA[31][1] = 11
DFA[31][2] = 37
DFA[32][0] = 17
DFA[32][1] = 18
DFA[32][2] = 19
DFA[33][0] = 20
DFA[33][1] = 37
DFA[33][2] = 37
DFA[34][0] = 22
DFA[34][1] = 37
DFA[34][2] = 37
DFA[35][0] = 37
DFA[35][1] = 30
DFA[35][2] = 37
DFA[36][0] = 32
DFA[36][1] = 37
DFA[36][2] = 37
DFA[37][0] = 37
DFA[37][1] = 37
DFA[37][2] = 37


i = 0
j = 0
one = 0
two = 0
three = 0

w, h = 38, 38
A = [[0 for x in range(w)] for y in range(h)]

while True:
    if j == 0:
        one = DFA[i][j]
    elif j == 1:
        two = DFA[i][j]
    elif j == 2:
        three = DFA[i][j]

    A[i][j] = 0

    if j == one or j == two or j == three:
        A[i][j] = 1

    j += 1

    if len(A[1]) == j:
        j = 0
        i += 1
    if len(A[1]) == i:
        A[0][0] = 0
        break


w = 38
u = [0 for x in range(w)]

u[0] = 1

w = 38
v = [1 for x in range(w)]

v[37] = 0


while True:

    try:
        problem = int(input("Which problem do you want todo? ([1-2] or [3 to quit]): "))
    except ValueError:
        print("This is not an integer")
        continue

    if problem == 1:

        try:
            n = int(input("Input (a positive) n: "))
            if n <= 0:
                raise ValueError
        except ValueError:
            print("This is not a correct integer!")
            continue

        a = np.matrix(A, dtype=object)

        b = matrix_power(a, n)

        u = np.matrix(u)

        v = np.matrix(v)

        c = u * b

        d = v.transpose()

        final = c * d

        print("Output: ", end="")
        print(int(final))
        print("")

    elif problem == 2:
        try:
            k = int(input("Enter (a positive) value k: "))
            if k <= 0:
                raise ValueError
        except ValueError:
            print("This is not a correct integer!")
            continue
        try:
            number = int(input("How many Digit's permitted?: "))
            if number <= 0:
                raise ValueError
        except ValueError:
            print("This is not a correct integer, try again!")
            continue

        digits = [0 for x in range(number)]

        for i in range(number):
            try:
                print("Enter (a positive) digit number", i + 1, end="")
                userInput = int(input(": "))
                digits[i] = userInput
                if userInput < 0 or userInput > 9:
                    raise ValueError
            except ValueError:
                print("This is not a correct integer, ignored!")

        transMatrix = my_transitionmatrix(k, digits)

        Final = []

        for i in range(k):
            Final.append(0)
        Final[0] = 1

        findshortest(k, 10, transMatrix, Final)
        print("")

    elif problem == 3:
        break

    else:
        print("1, 2, and 999 are the only options, try again!")

