import wordcloud
import numpy as np
from matplotlib import pyplot as plt
import io
import sys

def calculate_frequencies(file_contents):
    # Here is a list of punctuations and uninteresting words you can use to process your text
    punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
    uninteresting_words = ["the", "a", "to", "if", "is", "it", "of", "and", "or", "an", "as", "i", "me", "my", \
    "we", "our", "ours", "you", "your", "yours", "he", "she", "him", "his", "her", "hers", "its", "they", "them", \
    "their", "what", "which", "who", "whom", "this", "that", "am", "are", "was", "were", "be", "been", "being", \
    "have", "has", "had", "do", "does", "did", "but", "at", "by", "with", "from", "here", "when", "where", "how", \
    "all", "any", "both", "each", "few", "more", "some", "such", "no", "nor", "too", "very", "can", "will", "just"]
    
    new_file=""
    for x in file_contents:
        if x not in punctuations:
            new_file+=x
    words=new_file.split()
    dicti={}
    for word in words:
        if word.lower() not in uninteresting_words:
            if word not in dicti.keys():
                dicti[word]=0
            dicti[word]+=1
    #wordcloud
    cloud = wordcloud.WordCloud()
    cloud.generate_from_frequencies(dicti)
    return cloud.to_array()

file_contents='''In sooth I know not why I am so sad,
It wearies me. you say it wearies you;
But how I caught it, found it, or came by it,
What stuff ’tis made of, whereof it is born,
I am to learn.
And such a want-wit sadness makes of me,
That I have much ado to know myself.'''

myimage = calculate_frequencies(file_contents)
plt.imshow(myimage, interpolation = 'nearest')
plt.axis('off')
plt.show()
