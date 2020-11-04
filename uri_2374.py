def reg(x,y):
	c=0
	if x<y:
		while x<y:
			x+=1
			c-=1
	elif x>y:
		while x>y:
			y+=1
			c+=1
	elif x==y:
		return 0
	return c
N=int(input())
M=int(input())
print(reg(N,M))