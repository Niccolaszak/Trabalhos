class cozinha:
	def __init__(self,fogao,geladeira,panela):
		self.fogao = fogao
		self.geladeira = geladeira
		self.panela = panela

	def cozinhar(self, comida):
		print(f'Fazendo um(a) {comida} na panela {self.panela}')

#class quarto(cozinha)
#	def __init__(self):
#		super().__init__()
#	def cozinhar(self, comida, prato)
#		print(f'{super().cozinhar(comida)} prato {prato}')



cozi = cozinha('eletrolux', 'brastemp', 'ferro')
coz = cozinha('fogao', 'geladeira', 'panela')
#cozinha.cozinhar('Pé de Moleque')

cozinhas = []
cozinhas.append(coz)
cozinhas.append(cozi)

print(f"Os fogoes são: {[coz.fogao for coz in cozinhas]}")