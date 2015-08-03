

import operator

def findSpecialTriple():
    for hypotenuse in range(334, 999):
        for leg1 in range(1, 666 - hypotenuse):
            leg2 = 1000 - leg1 - hypotenuse
            if leg1**2 + leg2**2 == hypotenuse**2:
                print leg1, leg2, hypotenuse
                print leg1 * leg2 * hypotenuse
                return

def main():
    findSpecialTriple()

if __name__=="__main__":
	main()



