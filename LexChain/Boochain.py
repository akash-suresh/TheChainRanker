import nltk
from nltk.corpus import wordnet as wn
from nltk.corpus import wordnet_ic
import re

import sys
reload(sys)
sys.setdefaultencoding('utf8')
sys.path.append('../Lexrank')

from summa.preprocessing.textcleaner import clean_text_by_sentences as clean


def LexicalChain(fileName="amazon.txt", verbose=0):

	def findWholeWord(w):
		return re.compile(r'\b({0})\b'.format(w), flags=re.IGNORECASE).search
		
	#class Chain 
	class Chain(): 
	    def __init__(self, words, senses, count = 0):
	    	self.words = set(words)
	    	self.senses = set(senses)
	    	dictionary[words[0]] = 1 #initialize counter
		
	    def addWord(self, word):
	        
	        if(len(self.words.intersection([word])) > 0):
	            dictionary[word] += 1
	        else:
	            dictionary[word] = 1
	        
	        self.words.add(word)
		

	    def addSense(self, sense):
		   self.senses.add(sense)

	    def getWords(self):
		   return self.words

	    def getSenses(self):
		   return self.getSenses

	    def incCount(self):
			self.count += 1

	    def setScore(self, sc):
			self.score = sc

	    def mfword(self):
			maxfreq = 0
			for word in self.getWords():
				if dictionary[word] > maxfreq:
					maxword = word	
					maxfreq = dictionary[word]
			return maxword

	def add_word(word):
	    maximum = 0 
	    maxJCN = 0
	    flag = 0
	    for chain in lexical_chains: #for all chains that are present
		for synset in wn.synsets(word): #for all synsets of current word
		    for sense in chain.senses:  #for all senses of the current word in current element of the current chain
		        similarity = sense.wup_similarity(synset) #using wup_similarity
		        
		        if(similarity >= maximum):
		            if similarity >= threshold:
		                #print word, synset, sense, sense.jcn_similarity(synset, brown_ic)
		                JCN = sense.jcn_similarity(synset, brown_ic) #using jcn_similarity
		                if JCN >= jcnTreshold: 
		                    if sense.path_similarity(synset) >= 0.2: #using path similarity
		                        if JCN >= maxJCN:
		                            maximum = similarity
		                            maxJCN = JCN
		                            maxChain = chain
		                            flag = 1
	    if flag == 1:	               	                    
	        maxChain.addWord(word)
	        maxChain.addSense(synset)
	        return
			    
	    lexical_chains.append(Chain([word], wn.synsets(word)))


	def count_words(summary):
		count = 0
		for line in summary:
			count = count + len(line.split(' '))
		return count
	#fileName = raw_input("Enter file path + name, if file name is 'nlp.txt', type 'nlp' \n \n")
	#n = raw_input("Enter number of sentences in summary.\n")

	#fileName = "nlp.txt"
	threshold = 0.6 #treshold for wup
	jcnTreshold = 0.09 #jcn
	pathTeshold = 0.1 #path
	brown_ic = wordnet_ic.ic('ic-brown.dat') #load the brown corpus
	lexical_chains = [] #empty list to hold all the chains
	dictionary = {} #empty dictionart to hold the count of each word encountered
	word_count=50
	File = open(fileName) #open file
	lines = File.read() #read all lines
	#dec_lines =  [line.decode('utf-8') for line in lines] 
	#print [clean_line.token for clean_line in clean_lines]

	clean_lines = clean(lines)
	line_list = [clean_line.text for clean_line in clean_lines]
	is_noun = lambda x: True if (pos == 'NN' or pos == 'NNP' or pos == 'NNS' or pos == 'NNPS') else False
	nouns = [word for (word, pos) in nltk.pos_tag(nltk.word_tokenize(lines)) if is_noun(pos)]  #extract all nouns


	for word in nouns:
	    add_word(word)

	#print all chains
	for chain in lexical_chains:
		chain_length = 0
		dis_word = 0
		for word in chain.getWords():
			#print str(word + "(" + str(dictionary[word]) + ")") + ',',
			chain_length = chain_length + dictionary[word]
			dis_word = dis_word + 1
		#print 'Length =' + str(chain_length)
		hom = 1 - (dis_word*1.0/chain_length)
		#print 'Homogeneity =' + str(hom)
		score = 1.0*chain_length*hom
		#print 'Score =' + str(score)
		chain.setScore(score)

	#print 'Sorted start '
	lexical_chains.sort(key=lambda x: x.score, reverse=True)
	verbose=1
	if verbose==1:
		for chain in lexical_chains:
			if(chain.score>0.0):
				for word in chain.getWords():
					print str(word + "(" + str(dictionary[word]) + ")") + ',',
				print 'Score=' + str(chain.score)

	summary = []
	line_flags = []
	line_score=[]

	for line in line_list:
		line_flags.append(0)
		line_score.append(0)

	for chain in lexical_chains:
	
		bigword = chain.mfword()
		chain_score = chain.score
		#print '\nMF word ', bigword
		for i in range(len(line_list)):
			line=line_list[i]
			try:
				x = findWholeWord(bigword)(line) 
			except:
				#print 'Exception : Error in finding word'
				x = None
			if x!=None:
				#((line.find(' '+str(bigword)+' ')!=-1) or (line.find(' '+str(bigword)+'.')!=-1)):
				if line_flags[i]==0:
					#summary.append(line)
					#print 'i  ', count_words(summary)
					line_flags[i] = 1
					line_score[i] = chain_score
					#print 'line_score ', line_score
					#print 'line_flags ', line_flags

					break
				#elif line_flags[i]==1:
					#line_score[i] = line_score[i] + chain.score
					#print '\nline_score ', line_score
					#print 'line_flags ', line_flags
			

	'''
		if(count_words(summary)>word_count):
			break			

	'''
	bias = 20
	tot_score = 0
	for i in range(len(line_score)):
		line_score[i] = (line_score[i]*bias)+1

	for score in line_score:		
		tot_score = tot_score + score

	for i in range(len(line_score)):
		line_score[i] = (line_score[i]/tot_score)

	print line_score

	namscores = dict(zip([sentence.token for sentence in clean_lines],line_score))

	#print namscores
	#print len(summary)
	#print line_score

	#final_summary = ' '.join(summary)
	#print final_summary
	return namscores

#print LexicalChain(verbose=1)