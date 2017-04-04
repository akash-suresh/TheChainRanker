
# coding: utf-8

# In[71]:

def generate(filename,counter):
    f = open(filename,'r')
    text = f.read()
    a = text.split('\nIntroduction:\n')
    data = a[1]
    summary = a[0][10:]
    #print 'data', data
    text_file = open('Data/data_'+str(counter)+'.txt', "w")
    text_file.write(data)
    text_file.close()
    #print 'summary', summary
    text_file = open('Golden_summary/summary_'+str(counter)+'.txt', "w")
    text_file.write(summary)
    text_file.close()
    return


# In[72]:

import os
counter = 1
for filename in os.listdir(os.getcwd()):
    if 'txt' in filename:
        print filename
        generate(filename,counter)
        counter = counter + 1
print counter


# In[ ]:




# In[ ]:



