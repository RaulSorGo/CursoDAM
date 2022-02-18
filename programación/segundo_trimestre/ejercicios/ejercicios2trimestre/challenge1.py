def capital_indexes(palabra):
 lista = []
 for i, s in enumerate (palabra):
   if s.isupper():
     lista.append(i) 
   return lista
print(capital_indexes("HeLlO"))