import bs4
from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup
import numpy as np
import sqlite3
import  pandas as pd
from selenium import webdriver
from selenium import webdriver


# -------------------------------------------- Parent article --------------------------------
for sub in range(1,24):
    try:
        print("Subject Number",sub)
        # Change URL here
        url = "https://sattacademy.com/admission/question.php?" \
              "category=du&year=447&unit=1569&subject={}".format(str(sub))
        # url=input("URL :")

        # start=input("Start loop Form :")
        # open page
        my_page = uReq(url)
        page_html = my_page.read()
        my_page.close()

        page = soup(page_html, "html.parser")

        child = page.find_all("div", {"class": "col-sm-12 mt-2"})
        #print(child[0].text)
        Q = []
        O0 = []
        O1 = []
        O2 = []
        O3 = []
        R8 = []


        for x in range(0,len(child)):

            #question-----------
            qus = child[x].find_all("h5", {"class": "card-title card-title-single"})
            qus = qus[0].text
            #print("Question ",qus)
            Q.append(qus)

            # right ans-----------
            right_ans = child[x].find_all("p", {"class": "answer rightAns"})
            right_ans=right_ans[0].text
           # print("Right Ans:",right_ans)
            R8.append(right_ans)


            #all ans------------

            ans = child[x].find_all("div", {"class": "col-sm-6"})
            temp=0
            l=1
            for i in ans:

                if  temp==0 :
                    O0.append(i.text)
                    temp += 1
                  #  print(i.text)
                elif temp==1:
                    O1.append(i.text)
                    temp+=1
                  #  print(i.text)
                elif temp==2:
                    O2.append(i.text)
                    temp += 1
                  #  print(i.text)
                elif temp==3:
                    O3.append(i.text)
                    temp += 1
                  #  print(i.text)

        df = pd.DataFrame()
        df['Question'] = Q
        df['Option 1'] = O1
        df['Option 2'] = O2
        df['Option 3'] = O3
        df['Option 4'] = O0
        df['Answer'] = R8
        df.fillna(value=0)

        df.to_csv('Dhaka Qus -{}.csv'.format(sub), encoding='utf-8-sig')
    except:
        print("Cannot get sub-",sub)
        pass
    #




print("Done")