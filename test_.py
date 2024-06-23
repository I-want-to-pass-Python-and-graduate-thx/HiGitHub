def modify_collection(col):
	for i in range(len(col)): 
		col[i-1] = col[i-1] + col[i//2]
	print(col)
print(modify_collection({-1:[-1,0], 0:[0,1], 1:[1,2], 2:[2,3]}))

