#1. cosecutive pass count ?
n=[8,40,55,20,36,70,90,15,45]
largest=0
count=0
for i in n:
    if i>=35:
        count+=1
        if count>largest:
            largest=count
    else:
        count=0    
print(largest)            

        
#2 largest prime entered ?
num=[6,12,17,21,29,18,7]
largest=0
for i in num:
    if i%1==0 and i%i==0:
        if i>largest:
           largest=i
print(f'largest prime:{largest}')     


   
#3. sum of even digits ?
Evendigits=[4,8,2,7,3,1,6]
sum=0
for i in Evendigits:
    if i%2==0:
        sum+=i
print(f'sum of even digits:{sum}')  


#4.factory quality check ?
QualityOfitems=[6,45,60,72,38,80,49]
defective=0
good=0
for i in QualityOfitems:
    if i<=50:
        defective+=1
    else:
        good+=1
print(f'defective items:{defective}')
print(f'good items:{good}')            
 
#5.maximum sales increase ?
sales=[5,100,130,110,180,200]
max=0
i=2
while i<len(sales):
    increase=sales[i]-sales[i - 1]
    if increase>max:
        max=increase
    i+=1    
print(max)        

#6. number with most digits ?
n=[5,23,9867,105,123456,89]
largest=n[0]
for i in n:
    if len(str(i))>len(str(largest)):
        largest=i
print(f'number with most digits:{largest}')  


#7. count numbers divisible by 4 and 6 ?
n=[6,12,24,18,36,40,48]
count=0
for i in n:
    if i%4==0 and i%6==0:
        count+=1
print(f'count numbers divisible by both 4 and 6: {count}') 


#8. Longest odd streak ?
streak=[8,3,5,8,7,9,11,4,13]
longest=0
count=0
for i in streak:
    if i%2!=0:
        count+=1
        if count>longest:
            longest=count
    else:
        count=0        
print(f'longest odd streak:{longest}')  



#9. smallest digit sum ?
digit = [4, 123, 81, 44, 70]

smallest_sum = 999
number = 0

for i in digit:
    temp = i
    total = 0

    while temp > 0:
        total += temp % 10
        temp = temp // 10

    if total < smallest_sum:
        smallest_sum = total
        number = i

print("Number with smallest digit sum:", number)

#10. running balance ?
balance=int(input("Enter balance:"))
n=int(input("Enter no of transactions:"))
for i in range(n):
    transaction = int(input("Enter transaction (+ for deposit, - for withdrawal): "))
    balance+=transaction                    
print(f'balance:{balance}')
print(f'final balance:{balance}')    