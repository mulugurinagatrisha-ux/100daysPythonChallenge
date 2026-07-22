# 1. count passing students ?
marks=[5,45,20,67,35,18]
count=0
for i in marks:
    if i>=35:
        count+=1
print('count:',count)
    
    
    
    
# 2. Shop profit days ?
profit=[5,800,1200,1500,950,2000]
count=0
for i in profit:
    if i>=1000:
        count+=1
print("high profit days:",count) 



# 3. largest multiple of 5 ?
numbers=[5,12,25,18,40,7]
large=0
for i in numbers:
    if i%5==0 and i>large:
        large=i   
if large!=0:
    print("the large divisible by 5 is:",large)    
else:
    print("NO multiples divisible by 5") 
    
    
    
# 4. Average of even numbers ?
numbers=[5,2,5,8,7,10]
sum=0
count=0
for i in numbers:
    if i%2==0:
        sum+=i
        count+=1
if count>0:
    average=sum/count
    print(f'even numbers average:{average:.2f}')
else:
    print('no even values') 
    
    
    
#5. student improvement ?
marks=[5,50,55,52,60,70]
count=0
for i in range(1,len(marks)):
    if marks[i]>marks[i-1]:
        count+=1
print("improvement count:",count) 



#6. Divisors count ?
n=int(input("Enter number:"))
count=0
for i in range(1,n+1):
    if n%i==0:
        count+=1
print('the divisor of given number is:',count)  



# 7. smallest odd number ?
n=[5,8,13,6,5,10]
small=n[0]
for i in n:
    if i%2!=0 and i<small:
        small+=1
if small!=0:
    print("smallest odd number:",small)
else:
    print("No odd values")            
                                
 
 
# 8. count numbers ending with 7 ?
n=[5,27,15,97,120,47]
count=0
for i in n:
    if i%10==7:
        count+=1
print('numbers ending with digit 7 are:',count)        





# 9. multiplication table ?
n=int(input("Enter number:"))
for i in range(1,16):
    print(n,'x',i,'=',n*i)
print()    


#10. sum until negative number ?
n=[5,10,8,2,-1]
sum=0
for i in n:
    if i<0:
        break
    sum+=i
print('sum:',sum)    
                 
            
                      