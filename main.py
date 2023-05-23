a = int(input("Dígite o valo de a:"))
b =  int(input("Dígite o valor de b:"))
c =  int(input("Dígite o valor de c:"))

if (a + b < c or a + b == c ) or (a + c < b or a + c == b) or ( b + c < a or b + c == a):
     print("Não é um triângulo")
else:
        if a == b and b == c:
             print("Equilátero")
        elif (a == b and b != c) or (b == c and c != a ) or (a == c and c != b):
            print("Isósceles")
        if a != b and b != c and c != a:
             print("Escaleno")


   
#a + b > c`
#a + c > b`
#b + c > a`