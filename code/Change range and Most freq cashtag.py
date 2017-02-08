

jsondataT <- fromJSON(file = "/Users/narges/Dropbox/FinalSemEval/Microblogs_Trainingdata_withmessages.json", method = "C")

# jsondataT <- fromJSON(file = "/Users/narges/Dropbox/SemEval2017/Mon-Jan16-FromBeg/SemEval_TestData.json", method = "C")

jsonfile <- jsondataT

jsonfile <- lapply(jsonfile, function(x) {
  x[sapply(x, is.null)] <- NA
  unlist(x)
})

jsonfile.df  <- do.call("rbind", jsonfile)


 Mechtweets<- read.csv("/Users/narges/Dropbox/SemEval2017/Mon-Jan16-FromBeg/Mechanical_Turk.csv" , header = FALSE ,sep = ',', stringsAsFactors = FALSE)

#------- set the sentiments to 0 and 0ne 



Test <- cbind( jsonfile.df[,3:6])
Test <- Mechtweets

for(i in 1:nrow(Test)){
	if(Test[i,1] >= '0.1') 
		Test[i,5] <- 1
	else if(as.numeric(Test[i,1]) < -0.1 ) 
		Test[i,5] <- -1
	else 
		Test[i,5] <- 0
}


#convert to lower:

for(i in 1:nrow(Test)){
	Test[i,3] <- tolower(Test[i,3])
}

for(i in 1:nrow(Test)){
	Test[i,4] <- tolower(Test[i,4])
}



nonzero <- [0]
for(i in 1:nrow(Test)){
	if(Test[i,3] == 0){
		next
	}
	nonzero[i] <- Test[i,]
}

write.csv(Test, file = 'Train_twoSpan_semEval_tolower.csv')


#most popular cashtags in the training dataset 

cashtag <- count(jsonfile.df[,2])
ordertag<- cashtag[ order(-cashtag$freq), ]

topfreq <- head(ordercomp, 20)


strain_top_freq_Tw <- lapply(topfreq$x, function(a) subset(Strain,grepl(as.character(a), V6, ignore.case = TRUE)))


strain_top_freq <- do.call(rbind, strain_top_freq)
