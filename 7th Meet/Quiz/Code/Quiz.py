import nltk


# ---------------| No 1 |---------------
'''
text="Last week, the University of Cambridge shared its own research that shows if everyone wears a mask outside home,dreaded ‘second wave’ of the pandemic can be avoided."

tokens=nltk.word_tokenize(text )
for token in tokens :
  print (token )

'''

# ---------------| No 2 |---------------
'''
from nltk.tokenize import WordPunctTokenizer

text = "Reset your password if you just can't remember your old one."

print ("\nOriginal string:")

print(text)

result = WordPunctTokenizer() .tokenize(text )

print("\nSplit all punctuation into separate tokens:")

print(result )

'''

# ---------------| No 4 |---------------
'''
from nltk.corpus import stopwords

stoplist = stopwords.words ('english')

text = '

Virus Corona atau severe acute respiratory syndrome coronavirus 2

(SARS-CoV-2) adalah virus yang menyerang sistem pernapasan. 

Penyakit akibat infeksi virus ini disebut COVID-19. Virus Corona bisa 

menyebabkan gangguan ringan pada sistem pernapasan, infeksi paru-paru yang berat, 

hingga kematian.

'

print("\nOriginal string:")

print(text )

clean_word_list = [ word for word in text.split () if word not in stoplist]

print("\nAfter removing stop words from the said text:")

print(clean_word_list )

'''

# ---------------| No 5 |---------------
'''
text=" Makan bersama kawan di Jogja #jogja #liburan #liburanakhirpekan. Makan siang @Pantaikuta restro smile "

import re

text=re.sub(r'[^\w]', ' ', text )

from nltk.tokenize import TweetTokenizer

tokenizer=TweetTokenizer ()

print(tokenizer .tokenize(text))

'''


# ---------------| No 3 |---------------

from nltk.corpus import names 
import random 
 
male_names = names.words('male.txt')
female_names = names.words('female.txt')
 
labeled_male_names = [(str(name), 'male') for name in male_names]
labeled_female_names = [(str(name), 'female') for name in female_names]
labeled_all_names = labeled_male_names + labeled_female_names
random.shuffle(labeled_all_names)
print("First 15 random labeled combined names:")
print (labeled_all_names[:15])





