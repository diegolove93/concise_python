from math import pi

def area(r1, r2):
    area = pi*(r2 ** 2 - r1 ** 2)
    return area
    
def main():
	outerRadii = input("Enter the outer radii: ")
	innerRadii = input("Enter the inner radii: ")
	print("The annulus area is: {}".format(area(innerRadii, outerRadii)))
	
if __name__ == "__main__":
    main()
