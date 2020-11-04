def comp(m):
	r=m[0]
	for i in range(0,len(m)):
		i=int(i)
		x=m[i]
		if x<r:
			r=x
	return r
def val(x,y):
	return (x/y)*1000
s=int(input())
m=[]
for i in range(s):
	x=input().split(' ')
	a,b=float(x[0]),float(x[1])
	m+=[val(a,b)]
n=comp(m)
print(f'{n:.02f}')