class Solution:
    def romanToInt(self, s: str) -> int:
        romanValues = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
        romanNum = list(i for i in s)
        totalValue = 0
        for i in romanNum:
            if i not in romanValues.keys():
                return 'Invalid digit found.'
            
        romanNum.reverse()
        previousIndex = 0
        first = True
        for i in romanNum:
            if first:
                totalValue += romanValues[i]
                first = False
            elif romanValues[romanNum[previousIndex]] > romanValues[i]:
                totalValue -= romanValues[i]
                previousIndex += 1
            elif romanValues[romanNum[previousIndex]] <= romanValues[i]:
                totalValue += romanValues[i]
                previousIndex += 1
                
        return totalValue
