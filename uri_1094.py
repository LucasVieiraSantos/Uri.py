num_c=0
num_s=0
num_r=0
tot=0
x=int(input())
for i in range(0,x):
	quant=input().split(' ')
	a,b=quant
	a=int(a)
	if 1<=a<=15:
		if b=='c' or b=='C':
			num_c=a+num_c
		elif b=='R' or b=='r':
			num_r=a+num_r
		elif b=='S' or b=='s':
			num_s=a+num_s
	tot=tot+a
per_c=(num_c*100)/tot
per_r=(num_r*100)/tot
per_s=(num_s*100)/tot
print("Total: %d cobaias" %tot)
print("Total de coelhos: %d" %num_c)
print("Total de ratos: %d" %num_r)
print("Total de sapos: %d" %num_s)
print("Percentual de coelhos: {:.2f} %".format((num_c/float(tot))*100))
print("Percentual de ratos: {:.2f} %".format((num_r/float(tot))*100))
print("Percentual de sapos: {:.2f} %".format((num_s/float(tot))*100))