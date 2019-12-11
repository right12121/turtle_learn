from turtle import *
import random

def my_tree(n, l):
    n_1 = n
    def my_tree_1(n, l, n_1):
        pd()
        pensize(n / 3)
        forward(l)
        n_r = random.randint(1, n_1)
        if n > n_r * 5:
            left(15)
            my_tree_1(n - 1, l * 0.7, n_1)
            right(20)
            my_tree_1(n - 1, l * 0.7, n_1)
            left(5)
        elif n > 0:
            right(25)
            my_tree_1(n - 1, l * 0.7, n_1)
            left(30)
            my_tree_1(n - 1, l * 0.7, n_1)
            right(5)
        else:
            pass
        pu()
        backward(l)
    my_tree_1(n, l, n_1)

tracer(0,0)
bgcolor('peachpuff')
pencolor('darkgreen')
pensize(4)
left(45)
pu()
backward(200)
my_tree(10, 150)
done()