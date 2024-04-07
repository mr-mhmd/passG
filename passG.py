import string
import random

lenpass = int(input("enter len password :"))
uppersFlag = input("do you want to add uppers? 'yes' or 'no' ")
lowersFlag = input("do you want to add lowers? 'yes' or 'no' ")
numbersFlag = input("do you want to add numbers? 'yes' or 'no' ")
symbolsFlag = input("do you want to add symbols? 'yes' or 'no' ")
uppers = string.ascii_uppercase
lowers = string.ascii_lowercase
numbers = string.digits
symbols = string.punctuation
while True :
    if uppersFlag == 'yes' and lowersFlag == 'yes' and numbersFlag == 'yes' and symbolsFlag == 'yes' :               
        passwordGenerator = ""
        for char in range(lenpass//2):
            passwordGenerator += random.choice(uppers)
        for char in range(lenpass//2):
            passwordGenerator += random.choice(lowers)
        for char in range(lenpass//2):
            passwordGenerator += random.choice(numbers)
        for char in range(lenpass//2):
            passwordGenerator += random.choice(symbols)
    elif uppersFlag == 'no' and lowersFlag == 'yes' and numbersFlag == 'yes' and symbolsFlag == 'yes' :               
        passwordGenerator = ""
        for char in range(lenpass//2):
            passwordGenerator += random.choice(lowers)
        for char in range(lenpass//2):
            passwordGenerator += random.choice(numbers)
        for char in range(lenpass//2):
            passwordGenerator += random.choice(symbols)
    elif uppersFlag == 'no' and lowersFlag == 'no' and numbersFlag == 'yes' and symbolsFlag == 'yes' :               
        passwordGenerator = ""
        for char in range(lenpass//2):
            passwordGenerator += random.choice(numbers)
        for char in range(lenpass//2):
            passwordGenerator += random.choice(symbols)    
    elif uppersFlag == 'no' and lowersFlag == 'no' and numbersFlag == 'no' and symbolsFlag == 'yes' :               
        passwordGenerator = ""
        for char in range(lenpass//2):
            passwordGenerator += random.choice(symbols)            
    elif uppersFlag == 'yes' and lowersFlag == 'yes' and numbersFlag == 'yes' and symbolsFlag == 'no' :               
        passwordGenerator = ""
        for char in range(lenpass//2):
            passwordGenerator += random.choice(uppers)
        for char in range(lenpass//2):
            passwordGenerator += random.choice(lowers)
        for char in range(lenpass//2):
            passwordGenerator += random.choice(numbers)
    elif uppersFlag == 'yes' and lowersFlag == 'yes' and numbersFlag == 'no' and symbolsFlag == 'no' :               
        passwordGenerator = ""
        for char in range(lenpass//2):
            passwordGenerator += random.choice(uppers)
        for char in range(lenpass//2):
            passwordGenerator += random.choice(lowers)
    elif uppersFlag == 'yes' and lowersFlag == 'no' and numbersFlag == 'no' and symbolsFlag == 'no' :               
        passwordGenerator = ""
        for char in range(lenpass//2):
            passwordGenerator += random.choice(uppers)    
    elif uppersFlag == 'no' and lowersFlag == 'no' and numbersFlag == 'no' and symbolsFlag == 'no' :               
        print("error")
#4-,,,,
    break    

print(passwordGenerator)




#2

if uppersFlag == 'yes' :
    uppersBe = True
if lowersFlag == 'yes' :
    lowersBe = True
if numbersFlag == 'yes' :
    numbersBe = True
if symbolsFlag == 'yes' :
    symbolsBe = True

passwordGenerator = ""
for char in range(lenpass):
    if uppersBe == True :
        passwordGenerator += random.choice(uppers)
    elif lowersBe == True :    
        passwordGenerator += random.choice(lowers)
    elif numbersBe == True :
        passwordGenerator += random.choice(numbers)
    elif symbolsBe == True :
        passwordGenerator += random.choice(symbols)
print(passwordGenerator)