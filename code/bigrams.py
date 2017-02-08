
import os
cwd = os.getcwd()
path = "../data/"
# os.chdir(path)

import csv
import nltk
from nltk import word_tokenize
from nltk.util import ngrams
from collections import Counter
import re



Tweets = list()

with open(os.path.join(path, 'Tweet_nonZero_tolower.csv'), 'rb') as f:
	reader = csv.reader(f)
	for row in reader:
		Tweets.append(row)


testData = list()

with open(os.path.join(path, 'Test_semEval_tolower.csv'), 'rb') as f:
    reader = csv.reader(f)
    for row in reader:
        testData.append(row)




# tokenlist = list()
# bigramlist = list()

# for x in range(0, len(Tweets)):
# 	text = Tweets[x][0]
# 	tknzr = TweetTokenizer()
# 	token = tknzr.tokenize(text)
# 	tokenlist.append(token)
# 	#token = nltk.word_tokenize(text)
# 	bigram = ngrams(token,2)
# 	bigramlist.append(bigram)


# for grams in bigrams:
#   print grams

#-------------------------------START of BIGRAMS--------------------#
#-------------------------------UNIGRAMS AT THE END------------------#


#create the list of all bigrams
tokenlist = list()
bigramlist = list()

for x in range(0, len(Tweets)):
	sentence = Tweets[x][1]
	bigramls = []
	sixgrams = ngrams(sentence.split(), 2)
	for grams in sixgrams:
  		bigramls.append(grams)
  	bigramlist.append(bigramls)


#creating the list of bigrams
gramlist = list()
for grams in bigramlist[0:len(bigramlist)]:
  	#print grams
  	gramlist.append(grams)


#concatenateing the sentiment score of tweets with its bigrams 
#don't use it when you wanna do WEKA DATA PREPRATION 
for i in range(0, len(gramlist)) :
	gramlist[i].append(Tweets[i][0])


# making the bigrams ready for Weka!!! 
Wekabigram = list()

for item in gramlist:
	
	tweet = item[:-1]
	tclass = item[-1]
	if tclass!='0':
		tweetgram = []
		temp = []
		for i in tweet:
			tweetgram.append(i[0]+ "_" + i[1])
		temp = '"'+' '.join(tweetgram)+'"'
		#temp.append(tclass)
		line = [temp,tclass]
		Wekabigram.append(line)


#saving the dataset of bigrams with teir sentiment score prepared for WEKA 
# with open('bigramlist_sent_weka.txt', 'w') as f:
#     for row in Wekabigram:
#         #print row
#         f.write("%s\n" % str(row))

with open('bigramlist_sent_weka_test.csv','wb') as out:
	writer = csv.writer(out, delimiter=',')
	writer.writerows(Wekabigram)

#saving the list of bigrams with its sentiment score
with open('bigramlist_Wsent.txt', 'w') as f:
    for row in gramlist:
        #print row
        f.write("%s\n" % str(row))


#unlist the list of list and creat one list of bigrams
l = gramlist
ll = [item for sublist in l for item in sublist]
gramcount = Counter(ll)

fdistbi = FreqDist(gramcount)

#most common bigrams
grammostcommon = gramcount.most_common(200)

#saving the list of bigrams
with open('gramlist.txt', 'w') as f:
    for row in gramlist:
        #print row
        f.write("%s\n" % str(row))

with open('gramcommon.txt', 'w') as f:
    for row in grammostcommon:
        #print row
        f.write("%s\n" % str(row))




#list of counters of each tweet 
tlist = list()
for x in range(0, len(bigramlist)):
	tlist.append(Counter(bigramlist[x]))

#saving the list of counters
with open('test.txt', 'w') as f:
    for row in tlist:
        #print row
        f.write("%s\n" % str(row))



#stopwords removal for bigrams

stopwrds = ['to', 'the', 'an ','a', 'for', 'on', 'in', 'is', 'of', 'this', 'and', 'be', 'at', 'are', 'with', 'I', 'some', 'In', 'it', 'that', 'from', 'has', 'have', 'my' , 'by' , 'just', '&' , 'as', 'into', 'The', 'about', 'its',  'been', 'not', 'you', 'To','but', 'we', 'Are', 'no', 'these', 'Will', 'so', 'can', 'after', 'With', 'On', 'off', 'if', 'than', 'could', 'And', 'would', 'they',  'Out', 'should', 'another']


filtered=[]
for pairs in ll[0:len(ll)]:
	if pairs[0] in stopwrds or pairs[1] in stopwrds:
		continue
	filtered.append(pairs)

fdistbi_Stopwrds = FreqDist(filtered)

#most common bigrams
fdistbi_Stopwrds_common = fdistbi_Stopwrds.most_common(50)
fdistbi_Stopwrds.plot(50, cumulative=True)




# ------------End of bigram ------# 
#-------------Begin of unigram----#


#create the list of all unigrams
unigramlist = list()


for x in range(0, len(Tweets)):
	sentence = Tweets[x][0]
	#unigramls = []
	unigrams = sentence.split()
  	unigramlist.append(unigrams)


u = unigramlist
uu = [item for sublist in u for item in sublist]

ucount = Counter(uu)
unigramlist = ucount.most_common(20000)

text1 = uu
fdist1 = FreqDist(text1)
print(fdist1)
#<FreqDist with 2729 samples and 8549 outcomes>

fdist1.most_common(100)
fdist1.plot(100, cumulative=True)


#--------------character removal and stopwords removal for whole tweets
TweetsCopy = Tweets
# TweetsCopy = Mech
TweetsCopy = testData



TweetsCharRemoved = list()

for row in TweetsCopy:
		sentence = row[0]
		# sentence = re.findall("^'(.*)'$", sentence)
		sentence = re.sub('[!:@#$.$?;,\'\"]', '', sentence)
		TweetsCharRemoved.append(sentence)
		row[0] = sentence

stopwrds = ['to', 'the', 'an','a', 'for', 'on', 'in', 'is', 'of', 'this', 'and', 'be', 'at', 'are', 'with', 'I', 'some', 'in', 'it', 'that', 'from', 'has', 'have', 'my' , 'by' , 'just', '&' , 'as', 'into', 'the', 'about', 'its',  'been', 'not', 'you', 'to','but', 'we', 'are', 'no', 'these', 'will', 'so', 'can', 'after', 'with', 'on', 'than', 'could', 'and', 'would', 'they',  'out', 'another' , 'i']

for i in range(1, len(TweetsCopy)):
	filtered_words = TweetsCopy[i][0]
	# print("filtered words: ----- \n ", filtered_words)
	unigrams = filtered_words.split()
	x = [word for word in unigrams if word not in stopwrds]
	# print("x : ----- \n ", x)
	x = " ".join(x)
	TweetsCopy[i][0] = x
	# print("row[0] : ----- \n ", TweetsCopy[i][0])

with open('Test_SemEval_stopwordRmv_CharRmv.csv','wb') as out:
	writer = csv.writer(out, delimiter=',')
	writer.writerows(TweetsCopy)

#-------------stopwords removal 

stopwrds = ['to', 'the', 'an','a', 'for', 'on', 'in', 'is', 'of', 'this', 'and', 'be', 'at', 'are', 'with', 'I', 'some', 'in', 'it', 'that', 'from', 'has', 'have', 'my' , 'by' , 'just', '&' , 'as', 'into', 'the', 'about', 'its',  'been', 'not', 'you', 'to','but', 'we', 'are', 'no', 'these', 'will', 'so', 'can', 'after', 'with', 'on', 'than', 'could', 'and', 'would', 'they',  'out', 'another']
filtered_words = [word for word in uu if word not in stopwrds]
fdist_stopwrds = FreqDist(filtered_words)
fdist_stopwrds.most_common(50)
fdist_stopwrds.plot(50, cumulative=True)


with open('unigram_withstopwords.txt', 'w') as f:
    for row in uu:
        #print row
        f.write("%s\n" % str(row))


with open('unigram_no_stopwords.txt', 'w') as f:
    for row in filtered_words:
        #print row
        f.write("%s\n" % str(row))


# #counter help 

# import collections
# a = [1,1,1,1,2,2,2,2,3,3,4,5,5]
# counter=collections.Counter(a)
# print(counter)
# # Counter({1: 4, 2: 4, 3: 2, 5: 2, 4: 1})
# print(counter.values())
# # [4, 4, 2, 1, 2]
# print(counter.keys())
# # [1, 2, 3, 4, 5]
# print(counter.most_common(3))
# # [(1, 4), (2, 4), (3, 2)]





