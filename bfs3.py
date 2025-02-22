from turtle import *
import random
import copy
import time
from collections import deque


class Cube:
    # U = ['W', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'W'] # front
    # L = ['O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O'] # upper
    # R = ['R', 'R', 'R', 'R', 'R', 'R', 'R', 'R', 'R'] # down
    # F = ['G', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G'] # left
    # B = ['B', 'B', 'B', 'B', 'B', 'B', 'B', 'B', 'B'] # right
    # D = ['Y', 'Y', 'Y', 'Y', 'Y', 'Y', 'Y', 'Y', 'Y'] # back

    def __init__(self):
        self.U = ['W', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'W'] # front
        self.L = ['O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O'] # upper
        self.R = ['R', 'R', 'R', 'R', 'R', 'R', 'R', 'R', 'R'] # down
        self.F = ['G', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G'] # left
        self.B = ['B', 'B', 'B', 'B', 'B', 'B', 'B', 'B', 'B'] # right
        self.D = ['Y', 'Y', 'Y', 'Y', 'Y', 'Y', 'Y', 'Y', 'Y'] # back


    # Front Clockwise
    def FC(self):
        bl, bc, br = self.U[6], self.U[7], self.U[8]
        self.U[6], self.U[7], self.U[8] = self.L[8], self.L[5], self.L[2]
        self.L[2], self.L[5], self.L[8] = self.D[0], self.D[1], self.D[2]
        self.D[0], self.D[1], self.D[2] = self.R[6], self.R[3], self.R[0]
        self.R[0], self.R[3], self.R[6] = bl, bc, br

        rotate_face_cw(self.F)

    # Front AntiClockwise
    def FA(self):
        bl, bc, br = self.U[6], self.U[7], self.U[8]
        self.U[6], self.U[7], self.U[8] = self.R[0], self.R[3], self.R[6]
        self.R[0], self.R[3], self.R[6] = self.D[2], self.D[1], self.D[0]
        self.D[0], self.D[1], self.D[2] = self.L[2], self.L[5], self.L[8]
        self.L[2], self.L[5], self.L[8] = br, bc, bl

        rotate_face_acw(self.F)

    # Left Clockwise
    def LC(self):
        bl, bc, br = self.U[0], self.U[3], self.U[6]
        self.U[0], self.U[3], self.U[6] = self.B[8], self.B[5], self.B[2]
        self.B[2], self.B[5], self.B[8] = self.D[6], self.D[3], self.D[0]
        self.D[6], self.D[3], self.D[0] = self.F[6], self.F[3], self.F[0]
        self.F[0], self.F[3], self.F[6] = bl, bc, br


        rotate_face_cw(self.L)

     # Left AntiClockwise
    def LA(self):
        bl, bc, br = self.U[0], self.U[3], self.U[6]
        self.U[0], self.U[3], self.U[6] = self.F[0], self.F[3], self.F[6]
        self.F[0], self.F[3], self.F[6] = self.D[0], self.D[3], self.D[6]
        self.D[0], self.D[3], self.D[6] = self.B[8], self.B[5], self.B[2]

        self.B[2], self.B[5], self.B[8] = br, bc, bl

        rotate_face_acw(self.L)

    # Right Clockwise
    def RC(self):
        bl, bc, br = self.U[2], self.U[5], self.U[8]
        self.U[2], self.U[5], self.U[8] = self.F[2], self.F[5], self.F[8]
        self.F[2], self.F[5], self.F[8] = self.D[2], self.D[5], self.D[8]
        self.D[2], self.D[5], self.D[8]  = self.B[6], self.B[3], self.B[0]
        self.B[6], self.B[3], self.B[0] = bl, bc, br

        rotate_face_cw(self.R)

    # Right Anti Clockwise
    def RA(self):
        bl, bc, br = self.U[2], self.U[5], self.U[8]
        self.U[2], self.U[5], self.U[8] = self.B[6], self.B[3], self.B[0]
        self.B[6], self.B[3], self.B[0] = self.D[2], self.D[5], self.D[8]
        self.D[2], self.D[5], self.D[8] = self.F[2], self.F[5], self.F[8]
        self.F[2], self.F[5], self.F[8] = bl, bc, br

        rotate_face_acw(self.R)

    # Upper Clockwise
    def UC(self):
        bl, bc, br = self.B[0], self.B[1], self.B[2]
        self.B[0], self.B[1], self.B[2] = self.L[0], self.L[1], self.L[2]
        self.L[0], self.L[1], self.L[2] = self.F[0], self.F[1], self.F[2]
        self.F[0], self.F[1], self.F[2] = self.R[0], self.R[1], self.R[2]
        self.R[0], self.R[1], self.R[2] = bl, bc, br

        rotate_face_cw(self.U)

    # Upper anti Clockwise
    def UA(self):
        bl, bc, br = self.B[0], self.B[1], self.B[2]
        self.B[0], self.B[1], self.B[2] = self.R[0], self.R[1], self.R[2]
        self.R[0], self.R[1], self.R[2] = self.F[0], self.F[1], self.F[2]
        self.F[0], self.F[1], self.F[2] = self.L[0], self.L[1], self.L[2]
        self.L[0], self.L[1], self.L[2] = bl, bc, br

        rotate_face_acw(self.U)

    # Down Clockwise
    def DC(self):
        bl, bc, br = self.F[6], self.F[7], self.F[8]
        self.F[6], self.F[7], self.F[8] = self.L[6], self.L[7], self.L[8]
        self.L[6], self.L[7], self.L[8] = self.B[6], self.B[7], self.B[8]
        self.B[6], self.B[7], self.B[8] = self.R[6], self.R[7], self.R[8]
        self.R[6], self.R[7], self.R[8] = bl, bc, br

        rotate_face_cw(self.D)

    # Down anti Clockwise
    def DA(self):
        bl, bc, br = self.F[6], self.F[7], self.F[8]
        self.F[6], self.F[7], self.F[8] = self.R[6], self.R[7], self.R[8]
        self.R[6], self.R[7], self.R[8] = self.B[6], self.B[7], self.B[8]
        self.B[6], self.B[7], self.B[8] = self.L[6], self.L[7], self.L[8]
        self.L[6], self.L[7], self.L[8] = bl, bc, br

        rotate_face_acw(self.D)

    # Bottom Clockwise
    def BC(self):
        bl, bc, br = self.U[0], self.U[1], self.U[2]
        self.U[0], self.U[1], self.U[2]= self.R[2], self.R[5], self.R[8]
        self.R[2], self.R[5], self.R[8] = self.D[8], self.D[7], self.D[6]
        self.D[8], self.D[7], self.D[6] = self.L[6], self.L[3], self.L[0]
        self.L[6], self.L[3], self.L[0] = bl, bc, br

        rotate_face_cw(self.B)

    # Bottom anti Clockwise
    def BA(self):
        bl, bc, br = self.U[0], self.U[1], self.U[2]
        self.U[0], self.U[1], self.U[2]= self.L[6], self.L[3], self.L[0]
        self.L[6], self.L[3], self.L[0] = self.D[8], self.D[7], self.D[6]
        self.D[8], self.D[7], self.D[6] = self.R[2], self.R[5], self.R[8]
        self.R[2], self.R[5], self.R[8] = bl, bc, br

        rotate_face_acw(self.B)

    valid_moves = [BA,BC,DA,DC,UA,UC,RA,RC,LA,LC,FA,FC]
    test_valid_moves = [BA,DA,UA,RA,LA,FA]

    def print(self):
        tracer(0,0)
        x=0
        y=0
        print_face(x,y, self.L)
        x = x + 75
        y = 0
        print_face(x,y, self.F)
        x = x + 75
        y = 0
        print_face(x,y, self.R)
        x = x + 75
        y = 0
        print_face(x,y, self.B)
        x = 75
        y = -75
        print_face(x,y, self.D)
        x = 75
        y = 75
        print_face(x,y, self.U)
        update()

    def test_scramble(self):
        self.FA()
        self.RC()
        self.LC()
        self.BC()

    def scramble(self):
        for i in range(random.randint(20,30)):
            fun = random.choice(self.valid_moves)
            fun(self)

    def is_solved(self, initial):
        if self.B == initial.B and self.F == initial.F and self.L == initial.L and self.R == initial.R and self.U == initial.U:
            return True
        return False

def print_face(x, y, face):
    for i in range(9):
        draw_square(face[i], x, y)
        x= x + 25
        if i == 2 or i == 5 or i == 8:
            penup()
            y = y - 25
            x = x - 75

def rotate_face_cw(F):
    tmp = F[0]
    F[0], F[6], F[8], = F[6], F[8], F[2]
    F[2] = tmp
    F[1], F[3], F[7], F[5] = F[3], F[7], F[5], F[1]

def rotate_face_acw(F):
    F[0], F[2], F[8], F[6] = F[2], F[8], F[6], F[0]
    F[1], F[5], F[7], F[3] = F[5], F[7], F[3], F[1]

def draw_square(col, x, y):
    col = color_map(col)
    setpos(x, y)
    pendown()
    fillcolor(col)
    pencolor('black')
    begin_fill()
    for i in range(5):
        forward(25)
        right(90) if i!=4 else 0
    end_fill()

def color_map(col):
    switcher = {
        'W' : 'white',
        'O' : 'orange',
        'R' : 'red' ,
        'G': 'green',
        'B' : 'blue',
        'Y': 'yellow'
    }

    return switcher.get(col, 'brown')



def cube_to_tuple(cube):
    """Convert cube state to a tuple for hashing."""
    return (tuple(cube.F), tuple(cube.L), tuple(cube.R), tuple(cube.B), tuple(cube.U), tuple(cube.D))

def solve_cube(cube: Cube):

    initial = cube
    cube = Cube()
    frontier = deque([(cube, [])])
    reached = set()

    while frontier:
        current, moves = frontier.popleft()

        if current.is_solved(initial= initial):
            return current

        state = cube_to_tuple(current)
        if state in reached:
            continue
        reached.add(state)

        for move in current.valid_moves:
            newcube = copy.deepcopy(current)
            move(newcube)
            newstate = cube_to_tuple(newcube)
            if newstate not in reached:
                frontier.append((newcube, moves + [move.__name__]))



sum =0
count = 0
tlist = ['o']
def test(cube, level):
    global sum, count
    if level <= 0:
        start_time = time.time()
        solve_cube(cube)
        run_time = time.time() - start_time
        if run_time < 0.0005:
            tlist.pop()
            return
        print(f" Solved In ", run_time)
        sum += run_time
        count += 1
        print("Average = ", sum/count)
        tlist.pop()
        return

    for fun in reversed(cube.test_valid_moves):
        if tlist[-1] != fun.__name__:
            tlist.append(fun.__name__)
            newcube = copy.deepcopy(cube)
            fun(newcube)
            test(newcube, level-1)
            if count > 100:
                return




mycube = Cube()
mycube.test_scramble()
mycube.print()
time.sleep(1)
start_time = time.time()
solved = solve_cube(mycube)
print("Solved In ", time.time() - start_time)
solved.print()
time.sleep(1)


