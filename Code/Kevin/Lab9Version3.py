footTM = input("Enter a number, and I will convert it to meters:\n ")
numFootTM = int(footTM)
unitChoice = input("Is your number in ft, mi, meters, or kilos?\n")

if unitChoice == 'ft':
    print(f"{footTM} {unitChoice} is converted to {numFootTM * 0.3048}")

elif unitChoice == 'mi':
    print(f"{footTM} {unitChoice} is converted to {numFootTM * 1609.34}")

elif unitChoice == 'meters':
        print(f"{footTM} {unitChoice} is converted to {numFootTM * 1}")

elif unitChoice == 'kilos':
    print(f"{footTM} {unitChoice} is converted to {numFootTM * 1000}")

elif unitChoice == 'yd':
    print(f"{footTM} {unitChoice} is converted to {numFootTM * 0.9144}")

elif unitChoice == 'inch':
    print(f"{footTM} {unitChoice} is converted to {numFootTM * 0.0254}")
#else print("please enter a valid unit: \n")
