# -*- coding: utf-8 -*-
"""
Created on Thu Jun 18 11:28:12 2020

@author: katie
"""


print("####### Question 1-1 ########")
num = int(input("입력할 숫자는?"))
if num % 2 ==0:
    print("입력한 숫자는 짝수입니다.")
elif num % 2 == 1:
    print("입력한 숫자는 홀수입니다.")
    
print("####### Question 1-2 ########")
a = "It was fantastic"
if "fantastic" in a:
    print("fantastic")

word = a.split()
for w in word:
    if w == "fantastic":
        print(w)


print("####### Question 1-3 ########")
word = ['placement','neutral','attracting','effect','delivery']
len_word = {}
for w in word:
    len_word[w] = len(w)
    print("The length of the word",'"'+w+'"',"is",len(w))
print(len_word)



data = "The new coronavirus’s link to a market in China is the latest example of an infection that likely spread from animals to people."

print("####### 1-4(a) ########")
d_lower = data.lower()
print(d_lower)

print("####### Question 1-4(b) ########")
clean_data = d_lower.replace("’"," ").replace("."," ")
print(clean_data)

print("####### Question 1-4(c) ########")
clean_data = d_lower.replace("."," ")    #coronavirus's가 붙어있어야될거같아서 문장부호지우는 문제에서는 지웠는데 다시 붙였습니다.
words = clean_data.split()
print(words)
sentence = ''
for w in words:
    sentence = sentence + w + " "
print(sentence)

print("####### Question 1-4(d) ########")
total_words = len(words)
print("totoal words = " , total_words)

uni_word_list = list(set(words))
total_uni_word = len(uni_word_list)
print("uni words = " , total_uni_word)

print("####### Question 1-4(e) ########")
asc_list = sorted(uni_word_list)
print(asc_list)







