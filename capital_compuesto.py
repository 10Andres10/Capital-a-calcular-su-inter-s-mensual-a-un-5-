print("---------- Capital ----------")
print("------------ a --------------")
print("-------- 5% mensual ---------")

C = int(input("Ingrese el Capital a calcular su interés mensual a un 5%: "))

B = C * 2
m = 0

while C <= B:
    C = C + ( C * 0.05 )
    m = m + 1
else:
    print("El capital " + str(C) + "se duplica en el mes: "+ str(m))