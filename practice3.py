#****************
# operators based problems
#****************


#1. read food bill and gst% calculate gst and final bill ?
# bill=float(input("Enter food bill:"))
# gst_per=float(input("Enter gast percentage:"))
# gst=(bill*gst_per)/100
# final_bill=gst+bill
# print(f'gst amount:{gst}')
# print(f'bill:{bill}')
# print(f'final bill:{final_bill}')



#2. read mobile price and discount.calculate discount and final price ?
# mobile_price=float(input("Enter mobile_price:"))
# discount=float(input("Enter discount:"))
# dis=(mobile_price*discount)/100
# final_bill=mobile_price-dis
# print(f'discount amount:{dis}')
# print(f'final amount:{final_bill}')


#3. read liters and price/per. find total cost ?
# liters=float(input("Enter no of liters:"))
# price_per_liter=float(input("Enter cost of each liter:"))
# f_cost=liters*price_per_liter
# print(f'total cost:{f_cost}')



#4. read units and price/unit find bill ?
# units=float(input("Enter number of units:"))
# price_per_unit=float(input("Enter price per unit:"))
# total_bill=units*price_per_unit
# print(f'total bill:{total_bill}')



#5.read runs and balls. compute (runs*100)/balls ?
# runs=int(input("Enter number of runs:"))
# balls=int(input("Enter number of balls:"))
# strike_rate=(runs*100)/balls
# print(f'final result:{strike_rate}')




#6.read marks.check marks>=35 ?
# marks=int(input("Enter marks:"))
# if marks>=35:
#     print('pass')
# else:
#     print('fail')    




#7.read balance and withdrawel check balance >=withdrawel ?
# balance=float(input("Enter balance:"))
# withdraw=int(input("Enter withdrawel amount:"))
# if balance>=withdraw:
#     print('withdraw succesfull')
# else:
#     print('you dont have sufficient balance') 
# remaining=balance-withdraw   
# print(f'current balance:{remaining}')




#8.read age. check age>=18 ?
# age=int(input("Enter age:"))
# if age>=18:
#     print('eligible')
# else:
#     print('not eligible')




#9.read two passwords. check equality ?
# p1=input("enter password1:") 
# p2=input("Enter password2:")
# if p1==p2:
#     print('both are equal')
# else:
#     print('both are not equal') 




#10.read order amount.check >=500 ?
# amount=int(input("Order amount:"))
# if amount>=500:
#     print('thank you!') 
# else:
#     print('add more items to reach 500') 




#11.read percentage and income eligible if >=85 and income<300000 ?
# percentage=int(input("Enter percentage:"))
# income=int(input("Enter income amount:"))
# if percentage>=85 and income<300000:
#     print('eligible')
# else:
#     print('not eligible')   




#12.read age and fitness.eligible if age>=18 and fit ?
# age=int(input("Enetr age:"))
# fitness=input("Enter fit/unfit:")
# if age>=18 and fitness=="fit":
#     print('eligible')
# else:
#     print('not eligible') 



#13.read saturday and sunday flags. weekend if either true.
# saturday=input("it is saturday:(True/False):")
# sunday=input("it is sunday:(True/False):")
# if saturday=="True" and sunday=="True":
#     print('weekend')
# else:
#     print('not weekend')




#14. read degree status and age. eligible if degree and age>=21.
# degree=input("enter degree status(pass/fail:)") 
# age=int(input("Enter your age:"))
# if degree=="pass" and age>=21:
#     print('eligible')
# else:
#     print('not eligible') 



#15. read current and max level check full ?
# current=int(input("Enter current level:"))
# max=int(input("Enter maximum level:")) 
# full=current+max
# print(f'full level:{full}') 




#16. read hours . cost=40*hours ?
# hours=int(input("Enter hours:")) 
# cost=40*hours
# print(f'total hours cost:{cost}') 


#17. read salary.bonus if<50000 ?
# salary=float(input("enter salary amount:"))
# bonus=int(input("Enter bonus amount:"))
# if salary<50000:
#     bonus+=salary
#     print(f'total salary with bonus:{bonus}')
# else: 
#     print(f'no bonus added')      



#18.read loan and months.emi=loan/months ?
# loan=int(input("Enter loan amount:"))
# months=int(input("enter no of months:"))
# emi=loan/months
# print(f'total emi:{emi}')



#19.read purchase.cashback 5% if>2000.
# purchase = int(input("Enter purchase amount: "))
# if purchase > 2000:
#     cashback = purchase * 0.05
#     total = purchase - cashback
#     print("Cashback:", cashback)
#     print("Total bill is:", total)
# else:
#     print("No cashback added")
#     print("Total bill is:", purchase)



#20. read weight and height. bmi=weight/height*height ?
# weight=float(input("Enter weight:"))
# height=float(input("Enter height:"))
# bmi=weight/(height*height)
# print(f'the total bmi is :{bmi:.2f}')



#21.assign same value to two cars.check using is ?
# a=100
# b=a
# print(a is b)




#22.check coupon in list using in ?
# a=[1,2,3,4,5]
# b=a[2]
# print(b)



#23.check department in tuple ?
# departments = ("HR", "Finance", "IT", "Sales")
# dept = input("Enter department: ")
# if dept in departments:
#     print("Department found")
# else:
#     print("Department not found")



#24.use & to identify even/odd ?
# n=int(input("Enter number:"))
# if n&1==0:
#     print('even')
# else:
#     print('odd')    



#25.use << to double ?
# n=int(input("Enter number:"))
# res=n<<1
# print(res)



#26.use >>to halve ?
# n=int(input("Enter number:"))
# res=n>>1
# print(res)   



#27.use & on two permissions ?
# read = int(input("Enter read permission (0 or 1): "))
# write = int(input("Enter write permission (0 or 1): "))
# permission = read & write
# print("Permission:", permission)




#28.alaram is door or motion?
# door = input("Door open (yes/no): ")
# motion = input("Motion detected (yes/no): ")
# if door == "yes" or motion == "yes":
#     print("Alarm ON")
# else:
#     print("Alarm OFF")




#29.eligible if attendance>=75 or ptoject complete?
# attendance=int(input("Enter attendance:"))
# project=input("Enter project complete(yes/no):")
# if attendance>=75 or project=="yes": 
#     print('eligible')
# else:
#     print('not eligible')    




#30.board if passport,ticket,visa all true ?
# passport = input("Passport (yes/no): ")
# ticket = input("Ticket (yes/no): ")
# visa = input("Visa (yes/no): ")
# if passport == "yes" and ticket == "yes" and visa == "yes":
#     print("Boarding Allowed")
# else:
#     print("Boarding Denied")
 
          