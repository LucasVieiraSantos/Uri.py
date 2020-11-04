A=[]
for i in range(0,100):
	x=float(input())
	A+=[x]
for c in range(0,100):
	if A[c]<=10:
		print(f'A[{c}] = {A[c]}')