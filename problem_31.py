
from itertools import combinations



def main():
	coins = [1, 2, 5, 10, 20, 50, 100, 200]
	coinArray = []
	for target in range(0, 202):
		for col in range(1, len(coins)):
			coinArray.append([1] + [0] * (len(coins) - 1))
			if coins[col] < target: 
				coinArray[target][col] += coinArray[target][col - 1]
				coinArray[target][col] += coinArray[target - coins[col]][col]
			else:
				coinArray[target][col] += coinArray[target][col - 1]
		print target - 1, coinArray[target]	
if __name__=="__main__":
	main()