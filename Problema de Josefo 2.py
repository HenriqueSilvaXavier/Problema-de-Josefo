n=int(input("Digite o número total de pessoas: "))
P2=[]
k=1
while n>=k:
	P2.append(k)
	k=k*2
s=(n-P2[-1])*2+1
print("O último sobrevivente é a pessoa de número {}.".format(s))