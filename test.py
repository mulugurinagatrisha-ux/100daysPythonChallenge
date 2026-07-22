# # 1.write a program that accepts an integer and prints 
# # whether it is positive,negative or zero ?

# n=int(input("Enter a number:"))
# if n>0:
#     print('Postive number')
# elif n<-1:
#     print('Negative number')
# else:
#     print('zero') 
    
    
# # 2. write a program that takes a students marks as input and prints:
# # "pass" if marks are 40 or more
# # "fail" otherwise 

# marks=int(input("Enter student marks:"))
# if marks>=40:
#     print('you are passed. your marks are:',marks)
# else:
#     print('you are failed. your are marks are:',marks)          
        

# # 3. write a program that checks whether a given year is 
# # leap year ?

# year=int(input("enter year:"))
# if (year%400==0) or (year%4==0 and year%100!=0):
#     print('leap year')
# else:
#     print('ordinary year')  
    
    
   
# # 4. using for loop print all even numbers from 1 to 50 ?
# n=int(input("number:"))
# for i in range(1,n+1):
#     if i%2==0:
#         print(i)
     
     
     
# # 5. write a program to find sum of all numbers
# # from 1 to n, where n is entered by the user.
# n=int(input("Enter number:"))
# sum=0
# for i in range(1,n+1):  
#     sum=sum+i
# print('sum',sum)
   
      

# # 6. write a program that counts how many digits are
# # present in a numbers entered by the user?
# numbers=input("Enter numbers:")
# count=0
# for digit in numbers:
#     count+=1
# print('count:',count)
    



# # 7. using a loop print the multiplication
# # table of a number entered by the user up to 10 ?
# num=int(input("Enter number:"))
# for i in range(1,11):
#     print(num,'x',i,'=',num*i)
# print()        



# # 8. define a function is_even(number) that returns
# # true if the number is even otherwise returns false.

# def is_even(number):
#     if number%2==0:
#         print('True')
#     else:
#         print('False') 
# is_even(4)    

       
        
# # 9. define a function largest_of_three(a,b,c) that returns
# # the largest of three numbers without using max() .
# def largest_of_three(a,b,c):
#     if a>b:
#         print('largest is',a)
#     elif b>c:
#         print('largest is',b)
#     else:
#         print('largest',c)        
# largest_of_three(10,20,30)                         
              

# # 10.Define a function count_vowels(text) that returns 
# # the number of vowels in a given string.
# def count_vowels(text):
#     count=0
#     vowels='aeiouAEIOU'
#     for letter in text:
#         if letter in vowels:
#             count+=1
#     return count
# print(count_vowels("python"))        
        
          

# # 11. given this lsit:
# # numbers=[3,8,12,5,7,10,15]
# # using a list comprehension create a new list  
# # # list containing only even numbers?

# numbers=[3,8,12,5,7,10,15]
# print(Evennumbers:=list(i for i in numbers if i%2==0))   


# # 12. given this list:
# # use a dict comprehension to create a dict wher eeach word 
# # is a key and its lenght is the value.

# words=["python","java","c","javascript","go"]   
# print(word_dict:={word: len(word) for word in words})   