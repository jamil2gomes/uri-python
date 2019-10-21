A = float(input())
B = float(input())
C = float(input())

auxA = max(A, max(B, C))
auxB = auxC = 0

if auxA == A:
    auxB = max(B, C)
    auxC = min(B, C)

if auxA == B:
    auxB = max(A, C)
    auxC = min(A, C)

if auxA == C:
    auxB = max(B, A)
    auxC = min(B, A)

if auxA >= (auxB + auxC):
    print("NAO FORMA TRIANGULO")

elif auxA * auxA > ((auxB * auxB)+(auxC * auxC)):
    print("TRIANGULO OBTUSANGULO")

if auxA * auxA == ((auxB * auxB) + (auxC * auxC)):
    print("TRIANGULO RETANGULO")

if auxA * auxA < ((auxB * auxB) + (auxC * auxC)):
    print("TRIANGULO ACUTANGULO")

if (auxA == auxB) and (auxA == auxC):
    print("TRIANGULO EQUILATERO")

if ((auxB == auxA) and (auxA != auxC)) or ((auxA == auxC) and (auxA != auxB)) or ((auxB == auxC) and (auxB != auxA)):
    print("TRIANGULO ISOSCELES")

