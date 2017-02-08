
WD <- "/Users/narges/Dropbox/2-Courses/[Seventh Semester]/Machine Learning/Assignment/Decision Trees"

setwd(WD)

library(ROAuth)
library(plyr)
library(stringr)
library(ggplot2)
library(twitteR)
library(httr)
library("RCurl")
library("bitops")
library("rjson")
library("streamR")
library("ROAuth")
library("httr")
library("plyr")
library("stringr")





pos.words <- scan('positive-words-Harvard.txt', what='character')
neg.words <- scan('negative-words-Harvard.txt', what='character')


pos.words <- tolower(pos.words )
neg.words <- tolower(neg.words )


#CHECK THIS FILE TOMORROW!!!!

#reading name of all files
# allfiles <- grep("Tweets_Cleaned" ,list.files("/Users/narges/Dropbox/3-Research/Social media- finance/Analysis-R/Sentiment/Tweet-Sentiment-Data/Tweet-Text/") , value = T)


#https://jeffreybreen.wordpress.com/2011/07/04/twitter-text-mining-r-slides/
score.sentiment = function(sentences, pos.words, neg.words, .progress='none')
 {
     require(plyr)
     require(stringr)
     scores = laply(sentences, function(sentence, pos.words, neg.words) {
         sentence = gsub('[[:punct:]]', ' ', sentence)
         # sentence = tolower(sentence)
         word.list = str_split(sentence, '\\s+')
         words = unlist(word.list)
         pos.matches = match(words, pos.words)
         neg.matches = match(words, neg.words)
         pos.matches = !is.na(pos.matches)
         neg.matches = !is.na(neg.matches)
         score = sum(pos.matches) - sum(neg.matches)
         scorelist <- list("positive" = sum(pos.matches), "negative" = sum(neg.matches))
         return(scorelist)
     }, pos.words, neg.words, .progress=.progress )
     scores.df = data.frame(score=scores ,text=sentences)
      return(scores.df)
 }

# allfiles_filename <- paste0( "/Users/narges/Dropbox/3-Research/Social media- finance/Analysis-R/Sentiment/Tweet-Sentiment-Data/Tweet-Text/" ,allfiles[loopcnt] )

T <- read.csv( "testdata.csv" , header = TRUE ,sep=",", stringsAsFactors = FALSE)
Tweetset_Text <- T


T <- read.csv( "/Users/narges/Dropbox/SemEval2017/Mon-Jan16-FromBeg/nostemming/language dealing/startfromjson/Tweetlist_withNagation_noPunc.csv" , header = TRUE ,sep=",", stringsAsFactors = FALSE)


# test <- TRUE
loopcnt <- 1 
# final_score <- c(0)


test_score.names <- c( "score.positive" ,"score.negative", "text", , "label")
test_score <- sapply(test_score.names,function(x) NULL)



test_tweets = Tweetset_Text

res = score.sentiment(test_tweets[,1], pos.words, neg.words, .progress='text')
# res$label = test_tweets[,2]
# res$span = test_tweets[,3]
res$label = test_tweets[,2]
# res$cashtag = test_tweets[,3]
# res$actualSent = test_tweets[,6]



# for(i in 1:30){

#     Tweetset_Text.scores <- score.sentiment(Tweetset_Text[i,1], pos.words, neg.words, .progress='text')
#     # Tweetset_Text.scores
#     # colnames(test_score) <- colnames(Tweetset_Text.scores)
#     # Tweetset_Text.scores$label <- Tweetset_Text[i,2]
#     # Tweetset_Text.scores$actualSent <- Tweetset_Text[i,3]
#     # Tweetset_Text.scores$cashtag <- Tweetset_Text[i,4]
#     print(Tweetset_Text.scores)
#     # test_score <- rbind(test_score, Tweetset_Text.scores)
#     # Tweetset_Text.scores <- c(0)
# }

sapply(res, class)
sapply(res, class)
res.df = data.frame(res)
res.df$text <- unlist(res.df$text)
res.df$score.positive <- unlist(res.df$score.positive)
res.df$score.negative <- unlist(res.df$score.negative)

# Tweetset_Text.scores$score.positive <- unlist(Tweetset_Text.scores$score.positive)
# res.df$text <- as.list(res.df$text)

write.csv(res.df, file = "Train_withwordcount_Harvard.csv")

tweets<- read.csv("/Users/narges/Dropbox/SemEval2017/Random Forest/RF_output_lowe_alltweets.csv" , sep = ',')











