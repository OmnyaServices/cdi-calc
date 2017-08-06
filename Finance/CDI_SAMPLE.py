import math
from decimal import Decimal,ROUND_DOWN

percent_CDI=100
cetiptralala= 10.14
tax_d_cdi = [cetiptralala,cetiptralala,cetiptralala,9.14]

def get_investido(value,num_dias):
	TDKI=0
	tdkis=[]
	factors = []
	values=[]
	for tax in tax_d_cdi:
		tdkis.append(get_TDKI(tax))
	
	for td in tdkis:
		factors.append(get_factor(td))
	values = list()
	for i in factors:
		value = round(value*i,2)
		values.append(value)
		
	print values
	return values
	#TDKI = getTDKI()
	#factor = get_factor()
	#return round(value*factor,2)
	

def get_factor(TDKI):
	return round(Decimal((1+ TDKI*percent_CDI*.01)),16)
	
def get_TDKI(taxa):
	ftax_cdi= Decimal(taxa*.01)+1
	f252= Decimal(1.0/252.0)
	return round(Decimal(pow(ftax_cdi,f252)-1),8)

	
print get_investido(10000,tax_d_cdi)

