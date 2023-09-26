if __name__ == "__main__":
	for _ in range(int(input())):
		x, y = [int(val) for val in input().split()]
		if x == y:
			print((x*x) - y + 1)
		elif y > x:
			if y&1:
				print((y*y) - (x) + 1)
			else:
				print(((y-1)*(y-1)) + (x))
		else:
			if not (x&1):
				print((x*x) - (y) + 1)
			else:
				print(((x-1)*(x-1)) + (y))