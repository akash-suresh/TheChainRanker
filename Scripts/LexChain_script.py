import sys

sys.path.append('../')

from LexChain.Boochain import LexicalChain
from Lexrank.summa.textrank import textrank


def summarize(filename,option):
    #LexicalChain(os.getcwd()+'/../filename')
    summary = textrank(filename,original=1,words=100)
    text_file = open('Golden_summary/summary_'+str(counter)+'.txt', "w")
    text_file.write(summary)
    text_file.close()
    return


import os

counter = 1

for filename in os.listdir(os.getcwd()+'/../Raw_text/'):
    if 'txt' in filename:
        print filename
        option = 'lexchain'
        #summarize(filename,option)
        counter = counter + 1
print counter

