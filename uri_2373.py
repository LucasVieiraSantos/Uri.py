def copos(x,y):
	if x>y:
		return y
	elif x==y:
		return 0
	else:
		return 0

q1=0
b=int(input())
for i in range(b):
	x=input().split()
	l,c=x
	c=int(c)
	l=int(l)
	q=copos(l,c)
	q1+=q
print(q1)