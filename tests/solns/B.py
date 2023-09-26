if __name__ == "__main__":
	for i in range(1, int(input())+1):
		ns = i*i
		n2 = (ns*(ns-1))//2
		if i > 2:
			n2 = n2- 4*(i-1)*(i-2)
		print(n2)