print("Vul een geheel nummer in.")
numA = int(input())
print("Vul een ander geheel nummer in.")
numB = int(input())
Max = 0
Min = 0

if(numA > numB):
    Max = numA
    Min = numB
    print("a is het grootste getal: "+str(Max))
elif(numA < numB):
    Min = numA
    Max = numB
    print("a is het kleinste getal: "+str(Min))
else:
    Min = numA
    Max = Min
    print("a en b zijn even groot")

print("Het minimum is: "+str(Min))
print("Het maximum is: "+str(Max))