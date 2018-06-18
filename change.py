def main():
    pennies = int(input("Number of pennies?: "))
    while pennies < 0:
        pennies = int(input("Only positive values!: "))
    dollars = int(pennies / 100)
    remainder = pennies % 100
    if remainder > 0:
        quarters = int(remainder / 25)
        remainder %= 25
        if remainder > 0:
            dimes = int(remainder / 10)
            remainder %= 10
            if remainder > 0:
                pennies = remainder
            else:
                pennies = 0
        else:
            dimes = 0
            pennies = 0
    else:
        quarters = 0
        dimes = 0
        pennies = 0

    print("{} dollars, {} quarters, {} dimes and {} pennies.".format(
        dollars, quarters, dimes, pennies))


if __name__ == "__main__":
    main()
