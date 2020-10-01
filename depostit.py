p=10000
rate=0.06
T=5
t=0
for x in range (5):
	i=p*rate
	p=p+i
	t=i+t
	print("[+] principal for year ",x)
	print(p) 
print("[+] final ammount is",p)
print("[+] final total intrest" ,t)
