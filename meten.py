print("Vul een geheel nummer in.")
numA = int(input())
print("Vul een ander geheel nummer in.")
numB = int(input())
Max = 0

if(numA > numB):
    Max = numA
    print("a is het grootste getal: "+str(Max))
elif(numA < numB):
    Min = numA
    print("a is het kleinste getal: "+str(Min))