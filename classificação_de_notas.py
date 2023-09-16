nota = float(input("Digite o resultado (0 - 100)"))

if nota < 60: 
    print ("F")
elif nota <= 69 and nota >= 60:
    print("D")
elif nota <= 79 and nota >= 70:
    print("C")
elif nota <= 89 and nota >= 80:
    print("B")
elif nota >= 90 and nota <= 100:
    print("A")