
# -*- coding: utf-8 -*-
"""
Created on Mon Nov 13 16:55:37 2017

@author: Aurélien
"""

from lxml import etree
import numpy as np
"""
import matplotlib.pyplot as plt // Comment this line for bug
"""

month_list = ['01','02','03','04','05','06','07','08','09','10','11','12']
journal_list = ['JDG','GDL']

for journal in journal_list:
    print("-------------------" + journal + "------------------------")
    for month in month_list:
        root = 'Corpus/'+journal+'/1967/' + month + '.xml'
        tree = etree.parse(root)
        text = []
        box_number = []
        key_word1 = 'mouvement'
        key_word2 = 'démocratique'
        key_word3 = 'féminin'
        
        print('-------Month : ' + month +'-------')
        
        for user in tree.xpath("/monthEntity/article/entity/full_text"):
            text.append(user.text)
            
        for box in tree.xpath("/monthEntity/article/entity/meta/box"):
            box_number.append(box.text)
            
        compteur1 = np.zeros((len(box_number), 1), dtype='i')
        compteur2 = np.zeros((len(box_number), 1), dtype='i')
        compteur3 = np.zeros((len(box_number), 1), dtype='i')
        
        for i in range(0,len(text)):
            try:
                p = text[i].split(' ')
            except(AttributeError):
                pass
            
            for j in range(0, len(p)):
                
                p[j] = p[j].partition(',')[0]   #Remove the commas
                p[j] = p[j].partition('.')[0]   #Remove the points
                
                if(p[j] == key_word1):       #Check for a word
                    compteur1[i] +=1
                    
                if(p[j] == key_word2):       #Check for a word
                    compteur2[i] +=1
                    
                if(p[j] == key_word3):
                    compteur3[i] += 1
                
    
        nothing = 1  
        for i in range(0,len(compteur1)):
            if(compteur1[i] >= 1 and compteur2[i]>=1 and compteur3[i]>=1):
                print(key_word1 +': {}' .format(int(compteur1[i])))
                print(key_word2 +': {}' .format(int(compteur2[i])))
                print(key_word3 +': {}' .format(int(compteur3[i])))
                print(box_number[i])
                nothing = 0
        
        if (nothing):
            print('Nothing')
        
