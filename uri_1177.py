N=[]
t=int(input())
c=0
for i in range(0,1000):
	if c==t:
		c=0
	N+=[c]
	print(f'N[{i}] = {N[c]}')
	c+=1