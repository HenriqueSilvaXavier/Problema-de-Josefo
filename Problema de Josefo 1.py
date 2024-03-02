lista=[]
n=int(input("Digite o número total de pessoas: "))
for k in range(1, n+1):
	lista.append(k)
c=0
i=0
n=1
while len(lista)>1:
		if c%2==1:
			del lista[i]
		if c%2!=1:
			i=i+1
		c=c+1
		i2=lista.index(lista[-1])
		if i>i2:
			i=0
		if c%2==0:
			print(lista)
print("O último sobrevivente é a pessoa de número {}".format(lista[0]))