# 1. check whether a number is postivie or negative
num=int(input("Enter number:"))
if num>=0:
    print("positive")
else:
    print("negative")    


# 2. number is even or odd.
num=int(input("Enter number:"))
if num%2==0:
    print("even")
elif num%2!=0:
    print("odd")


# 3. largest of two numbrs ?
num1=int(input("Enter number:"))
num2=int(input("Enter number:"))
if num1>num2:
    print('num1 larger')
elif num2>num1:
    print('num2 larger')




# 4. smallest of two numbers?
num1=int(input("Enter number:"))
num2=int(input("Enter number:"))
if num1<num2:
    print('num1 is smaller')
elif num2<num1:
    print('num2 is smaller')   


# 5. person eligible to vote or not?
age=int(input("Enter age:"))
if age>20:
    print('person eligible for vote')
else:
    print('person not eligible for vote')


#6. number is divisible by 5?
num=int(input("Enter number:"))
if num%5==0:
    print('number is divisible by 5')
else:
    print('number is not divisible by 5') 



#7. number is divisible by 3 and 5?
num=int(input("Enter number:"))
if num%3==0 and num%5==0:
    print('number is divisible by both 3 and 5')
else:
    print('number is not divisible by both 3 and 5')       




# 8. charecter is vowel or consonent ?
ch=input("Enter charecter:")
if ch=='a' or ch=='e' or ch=='i' or ch=='o' or ch=='u' or ch=='A' or ch=='E' or ch=='I' or ch=='O' or ch=='U':
    print('char is vowel')
else:
    print('char is consonant')    


# 9. year is leap or not?

year=int(input("Enter year:"))
if (year%400==0) or (year%4==0 and year%100!=0):
    print(year,'is a leap year')
else:
    print(year,'is a ordinary year')    


#10 a student passed (marks>=35).
marks=int(input("Enter marks:"))
if marks>=35:
    print('pass') 
else:
    print('fail')        


# 11. find the largest of three numbers?
n1=int(input("Enter number:"))
n2=int(input("Enter number:"))
n3=int(input("Enter numebr:"))
if n1>n2:
    print('n1 is larger')
elif n2>n3:
    print('n2 is larger')
elif n3>n1:
    print('n3 is larger')        



# 12. find smallest fo three numbers .
n1=int(input("Enter number:"))
n2=int(input("Enter number:"))
n3=int(input("Enter numebr:"))
if n1<n2:
    print('n1 is smallest')
elif n2<n3:
    print('n2 is smallest')
elif n3<n1:
    print('n3 is smallest')        



#13. if num is multiple of 7?
num=int(input("Enter number:"))
if num%7==0:
    print(num,'is a multiple of 7')
else:
    print(num, 'is not a multiple of 7')    



# 14. calculate electricity bill based on units?
# units=int(input("enter units:"))
# if units<=100:
#     bill=units*5
# elif units<=200:
#     bill=units*8
# else:
#     bill=units*10
# print('electricity bill=',bill)     



# 15. income tax based on salary ?
# salary=int(input("enter amount:"))
# if salary<=25000:
#     tax=salary*0.02
# elif salary<=35000:
#     tax=salary*0.04
# elif salary<=45000:
#     tax=salary*0.08
# else:
#     tax=salary*0.10
# print('total salary:',salary)
# print('tax:',tax)                
    
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          

# 16. display grade based on marks?
# marks=int(input("Enter marks:"))
# if marks>=90:
#     print('grade A+')
# elif marks>=80:
#     print('grade A')
# elif marks>=70:
#     print('grade B')
# elif marks>=60:
#     print('grade C')
# elif marks>=50:
#     print('grade D')
# elif marks>=35:
#     print('just pass you have to improve')
# else:
#     print('fail')                       


# 17. check if char is uppercase or lower case ?
# ch=input("Enter alphabet:")
# if ch>='A'and ch<='Z':
#     print('char is upper')
# elif ch>='a' and ch<='z':
#     print('char is lower')  
# else:
#     print('invalid input')          


# 18. check if a number is a 3 digit number ?
# num=int(input("Enter number:"))
# if num>=100 and num<=999:
#     print(num,'num is a 3-digit number')
# elif num>=-100 and num<=-999:
#     print(num,'num is a 3-digit number')
# else:
#     print(num, 'num is not a 3-digit number')          



# 19. check wether a triangle is valid .
# a=float(input("Enter first side:"))
# b=float(input("Enter second side:"))
# c=float(input("enter third side:"))
# if (a+b>c) and (b+c>a) and (c+a>b):
#     print('valid triangle')
# else:
#     print('invalid triangle')


#20 find the type of triangle ?
# a=float(input("Enter first side:"))
# b=float(input("Enter second side:"))
# c=float(input("Enter third side:"))
# if (a+b>c) and (a+c>b) and (b+c>a):
#    if a==b==c:
#        print('equilateral triangle')
#    elif (a==b) or (b==c) or (c==a):
#        print('isosceles triangle')
#    else:
#        print('scalen triangle') 
# else:
#     print('invalid triangle')    
       


# 21. atm withdrawel validation (balance,pin,amount)?
# balance=int(input("Enter balance:"))
# pin=12345
# password=int(input("Enter your pin:"))
# if password==pin:
#     amount=int(input("Enter withdrawel amount:"))
#     if amount<=balance:
#        balance=balance-amount
#        print("withdrawel successful")
#        print(' Remaining balance:',balance)
#     else:
#        print('insufficient balance')  
# else:
#     print('Incorrect pin')       


# 22. login system using username and password ?
# username=input("Enter your username:")
# password=input("Enter your password:")
# if username=="trisha@720" and password=="whatsapp123":  
#     print('your login successful')
# else:
#     print('invalid username and password')



# 23. movie ticket booking eligibility based on age ?
# age=int(input("Enetr your age:"))
# if age<5:
#     print('entry is free')
# elif age>=5 and age<=18:
#     print('child ticket')
# elif age>=18 and age<60:
#     print('adult ticket')
# else:
#     print('senior citizen ticket')    



# 24. calculate discount based on purchase amount ?
# amount=int(input("Enter your purchase amount:"))
# if amount>=10000:
#     discount=amount*0.20
# elif amount>=5000:
#     discount=amount*0.10
# elif amount>=2000:
#     discount=amount*0.05
# else:
#     discount=0
# final_amount=amount-discount
# print("purchase amount:",amount)
# print("discount:",discount)
# print("final amount:",final_amount)        
            



# 25. mobile recharge offer based on recharge amount ?
# recharge=int(input("Enter your mobile rechagre amount:"))
# if recharge>=999:
#     print("offer: unlimited calls + 2gb/day + OTT subscription")
# elif recharge>=499:
#     print("offer: unlimited calls + 2gb/day")
# elif recharge>=299:
#     print("offer: unlimited calls + 1.5gb/day")
# elif recharge>=199:
#     print("offer: unlimited calls + 1gb/day")
# else:
#     print("offer: talktime only")


# 26. check whether a person is eligible for loan or not ?
# age=int(input("Enter your age:"))
# income=float(input("Enter your monthly income:"))
# if age>=21 and age <=60:
#     if income>=25000:
#        print('congratulations you are eligible for loan')
#     else:
#         print('sorry! income is too low for a loan')
# else:
#     print('sorry! age is not eligible for a loan')   


         
# 27. bmi calculator with health categeory .
# height=float(input("Enetr your height:"))
# weight=float(input("Enter your weight:"))
# bmi=weight/(height*height)
# print('bmi:',round(bmi,2))
# if bmi<18.5:
#     print("health categeroy: underweight")
# elif bmi<25:
#     print("health categeory: normal weight")
# elif bmi<30:
#     print("health categeory: overweight")
# else:
#     print("health categeory: obese")            




# 28. bonus based on employee experience ?
# experience=int(input("Enter your experience:"))
# salary=int(input("Enter your monthly salary:"))
# if experience>5:
#     bonus=salary*0.5
    
# elif experience>10:
#     bonus=salary*0.10
    
# elif experience>15:
#     bonus=salary*0.15
# else:
#     bonus=0
# total_salary=salary+bonus
# print("salary:",salary) 
# print("bonus:",bonus)
# print("total salary:",total_salary)       
   



# 29. admissions eligibilty based on marks and entrance exam score.
# marks=int(input("Enter your marks:"))
# examscore=int(input("Enter your score:"))
# if marks>=35 and examscore>=70:
#     print('you are eligible for admission')
# elif marks>=35 and examscore>=45:
#     print('your are eligible , but you have to pay half fee')
# elif marks>=35 and examscore>=30:
#     print('you are eligible , but you have to pay one third of fee') 
# else:
#     print('you are not eligible and you have to pay full fee')               
     


# 30. restaurant bill with gst and discount.
# bill=int(input("Enter your restaurent bill:"))
# if bill>=1000:
#     discount=bill*0.10
#     gst=bill*2/100
# elif  bill>=2000:
#     discount=bill*0.20
#     gst=bill*3/100
# elif bill>=3000:
#     discount=bill*0.25
#     gst=bill*3.5/100
# else:
#     discount=0
#     gst=bill*5/100
# bill_after_discount=bill-discount  
# total_bill=bill_after_discount+gst
# print("bill amount:",bill)
# print('discount:',discount)
# print("bill after discount:",bill_after_discount)
# print('gst:',gst)
# print('total bill:',total_bill)   




# second largest among three numbers?
# n1=int(input("Enter your number:"))
# n2=int(input("Enter you number:"))
# n3=int(input("Enter your number:"))
# if (n1>n2 and n1<n3) or (n1<n2 and n1>n3):
#     print('second largest:',n1)
# elif (n2>n1 and n2<n3) or (n2<n1 and n2>n3):
#     print('second largest:',n2)
# else:
#     print('second largest:',n3)                    



                           