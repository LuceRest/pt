#import library
import tweepy
import re
import string
import pandas as pd
import numpy as np
import csv
 

###input key dan token
consumer_key='v9wwwwwIo8GZIPEOuhqBsPO76'
consumer_secret='3SHXLbNbWSatGGwQGNyWQHRnje0OGuf9i5bpgJxnT6atGOPxnp'

access_token='1493952640577044486-AoIoamI8ZuswcoWq06ayiHFal9BpQp'
access_token_secret='zneVVd7ScTfpslL2SMx8ynLJoHiFUv9Qad7oWs1BrQgxs'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret) 
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth,wait_on_rate_limit=True)

#####MotoGP Mandalika
# Open/Create a file to append data
csvFile = open('4th Meet (Wednesday, March, 2nd 2022)\Task\Data\Rusia.csv', 'a')
#Use csv Writer
csvWriter = csv.writer(csvFile)
 
for tweet in tweepy.Cursor(api.search_tweets,q="#rusia",count=2,lang="id").items():
    csvWriter.writerow([tweet.text.encode('utf8')])

# =========================

#read data
def load_data():
    data = pd.read_csv('4th Meet (Wednesday, March, 2nd 2022)\Task\Data\Rusia.csv')
    return data

#Pembuatan dataframe
teks = load_data()
teks = '''"b'Harga minyak dunia melonjak pada Selasa (1/3), dengan minyak mentah AS mencapai level tertinggi sejak Juni 2014 kar\xe2\x80\xa6 https://t.co/e3nHzH8Rto'"'''

# # teks = texts[0]
    
# Uppercase
print(teks.upper() + '\n')

# Lowercase
print(teks.lower() + '\n')

# Split teks
for i in re.split(' ', teks):
    print(i)
print()
    
# Replace karakter
print(teks.replace('a', 'o') + '\n')

# Join
kataJoin = "\t TRENDING!!"
print(teks.join(kataJoin) + '\n')




