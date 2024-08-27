import pandas as pd

#Background: This is a quick code that i used to combine data and give my marketing manager a insights on the performance of different menu.nepvent clients
#Problem : I have Multiple CSV files extracted from differnt source. Monhtly, Yearly and Weekly all extracted form google analytics insights that contains
# Weekly , Monthly and Weekly Views along with another sheet containing data on when the menu was created. The createdAt column identifies the data
#I want all the data in a single sheet to help with insisghnt Better


#This is a simple function that extracts actual restaurant names from the link
# input Nepvent | Bricks Cafe Menu give Bricks Cafe, This is done to ensure both all my dataset have same restaurant name
def changePageTitle(x):
    return x[x.find('|')+1:x.find('Menu')-1].strip()

#Choosing the columns that i need for my analysis
columnsToSelect = ['Page title and screen class','Views','Users']

#Loading CSV
dataYearly = pd.read_csv('Yearly.csv')
#Creating columnsnames to replace the existing column names
columnsToReplace = ['Restaurant Name','Yearly Views','Yearly Users']
dataYearly = dataYearly[columnsToSelect]
dataYearly.columns = columnsToReplace
#Chaning the name by using apply
dataYearly['Restaurant Name'] = dataYearly['Restaurant Name'].apply(changePageTitle)


print("Data Monthly----------")
#Doing Same for Monthly
dataMonthly = pd.read_csv('Monthly.csv')
columnsToReplace = ['Restaurant Name','Monthly Views','Monthly Users']
dataMonthly = dataMonthly[columnsToSelect]
dataMonthly.columns = columnsToReplace
dataMonthly['Restaurant Name'] = dataMonthly['Restaurant Name'].apply(changePageTitle)


print("Data Weekly----------")
#Doing Same for Weekly
dataWeekly = pd.read_csv('Weekly.csv')
columnsToReplace = ['Restaurant Name','Weekly Views','Weekly Users']
dataWeekly = dataWeekly[columnsToSelect]
dataWeekly.columns = columnsToReplace
dataWeekly['Restaurant Name'] = dataWeekly['Restaurant Name'].apply(changePageTitle)


#Mering the first two data set on  Restuarnt Name, We've made sure that restaurant names are unique
# Outer join preserves column from both datasets
merge1 = pd.merge(dataWeekly,dataMonthly,on='Restaurant Name',how='outer')
merge2 = pd.merge(merge1,dataYearly,on='Restaurant Name',how='outer')
print(merge2.head().to_string())


print("Nepvent Menu Data===")
#Loading the next data
menuNepventData = pd.read_csv('MenuNepventData.csv')
menuNepventData['Restaurant Name'] = menuNepventData['name']
menuNepventData.drop(columns=['name','Unnamed: 0'],inplace=True)

print(menuNepventData.head().to_string())
#Exporting the final data
finalDataToExport = pd.merge(merge2,menuNepventData,on='Restaurant Name',how='outer')
finalDataToExport.to_csv('FinalDataNepventView.csv')
