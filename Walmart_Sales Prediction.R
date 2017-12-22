library(dplyr)
library(ggplot2)
library(reshape2)
library(readr)
library(lubridate)
library(rpart)
library(rattle)
library(car)
library(caret)
library(corrplot)
library(rpart.plot)

train<- read_csv("C:/Users/Saikrishna Nellutla/Downloads/train.csv/train.csv")
stores <- read_csv("C:/Users/Saikrishna Nellutla/Downloads/stores.csv")
features <- read_csv("C:/Users/Saikrishna Nellutla/Downloads/features.csv/features.csv")

options(max.print = 10000000)
stores$Store <- factor(stores$Store)
train$Store <- factor(train$Store)
train <- full_join(train,stores,by=c("Store"))
summary(train)

train$week=lubridate::week(mdy(train$Date))
train$Returns <- lapply(train$Weekly_Sales,function(sales){
  ifelse(sales < 0,sales,0)
})
train$Weekly_Sales <- lapply(train$Weekly_Sales,function(sales){
  ifelse(sales > 0,sales,0)
})


train=data.frame(train)
my.df <- data.frame(lapply(train, as.character), stringsAsFactors=FALSE)
write.csv(my.df, file="C:/Users/Saikrishna Nellutla/Desktop/train.csv", row.names = TRUE)

train$Weekly_Sales=as.numeric(train$Weekly_Sales)
sum(train$Weekly_Sales)
final_data <- data.frame(Store=factor(),Date=as.Date(character()),Weekly_Sales=numeric(),IsHoliday=logical(),Type=factor(),month=factor())
sum(train$Weekly_Sales)
train$Returns=as.numeric(train$Returns)
final_data=data.frame(train)

if(final_data$Dept==train$Dept){
  final_data$Weekly_Sales=
}

features$Store <- factor(features$Store)
#Merge our final_data with our features
features$IsHoliday=as.logical(features$IsHoliday)
final_data <- left_join(final_data,features,by=c("Store","Date","IsHoliday"))

final_data$MarkDown1 <- sapply(final_data$MarkDown1, function(value){
  ifelse(is.na(value),0,value)
})
final_data$MarkDown2 <- sapply(final_data$MarkDown2, function(value){
  ifelse(is.na(value),0,value)
})
final_data$MarkDown3 <- sapply(final_data$MarkDown3, function(value){
  ifelse(is.na(value),0,value)
})
final_data$MarkDown4 <- sapply(final_data$MarkDown4, function(value){
  ifelse(is.na(value),0,value)
})
final_data$MarkDown5 <- sapply(final_data$MarkDown5, function(value){
  ifelse(is.na(value),0,value)
})


set.seed(12345)
row<-nrow(final_data)
trainindex <- sample(row, 0.6*row, replace=FALSE)
training <- final_data[trainindex,]
validation <- final_data[-trainindex,]

mydata.rpart <-rpart(Type~Store+,data=training, control=rpart.control(minsplit=1,cp=0.05))
summary(train.rpart)

prediction <- predict(mydata.rpart,validation, type="class")
validation$Prediction <- prediction
#Find the percentage accuracy of our model
accur_table <- validation %>% select(Type,Prediction) 
bool_vector <- accur_table$Type == accur_table$Prediction
length(which(bool_vector)) / length(bool_vector)