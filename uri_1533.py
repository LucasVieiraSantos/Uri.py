def ind(x,z):
	c=1
	for i in z:
		if i==x:
			return c
		c+=1
		
s=int(input())
l=[]
while s!=0:
	l.clear()
	x=input().split(' ')
	for c in x:
		l+=[int(c)]
	print(ind(s,l))
	s=int(input())
