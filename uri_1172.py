vet=[]
for i in range(0,10):
	x=int(input())
	if x<=0:
		x=1
	vet+=[x]	
for c in range(0, 10):
	print(f'X[{c}] = {vet[c]}')