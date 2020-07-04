# -*- coding: utf-8 -*-
"""
Created on Thu Jun 18 13:08:43 2020

@author: katie
"""

def text_file(text):
    t1 = open("C://Users//katie//OneDrive//바탕 화면//수업//목요일수업//"+text,"r")
    text = t1.read()
    return text
    t1.close()
    
data=text_file("Obama_speech.txt")
print("####### Question 3-1 ########")
print(data)


def text_wo_punc(text):
    clean_data = data.replace("."," ").replace(","," ").replace("--"," ").replace("("," ").replace(")"," ").replace("?"," ").replace(";"," ").replace('"'," ").replace(":"," ")
    return clean_data

clean_data = text_wo_punc(data)
print("####### Question 3-2 ########")
print(clean_data)


print("####### Question 3-3 ########")
def freq_pron(w):
    words = clean_data.split()
    first_pron = ['I','me','mine','my','My']
    third_pron = ['we','our','us','ours','We','Our']

    freq_first_pron=dict()
    for w in first_pron:
        if w in words:
            freq = words.count(w)
            freq_first_pron[w] = freq
    print(freq_first_pron)
    total_first_pron = sum(freq_first_pron.values())
    
    freq_third_pron=dict()
    for w in third_pron:
        if w in words:
            freq = words.count(w)
            freq_third_pron[w] = freq
    print(freq_third_pron)
    total_third_pron = sum(freq_third_pron.values()) 
           
    return ("The frequency of first pronoun: {0}, The frequency of third pronoun: {1}".format(total_first_pron,total_third_pron))

compare_total = freq_pron(clean_data)     
print(compare_total) 
     


def max_w(w):
    words = clean_data.split()
    max_word_len=0
    max_word = ""
    for word in words:
        if max_word_len <len(word):
            max_word_len = len(word)
            max_word= word
    return max_word

max_word = max_w(clean_data)
print("####### Question 3-4 ########")
print("The longest word :",max_word)




