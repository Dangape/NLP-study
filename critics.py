# Created by: Daniel Bemerguy 
# 19/12/2020 at 12:49
from bs4 import BeautifulSoup
import requests
import re
import pandas as pd
import numpy as np
import csv


movies = pd.read_csv("movies_metadata.csv")
columns = ["original_title","title","release_date","original_language"]
movies = movies.dropna(0)
titles = pd.DataFrame(movies[columns])
titles['release_date'] = pd.to_datetime(titles['release_date'], errors='coerce')

titles= titles[(titles['release_date'].dt.year >= 2010) & ((titles['original_language']) == ("en"))]
titles["original_title"] = titles["original_title"].apply(lambda x:x.lower())
titles["original_title"] = titles["original_title"].apply(lambda x:x.replace(" ","_"))
titles["original_title"] = titles["original_title"].apply(lambda x:x.replace(":",""))

print(titles.columns)

global data,number
columns = ["movies","critics"]
dict = {"movies": [],
        "critics": []}
df = pd.DataFrame()
data = []
number = []

movie = "toy_story_3"
for k in range(0,1):
    movie = titles.iloc[10,0]
    for j in range(0,20):
        url = "https://www.rottentomatoes.com/m/"+movie+"/reviews?type=top_critics&sort=&page="+str(j)
        html_content = requests.get(url).text
        soup = BeautifulSoup(html_content, "lxml")
        critics_list = soup.find_all("div", {"class": "the_review"}, text= True)
        for i in range(0,len(critics_list)):
            string = str(critics_list[i]) #O contador vai passar por toda a lista e converter seus elementos em string
            m = re.search('<div class="the_review">', string)
            end = m.end()
            n = re.search('</div>', string)
            start = n.start()
            critic = string[end:start]
            data.append(critic)
            data[i] = str(data[i]).strip()
        number.append(len(data))
        if len(number)>1 and number[j-1] == number[j]:
            break
        else:
            continue

for i in range(0,len(data)):
    data[i] = str(data[i]).strip()

print("There were found " + str(len(data)) + " critics for "+movie)
print(data)
