from math import log


def input_stream():
    principal = input("Enter the principal: ")
    interest_rate = input("Enter the interest rate: ")
    number_of_years = input("Enter the number of years: ")
    return (principal, interest_rate, number_of_years)


def balance_formula(data):
    P = data[0]
    i = data[1]
    t = data[2]
    balance = P * (1 + i)**t
    return balance


def years_to_double_interest(data):
    i = data[1]
    r = data[2]
    years = log(2) / log(1 + i)
    return years


def main():
    data = input_stream()
    print("The new balance is {} ".format(balance_formula(data)))
    print("The number of years to double principal is {} ".format(
        years_to_double_interest(data)))


if __name__ == '__main__':
    main()
