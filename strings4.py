# 1. remove all spaces ?
# s=input("Enter string:")
# rem=''
# for i in s:
#     if i!=' ':
#         rem+=i
# print(f'remove all spaces:{rem}')   



#2. camelcase to snake case ?
# s = input("Enter camelCase string: ")
# snake = ''
# for i in s:
#     if i >= 'A' and i <= 'Z':
#         snake += '_'
#         snake += chr(ord(i) + 32)   
#     else:
#         snake += i
# print(snake)  



# 3. snake case to camelcase ?
# s=input("Enter string:")
# camel=''
# under=0
# for i in s:
#     if i=='_':
#         under=1
#     elif under:    
#         camel+=chr(ord(i)-32)
#         under=0
#     else:
#         camel+=i
# print(camel)          


#4. uppercase to lowercase ?
# s=input("Enter string:")
# lower=''
# for i in s:
#     if i>='A' and i<='Z':
#         lower+=chr(ord(i)+32)
#     else:    
#         lower+=i
# print(f'uppercase to lowercase:{lower}')        




#5. lowercase to uppercase ?
# s= input("Enter string:")
# upper=''
# for i in s:
#     if i>='a' and i<='z':
#         upper+=chr(ord(i)-32)
#         upper+=i
# print(f'lower case to upper case:{upper}')        




#6. reverse every word ?
# s=input("enter string:")
# rev=''
# for i in s:
#     rev=i+rev
# print(f'reverse every word:{rev}')    



#7. remove duplicate charecters ?
# s=input("Enter string:")
# rem=''
# for i in s:
#     if i not in rem:
#         rem+=i
# print(f'remove duplicate char:{rem}')        




#8. count vowels and consonants ?
# s=input("Enter string:")
# vowels=0
# cons=0
# for i in s:
#     if i in 'AEIOUaeiou':
#         vowels+=1
#     elif (i>='A' or i<='Z') and (i>='a' or i<='z'):
#         cons+=1
# print(f'vowels count:{vowels}')
# print(f'consonants count:{cons}')            



#11.print only digits ?
# s=input("Enter string:")
# digits=0
# for i in s:
#     if i>='0' and i<='9':
#         digits+=1
# print(digits) 


#12. print only alphabets ?
# s=input("Enter string:")
# alphabets=''
# for i in s:
#     if (i>='A' and i<='Z') or (i>='a' and i<='z'):
#         alphabets+=i
# print(alphabets)        


#13. count words ?
# s=input("Enter string:")
# word=1
# for i in s:
#     if i==' ':
#         word+=1
# print(word)      



# 14. 

# 15. find longest word ?
# s=input("Enter string:")
# long=''
# word=''
# for i in s:
#     if i!=' ':
#         word+=i
#     else:
#         if len(word) > len(long):
#             long = word
#             word=''
# print("Longest word:", long)    



# 16 remove all digits ?
# s=input("Enter string:")
# rem=0
# for i in s:
#     if i not in '0987654321':
#         rem+=1
# print(rem)     


# 17. move digits to end?
# s = input("Enter string: ")
# char=''
# digit=''
# for i in s:
#     if i >= '0' and i <= '9':
#         digit+=i
#     else:
#         char+=i
# print(char+digit)

# 18. toggle case ?
# s = input("Enter string: ")
# swap=''
# for i in s:
#     if i>='A' and i<='Z':
#         swap+=chr(ord(i)+32)   
#     elif i>='a' and i<='z':
#         swap+=chr(ord(i)-32)   
#     else:
#         swap+=i                  
# print("Toggle case:", swap)



# 19. palindrome ?
# s=input("Enter string:")
# if s==s[::-1]:
#     print('palindrom')
# else:
#     print('not a palindrom')   



#20.compress charecters ?
s=input("Enter string:")
 
       
            
           