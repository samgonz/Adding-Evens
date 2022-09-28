sumOfEvenNumbers = 0

startingNumber = int(input('What would you like to choose for a starting number?\n'))
endingNumber = int(input('What would you like to choose for an ending number?\n'))
for i in range(startingNumber, endingNumber+1):
    if i % 2 == 0:
        sumOfEvenNumbers += i
        
print(f'The sum of all even numbers from {startingNumber} to {endingNumber} is {sumOfEvenNumbers}.')
