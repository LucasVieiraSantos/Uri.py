def med(x,y):
	y/=3.6
	t=x/y
	return t
x=input().split()
a,b,c=x
a=int(a)
b=int(b)
c=int(c)
x=input().split()
a2,b2,c2=x
a2=int(a2)
b2=int(b2)
c2=int(c2)
b=med(b,c)
b2=med(b2,c2)
if b<b2:
	print(a)
else:
	print(a2)