





def main():
	largest_seq = 2
	largest_seq_len = 0
	prev_sequences = {} 

	for i in xrange(2, 1000000):
		term = i
		seq = [i]
		while term != 1:
			if term % 2 == 0: 
				term = term / 2
			else:
				term = 3 * term + 1
			if prev_sequences.has_key(term):
				prev_sequences[i] = len(seq) + prev_sequences[term]
				break
			seq.append(term)
		
		if not prev_sequences.has_key(i):	
			prev_sequences[i] = len(seq)

		if prev_sequences[i] > largest_seq_len:
			largest_seq = i
			largest_seq_len = prev_sequences[i]

	print largest_seq
	print largest_seq_len

if __name__=="__main__":
	main()



