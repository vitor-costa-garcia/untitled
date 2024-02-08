oddPos = []
evenPos = []
oddGreaterThanFour = 0

while True:
    creditNum = input("Please write down your credit card number: ")
    creditNum = creditNum.replace(' ','')
    try:
        int(creditNum)
        if len(str(creditNum)) == 16:
            break
        else:
            print('Something went wrong.')
    except:
        print("Your credit card number should be only numbers.")

creditFinalNum = creditNum[-1]
creditNum = creditNum[:15]

for i in range(15):
    if i % 2 == 0:
        oddPos.append(int(creditNum[i]))
    else:
        evenPos.append(int(creditNum[i]))
        
for i in oddPos:
    if i > 4:
        oddGreaterThanFour += 1
        
oddValue = sum(oddPos)*2
evenValue = sum(evenPos)
        
finalNum = sum([int(oddValue), int(evenValue), int(oddGreaterThanFour)])
finalDigit = ((((finalNum // 10) + 1)*10) - finalNum)

if int(finalDigit) == int(creditFinalNum):
    print('Valid credit card number.')
else:
    print('Invalid credit card number.')
