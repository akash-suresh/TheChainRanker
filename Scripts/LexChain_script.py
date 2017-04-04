import sys

sys.path.append('../Lexrank/summa/')

from textrank import textrank


def summarize(filename,option):
    #LexicalChain(os.getcwd()+'/../filename')
    summary = textrank(filename,original=option,words=100)
    op_name='summary'+filename[4:]
    text_file = open('../RougeEval/syssum/PageRank/'+op_name, "w")
    text_file.write(summary)
    text_file.close()
    return

import os

counter = 1

for filename in os.listdir(os.getcwd()+'/../Raw_text/'):
        print filename
        option = 'pagerank'
        summarize(filename,option)
        counter = counter + 1
print counter

