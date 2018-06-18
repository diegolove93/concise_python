from math import sqrt


def basel(n):
    # Compute the sum of 1 / k ** 2 for k=1 to n.
    total = 0

    for k in range(1, n + 1):
        total += 1 / (k ** 2)
    return total


def main():
    print("%-13s%-13s%-13s" % ("n", "sum", "sqrt(6*sum)"))
    for n in range(1, 100001, 1000):
        print("%-13f%-13f%-13f" % (n, basel(n), sqrt(6 * basel(n))))
    return


if __name__ == "__main__":
    main()
