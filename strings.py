# # 1. count upper case and lower case letters ?
# string=input("Enter string:")
# upper=0
# lower=0
# for ch in string:
#     if ch>'A' and ch<'Z':
#         upper+=1
#     else:
#         lower+=1
# print(f'upper case:{upper}')  
# print(f'lower case:{lower}')   



# #2. longest word length ?
# word=input("Enter word:")
# longest=0
# count=0
# for ch in word:
#     if ch!=" ":
#         count+=1
#         if count>longest:
#             longest=count
#     else:
#         count=0    
# print(f'longest word length:{count}')   



#3. count vowels in even positions ?
# s=input("Enter word:")
# count=0
# pos=0
# for ch in s:
#     if pos%2==0:
#         if ch=='a' or ch=='e' or ch=='i' or ch=='o' or ch=='u' or ch=='A' or ch=='E' or ch=='I' or ch=='O' or ch=='U':
#             count+=1
#     pos+=1    
# print(f'count of vowels in even places:{count}')  



# #4. consecutive duplicate charecters ?
# s=input("Enter word:")
# count=0
# for ch in range(len(s)-1):
#     if s[ch]==s[ch+1]:
#         count+=1
# print(f'consecutive duplicate charecters:{count}')  


#5. first non repeating charecter ?
# s=input("Enter word:")
# for ch in s:
#     count=0
#     for j in s:
#         if ch==j:
#             count+=1
#     if count==1:
#         break
# print(f'non repeating charecter:{ch}')            
      


#6. longest consecutive vowel sequence ?
# s=input("Enter word:")
# longest=0
# count=0
# for ch in s:
#     if ch=='a' or ch=='e' or ch=='i' or ch=='o' or ch=='u' or ch=='A' or ch=='E' or ch=='I' or ch=='O' or ch=='U':
#         count+=1
#         if count>longest:
#             longest=count
#     else:
#         count=0
# print(f'longest consecutive vowel sequence:{longest}')     



#7. charecter frequency ?
# s=input("Enter a string:") 
# p=input("Enter a charecter:")
# count=0
# for ch in s:
#     if ch==p:
#         count+=1
# print(f'charecter frequency:{count}')  


#8. mirror string check ?
# s=input("Enter word:")
# i = ""
# for ch in s:
#     i = ch + i
# if s==i:
#     print("Palindrome")
# else:
#     print("Not Palindrome")
    
    
#9. largest alphabet ?
# s=input("Enter word:")
# g=''
# for ch in s:
#     if ch>g and ('A'>=ch<='Z' or 'a'>=ch<='z'):
#         g=ch
# print(f'largest alphabet:{g}')        
