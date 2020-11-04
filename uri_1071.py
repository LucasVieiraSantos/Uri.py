x=int(input())
y=int(input())
cnt=0
for i in range((y+1),x):
	if (i%2!=0):
		cnt+=i
print(cnt)