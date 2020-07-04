# -*- coding: utf-8 -*-
"""
Created on Thu Jun 18 12:55:40 2020

@author: katie
"""


print("####### Question 2-1 ########")

text = open("C://Users//katie//OneDrive//바탕 화면//수업//목요일수업//wsj_partial.txt","r")
text = text.read()
print(text)


import re
word = re.compile("[A-Za-z0-9]+/[A-Z]*")
word = word.findall(text)

word_dic = {}
i=0
for w in word:
    wo_key = (word[i].split("/"))[0]
    wo_value =(word[i].split("/"))[1]
    i += 1
    word_dic[wo_key] = wo_value
print(word_dic)


print("####### Question 2-2 ########")
new_word_dic = {}
for word,pos in word_dic.items():
    if pos == "VBN":
        pos = "VB"
        word = word[:-1]
    elif pos == "NNS":
        pos = "NN"
        word = word[:-1]
    elif pos == "VBZ":
        pos ="VB"
        if word == "is":
            word = "be"
        elif word == "has":
            word = "have"
        else:
            word = word[:-1]
    elif pos =="VBD":
        pos = "VB"
        if word == "said":
            word ="say"
        else:
            word = word[:-2]
    elif pos == "VBG":
        pos = "VB"
        word = word[:-3]+"e"
    elif pos == "VBP":
        pos = "VB"
        word = word
    new_word_dic[word] = pos
print(new_word_dic)

print("####### Question 2-3 ########")
dic = open("C://Users//katie//OneDrive//바탕 화면//수업//목요일수업//dic.txt","w")
sort_list = sorted(new_word_dic.items())
sort_dic = dict(sort_list)
for key,value in sort_dic.items():
    print(key,":",value)
    dic.write(key+":"+value+"\n")
print(dic)
dic.close()


print("####### Question 2-4 ########")
noun_list = []
verb_list = []
for word,pos in new_word_dic.items():
    if pos == "NN":
        word = noun_list.append(word)
    elif pos =="VB":
        word = verb_list.append(word)
        
print("#### noun list #######"+"\n",noun_list)
print("#### verb list #######"+"\n",verb_list)



