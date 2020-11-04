A=[]
B=[]
C=[]
M=[]
a=input()
b=input()
c=input()
A+=[a]
B+=[b]
C+=[c]
print(A+B+C)
print(B+C+A)
print(C+A+B)
if len(A)>10:
	M+=[A]
if len(B)<11:
	M+=[B]
if len(C)<11:
	M+=[C]
print(M)