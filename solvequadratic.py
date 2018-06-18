from cmath import sqrt as sqrt2
from math import sqrt


def solvequadratic(a, b, c):
    if a != 0:
        d = b**2 - 4 * a * c
        if d == 0:
            root = - b / (2 * a)
            print("there is only 1 root: {}".format(root))
        elif d > 0:
            sqrt_d = [sqrt(d), -sqrt(d)]
            roots = [ (x - b) / (2 * a)  for x in sqrt_d]
            print("there are 2 real roots: {}, {}".format(roots[0],roots[1]))
        elif d < 0:
            sqrt_d = [sqrt2(d), -sqrt2(d)]
            roots = [ (x - b) / (2 * a) for x in sqrt_d]
            print("there are 2 complex roots: {}, {}".format(roots[0], roots[1]))
    else:
        print("Not a quadratic polynomial!")


def main():
    a = float(input("""input "a" coefficient: """))
    b = float(input("""input "b" coefficient: """))
    c = float(input("""input "c" coefficient: """))

    solvequadratic(a, b, c)


if __name__ == "__main__":
    main()