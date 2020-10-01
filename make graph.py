import matplotlib.pyplot as plt

n1=int(input("Enter a starting point "))
n2=int(input("Enter a end point "))
h=6.63*10**(-34)
m=9.1*10**(-31)
l=1*10**(-6)
E1=[]
for n in range(n1,n2):
    print('For n ',n)
    E=n**2*h**2/(8*m*l**2)
    E1.append(E)
    print('value of E',E)

n=[i for i in range(n1,n2)]
plt.plot(n,E1)

plt.title('Energy verses Number')
plt.ylabel('Energy')
plt.xlabel('Number')
plt.show()
