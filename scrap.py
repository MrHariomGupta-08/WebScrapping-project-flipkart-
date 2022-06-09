#hariom gupta
from bs4 import BeautifulSoup 
import requests 
import csv
import pandas as pd
#now we will request to access a link with the help of request module
url="https://www.flipkart.com/search?q=laptop&sid=6bo%2Cb5g&as=on&as-show=on&otracker=AS_QueryStore_OrganicAutoSuggest_1_6_na_na_na&otracker1=AS_QueryStore_OrganicAutoSuggest_1_6_na_na_na&as-pos=1&as-type=RECENT&suggestionId=laptop%7CLaptops&requestId=7ec220e8-4f02-4150-9e0b-9e90cf692f4b&as-searchtext=laptop"
response = requests.get(url)
#now we will fect the html data of the url page
htmlcontent = response.content
soup = BeautifulSoup(htmlcontent,"html.parser")
#now we will make list to store the name ,price and rating of the product.
products=[]
prices=[]
ratings=[]
#now we have to controll a loop to fetch all the data from the requested url
for a in soup.findAll('a',href=True, attrs={'class':'_1fQZEK'}):
  name=a.find('div',attrs={'class':'_4rR01T'})
  price=a.find('div',attrs={'class':'_30jeq3 _1_WHN1'})
  rating=a.find('div',attrs={'class':'_3LWZlK'})
#now we will input all the fetched data in the lists
  products.append(name.text)
  prices.append(price.text)
  ratings.append(rating.text)
# making the data base for the data with the help of pandas
  import pandas as pd
df = pd.DataFrame({'Product Name':products,'Prices':prices,'Ratings':ratings})
df.head(30)
# now we will store the data into a csv file
df.to_csv('products.csv')
# converting the csv file to the downloadable xlx file
import pandas as pd
df = pd.read_csv("products.csv")
df.to_excel("productsdata.xlsx", sheet_name="proudcts.csv", index=False)
#this is code is written on google colab.
