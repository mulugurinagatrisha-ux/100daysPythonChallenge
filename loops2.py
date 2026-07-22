# 1. Highest profit month ?
# def:find the maximum value and its position while reading inputs.
# task: a shop owner records the profit for N months.
# Print the highest profit and its month number?
profit=[5,12000,15000,9800,17500,16000]
highest=profit[0]
month=1
for i in range(len(profit)):
    if profit[i]>highest:
        highest=profit[i]
        month=i+1
print('highest profit:',highest)
print('month number:',month)


#2. perfect square counter ?
# def: a perfect square in the square of an integer
# read N numbers and count how many are perfect squares.
n = [5,16,20,25,18,49]

count = 0

for i in n:

    j = 1
    while j * j <= i:
        if j * j == i:
            count = count + 1
            break
        j = j + 1

print(f'perfect squares of a number:{count}')

#3. sum of multiples of 7 
#  def: multiples of 7 are numbers divisible by 7
# task:read a and b sum of all multiples of 7 between them
a = int(input("enter number:"))
b = int(input("Enter number:"))
total = 0
for i in range(a, b + 1):
    if i % 7 == 0:
        total = total + i
print(f'Sum of all multiples of 7:{total}')   



#4. longest positive streak ?
num=[8,5,7,-2,4,9,10,12,-5]
longest=0
count=0
for i in num:
    if i>0:
        count+=1
        if count>longest:
            longest=count
    else:
        count=0        
print(f'longest positive streak is:{longest}')  


#5. count numbers with exactly three divisors ?
num=[5,4,9,8,16,25]
count=0
for i in num:
    divisor=0
    for j in range(1,i+1):
        if i%j==0:
            divisor+=1
    if divisor==3:
        count+=1
print(f'the number with exact 3 divisors is:{count}')        
                  

#6. largest difference ?
num=[5,10,25,18,40,32]
largest = 0
for i in range(len(num) - 1):
    diff = num[i + 1] - num[i]
    if diff < 0:
        diff = -diff
    if diff > largest:
        largest = diff
print(f'largest difference for a number is:{largest}')  


#7 Salary bonus ?
salary=[5,25000,40000,18000,32000,29000]
count=0
for i in salary:
    if i<30000:
        count+=1
print(f'salary count lessthan 30000 is:{count}')  



#8 largest digit sum?
dig=[4,123,98,555,71]
sum=0
largest=0
for i in dig:
    temp = i
    dig_sum = 0
    while temp > 0:
        dig_sum = dig_sum + (temp % 10)
        temp = temp // 10

    if dig_sum > largest:
        largest = dig_sum
        d = i
print(f'the largest digit sum is:{d}')


#9 Average until Zero ?
num=[8,12,20,0]
count=0
sum=0
for i in num:
    if i==0:
        break
    sum+=i
    count+=1
average=sum/count
print(f'average until zero is:{average}')    



#10. count numbers greater than average?
num=[5,10,20,30,40,50]
count=0
sum=0
for i in num:
    count+=1
    sum+=i
average=sum/count 
greater=0
for i in num:
    if i>average:
        greater+=1    
print(f'average of numbers:{average}')
print(f'greater than of numbers:{greater}')