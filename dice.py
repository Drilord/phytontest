import random 

def dice(dados):
	print('Te toca')
	#print('dados: ',dados)
	tiros=0
	while (tiros < dados):
	#print('tiros: ',tiros)
		print(random.randint(1,6))
		tiros= tiros+1
	
a= ''	
while (a != 'n'):
	a= input('tirar y/n?')	
	if a=='y':
		cuantos=int(input('cuantos dados?'))
		dice(cuantos)
