#Program in python3 to download comics from a range x to y given by a user
#Run the code by typing: python3 xkcd_comic_downloader.py to make it work correctly
#Also don't forget to change the directory in the program, where you want your downloaded files to be saved
#All the downloaded comics are saved in /home/srajan/Downloads (In this program) 
#Written by SRAJAN GUPTA

from bs4 import BeautifulSoup
import requests
import urllib.request
import os
x = int(input("Enter the first param: "))
y = int(input("Enter the Second param: "))
list = [x,y]
title_text = ""
if (not x>y) and (x>=1 and y>=1):
        while x<=y:
                os.chdir('/home/srajan/Downloads')
                url = 'https://www.xkcd.com/{}'.format(x)
                response = requests.get(url)
                if response.status_code == 200:
                        html = response.text
                        soup = BeautifulSoup(html,'html.parser')
                        title = soup.title
                        title_text = title.text+" comic_num: {}".format(x)
                        print(title_text)
                        tag = soup.find(id="comic")
                        tag_img = tag.img["src"]
                        tag_img_link = "https:{}".format(tag_img)
                        filename = str(tag_img_link.split('/')[-1])
                        download = urllib.request.urlretrieve(tag_img_link,filename)
                        op = "Comic: {} downloaded".format(title_text)
                        print(op)
                        op1 = "File saved in: {}".format('/home/srajan/Downloads')
                        print(op1)
                else:
                        error = response.status_code
                        op = "Comic: {} cannot be downloaded due to error {}".format(title_text,error)
                        print(op)
                x = x + 1
else:
        print("please enter valid paramaters")



