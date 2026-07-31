#1. longest repeating charecter block ?
# s=input("Enter string:")
# c=input("Enter charecter:")
# longest=0
# count=0
# for i in s:
#     if i==c:
#         count+=1
#         if count>longest:
#             longest=count
#     else:
#         count=0        
   
# print(f'length of charecter:{longest}')        
            


#2. charecters between two letters ?

# s = input("Enter string: ")
# c = input("Enter character: ")
# first = -1
# last = -1
# for i in range(len(s)):
#     if s[i] == c:
#         if first == -1:
#             first = i
#         last = i

# if first == last:
#     print(-1)
# else:
#     print(last - first - 1) 



#3. word with maximum vowels ?
# s=input("Enter string:")
# words=s.split()
# max_vowels=0
# max_word=''
# for word in words:
#     count=0
#     for ch in word:
#         if ch in 'AEIOUaeiou':
#             count+=1
#     if count>max_vowels:
#         max_vowels=count
#         max_word=word
# print(f'word in a string:{max_word}')
# print(f'vowels in a word:{max_vowels}')     



#4. consecutive alphabet check?
# s=input("Enter string:")
# n = 1
# for i in range(len(s) - 1):
#     if ord(s[i + 1]) - ord(s[i]) != 1:
#         n=0
#         break

# if n:
#     print("yes")
# else:
#     print("no")


# 5. reverse every word ?
# s=input("Enter string:")
# words=s.split()
# for word in words:
#     print(word[::-1],end=' ') 



#6.    
           
                    