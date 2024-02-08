class Solution:
    def addTwoNumbers(self, l1, l2):
        myNum1 = ''
        myNum2 = ''
        for i in range(0,len(l1)):
            myNum1 = str(l1[i])+myNum1
        for i in range(0,len(l2)):
            myNum2 = str(l2[i])+myNum2
            
        myResult = int(myNum1) + int(myNum2)
        return [str(myResult)[-i] for i in range(1,1+len(str(myResult)))]
