def pyramid(n):
    total = 0
    for m in range(1,n+1):
        total += m ** 2
    return total

def main():
    print("%-13s%-13s%-13s" % ("n","pyramid","growth-rate"))
    past_pyramid = 0
    for n in range(1, 41):
        if n != 1:
            growth_rate = (pyramid(n) - past_pyramid)/past_pyramid
            print("%-13f%-13f%-13f" % (n,pyramid(n),growth_rate))
        else:
            print("%-13f%-13f%-13f" % (n,pyramid(n),0))
        past_pyramid = pyramid(n)
    return

if __name__ == "__main__":
    main()
