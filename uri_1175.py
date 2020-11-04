N=[]
in_N=[]
for i in range(0,20):
	x=int(input())
	N+=[x]
for c in range(19,-1,-1):
	in_N+=[N[c]]
for c1 in range(0,20):
	print(f'N[{c1}] = {in_N[c1]}')
