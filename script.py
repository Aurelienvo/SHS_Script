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

total_article = 0

years = range( 1971, 1990, 1)
month_list = ['01','02','03','04','05','06','07','08','09','10','11','12']
journal_list = ['JDG','GDL']

filecp = open( 'keywords_education.txt', encoding='utf-8' )
key_words = filecp.read().split('\n')

for journal in journal_list:
    print("-------------------" + journal + "------------------------")
    
    for year in years :
        print("-------------------" + str(year) + "------------------------")
        
        for month in month_list:
            print('-------Month : ' + month +'-------')
            
            root = '../'+journal+'/'+ str(year) + '/' + month + '.xml'
            tree = etree.parse(root)
            
            articles = []
            titles = []
            dates=[]

            for article in tree.xpath("/monthEntity/article/entity/full_text"):
                articles.append(article.text)

            for title in tree.xpath("/monthEntity/article/entity/meta/name"):
                titles.append(title.text)
                
            for date in tree.xpath("/monthEntity/article/entity/meta/issue_date"):
                dates.append(date.text)
                

            for i in range(0,len(articles)):
                
                cpt = 0
                kw = key_words.copy()
                
                try:
                    words = articles[i].split(' ')
                except(AttributeError):
                    pass

                
                for j in range(0, len(words)):

                    
                    words[j] = words[j].replace(',','')   #Remove the commas
                    words[j] = words[j].replace('.', '')  #Remove the points

                    if words[j] in kw  :
                        kw.remove(words[j])
                        cpt += 1
                    
                    if cpt >= 5 :
                        total_article += 1
                        print( total_article )
                        break