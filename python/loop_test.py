# loop test
names = ['xiaoming', 'Lilei', 'Hanmeimei']
for name in names:
    print(name)

numbers = range(100 + 1)
sum = 0;
for x in numbers:
    sum += x
print(sum)

numbers = list(range(5))
print(numbers)


n = 10
sum = 0
while n > 0:
    sum += n
    n -= 1
    if n <= 5 :
        break
print('sum =', sum)

n = 10
while n > 0:
    n = n - 1
    if n % 2 == 1:
        continue
    print(n)