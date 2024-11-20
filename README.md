# UNIVERSIDAD NACIONAL DE COLOMBIA
# PROGRAMACIÓN ORIENTADA A OBJETOS

# Santiago Daza Yepes

## Reto 1: Resumen de conceptos clave en Python

### Crear una función que realice operaciones básicas (suma, resta, multiplicación, división) entre dos números, según la elección del usuario, la forma de entrada de la función será los dos operandos y el caracter usado para la operación. *entrada:* `(1,2,"+")`, *salida* `(3)`.

+ Separamos el input en: número A, número B y operador
+ Utilizamos match case para determinar la operación en cada caso
+ Imprimimos en pantalla la lista y el resultado

```python
entrada=input("Escriba dos números y el operador, separados por coma: ").split(",")
def operar(a,b,c):
    match c:
        case "+":
            return a+b
        case "-":
            return a-b
        case "*":
            return a*b
        case "/":
            if b==0:
                return "Indeterminado"
            else:
                return a/b

print(entrada)
print(operar(int(entrada[0]),int(entrada[1]),entrada[2]))
```
*Resultado*
```
Escriba dos números y el operador, separados por coma: 15,3,/
['15', '3', '/']
5.0
```
### Realice una función que permita validar si una palabra es un palíndromo. **Condición:** No se vale hacer slicing para invertir la palabra y verificar que sea igual a la original.

+ Convertimos la palabra a minúsculas usando el método lower
+ Un ciclo while comparará el primer carácter con el último
  + Si son iguales para todos los casos determinará que es una palabra palíndroma "True"
  + De lo contrario indicará que no es palíndromo, simbolizado como "False"
+ Muestra el resultado en pantalla

```python
entrada=input("Escriba la palabra a verificar: ").lower()
i: int=0
pal: bool=True
largo: int=len(entrada)-1
while (i<len(entrada)):
    if entrada[i]==entrada[largo-i]:
        i+=1
        continue
    else:
        pal=False
        break

print(entrada+" es palíndromo? "+str(pal))
```
*Resultado*
```
Escriba la palabra a verificar: reconocer
reconocer es palíndromo? True
```

### Escribir una función que reciba una lista de números y devuelva solo aquellos que son primos. La función debe recibir una lista de enteros y retornar solo aquellos que sean primos.

+ Recibimos del usuario una lista de números separados por comas
+ Convertimos el input en una lista de números enteros
+ Definimos una función "primo" de la siguiente manera:
  + Si el número es = 1, no es primo
  + Si el número tiene algún divisor (sin residuo) mayor que uno y menor que el mismo, se determina como no primo
  + Si no cumple las anteriores, es primo
+ Agregamos los primos encontrados a una nueva lista
+ Se muestra la lista de primos al usuario

```python
entrada=[int(i) for i in input("Escriba la lista de números, separados por coma: ").split(",")]
primos = []

def primo(n):
    if n==1:
        return False
    for i in range(2,n):
        if n%i == 0:
            return False
    return True

for i in entrada:
    if primo(i):
        primos.append(i)

print("los números primos son: ")
print(primos)
```
*Resultado*
```
Escriba la lista de números, separados por coma: 1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20
los números primos son: 
[2, 3, 5, 7, 11, 13, 17, 19]
```

### Escribir una función que reciba una lista de números enteros y retorne la mayor suma entre dos elementos consecutivos.

+ Tomamos una lista de n números
+ Sumamos los pares de números consecutivos, manteniendo registro del record más alto
+ Se determina como solución al valor de suma más alto encontrado al terminar de iterar la lista

```python
entrada=[int(i) for i in input("Escriba la lista de números, separados por coma: ").split(",")]
print(entrada)
mayor=0
for i in range(0,len(entrada)-1):
    sumar=entrada[i]+entrada[i+1]
    if (sumar>mayor):
        mayor=sumar
    
print ("La suma mayor es: ")
print (mayor)
```
*Resultado*
```
Escriba la lista de números, separados por coma: 47,15,18,75,35,48,77,55
[47, 15, 18, 75, 35, 48, 77, 55]
La suma mayor es:
132
```

### Escribir una función que reciba una lista de string y retorne unicamente aquellos elementos que tengan los mismos caracteres. e.g. entrada: `["amor", "roma", "perro"]`, salida `["amor", "roma"]`

+ Recibimos las palabras del usuario como Strings separadas por comas
+ Creamos una lista vacía "ordenada"
+ Ordenamos los carácteres de cada String de manera alfabética
+ Buscamos la cantidad de repeticiones de cada elemento ordenado
  + Si es exáctamente = 1, se remueve de la lista inicial
  + De lo contrario se conserva
+ Presemtamos las palabras repetidas depuradas

```python
entrada=input("Escriba la lista de palabras, separadas por coma: ").split(",")
ordenada=[]

for i in range(0,len(entrada)):
    ordenada.append(sorted(entrada[i]))
for i in ordenada:
   if ordenada.count(i)==1:
      entrada.pop(ordenada.index(i))

print("Repetidos:")
print(entrada)
```
*Resultado*
```
Escriba la lista de palabras, separadas por coma: perro,amor,roma,omar,ramo
Repetidos:
['amor', 'roma', 'omar', 'ramo']
```
