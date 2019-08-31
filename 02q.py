def  fib(num,target):
    for i in range(len(num)):
        if sum(num[:i]) == target:
            return True
        else:
            return False
num = [11,13,200,300,2.5]
target = 500
a = fib(num, target)
# print(sum([11,13,2.5]))
print(a)