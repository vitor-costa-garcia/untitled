mylist = [x if x%3==0 else 0 for x in range(0, 1000)]
mylist2 = [x if x%5==0 else 0 for x in range(0,1000)]
numlist = mylist + mylist2
sum(set(numlist))
