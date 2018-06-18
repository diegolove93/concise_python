
def main():
    for integer in range(1, 101):
        print("%-7i%-13s%-13s" % (integer, bin(integer), hex(integer)))
    return


if __name__ == "__main__":
    main()
