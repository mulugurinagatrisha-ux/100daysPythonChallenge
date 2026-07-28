# #1. longest consecutive consonant sequence ?
# s=input("Enter string:")
# longest=0
# count=0
# for i in s:
#     if i not in 'AEIOUaeiou':
#         count+=1
#         if count>longest:
#             longest=count
#     else:
#         count=0
# print(f'longest consecutive consonant sequence:{longest}')            




#2. Alternate case check ?
# s=input("Enter string:")
# count=0
# i=0
# for ch in s:
#     if 'A' <= s[0] <= 'Z':
#         if (i % 2 == 0 and 'A' <= ch <= 'Z') or (i % 2 != 0 and 'a' <= ch <= 'z'):
#             count += 1
#     else:
#         if (i % 2 == 0 and 'a' <= ch <= 'z') or (i % 2 != 0 and 'A' <= ch <= 'Z'):
#             count += 1
#     i += 1       
# if count==len(s): 
#     print("Alernating") 
# else:    
#     print("Not Alternating")  



#3. most frequent charecter ?
# s=input("Enter string:")
# high=0
# char=""
# for i in s:
#     count=0
#     for j in s:
#         if i==j:
#             count+=1
#     if count>high:
#         high=count
#         char=i
# print(char)        
                


#4. count words starting with a vowel ?
# s=input("Enter string:")
# words=s.split()
# count=0
# for word in words:
#     if word[0] in "AEIOUaeiou":
#         count=count+1
        
# print(f'count words starting with a vowel:{count}')        

            
#5. Remove consecutive duplicates ?
# s=input("Enter string:")
# result=''
# for i in s:
#     f=False
#     for j in result:
#         if i==j:
#             f=True
#             break
#     if f==False:
#         result+=i
# print(result)           



#6. longest word?
# s=input("Enter string:")
# n=s.split()
# max=0
# longest=''
# for i in range(len(n)):
#     if len(n[i])>=max:
#         max=len(n[i])
#         longest=n[i]
# print(f'longest word:{longest}')
# print(f'max length:{max}')               



#7.count charecter changes ?
# s1=input("Enter string:") 
# count=0
# for ch in range(len(s1)-1): 
#     if s1[ch]!=s1[ch+1]: 
#         count+=1 
# print(count)



#8. rotate string left by one postion ?
# s=input("Enter string:")
# s=s[1:]+s[0]
# print(f'rotate string left by one position:{s}')



#9. largest alphabetical word?
# s=input("Enter string:")
# n=s.split()
# largest=n[0]
# for i in n:
#     if i>largest:
#         largest=i
# print(f'largest alphabetical word:{largest}') 




#10. count palindromic words?
# s=input("Enter string:")
# n=s.split()
# count=0
# for ch in n:
#     rev=''
#     for i in ch:
#         rev=i+rev
#     if ch==rev:
#         count+=1    
# print("Palindromic words:", count)
          

