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