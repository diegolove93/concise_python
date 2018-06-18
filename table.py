from math import log

def main():
    print("%-13s%-13s%-13s%-13s%-13s" % ("n","log(n)","n*log(n)","n**2","2**n"))
    for n in range(10,210,10):
        print ("%-13i%-13f%-13f%-13f%-13f" % (n,log(n),n*log(n),n**2,2**n))
    return
    
if __name__ == "__main__":
    main()

    

