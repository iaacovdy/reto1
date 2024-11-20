entrada=input("Escriba la lista de palabras, separadas por coma: ").split(",")
ordenada=[]
unicos=[]
repetidos=[]

#for i in entrada:
    #entrada[i].sort
print(entrada)
print(sorted(entrada))
print(sorted(entrada[1]))
for i in range(0,len(entrada)):
    ordenada.append(sorted(entrada[i]))
print(entrada)
print(ordenada)
for i in ordenada:
   if ordenada.count(i)==1:
      entrada.pop(ordenada.index(i))

#for i in range(0,len(ordenada)-1):
#    if ordenada.count(ordenada[i])==1:
#        entrada.remove(entrada[i].index(i))

print("Repetidos:")
print(ordenada)
print(entrada)