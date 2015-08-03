
import itertools

def main():
	L = [int("%d%d%d" % (x,y,x)) for x in range(1,10) for y in range(10)]
	[sum([n*(10**i) for i,n in enumerate(([x]+list(ys)+[z]+list(ys)[::-1]+[x]) if k%2
                                else ([x]+list(ys)+list(ys)[::-1]+[x]))])
            for x in range(1,10)
            for ys in itertools.permutations(range(10), k/2-1)
            for z in (range(10) if k%2 else (None,))]

if __name__=="__main__":
	main()