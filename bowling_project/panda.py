import pandas as pd

df = pd.read_excel('bowlingtest.xlsx', sheet_name="Sheet1", usecols='A:E')
#print(df.head(1))
#print("Start of index print")
firstDate = df['Dates'].iloc[0].strftime('%Y-%m-%d')

#print(df['Dates'].head(1))

average_scores_by_date = round(df.groupby('Dates').mean())
#print("Start of average scores by date")
print(average_scores_by_date)
print("-------------------------")
dad_averages  = average_scores_by_date['Dad']
print(dad_averages)
print("-------------------------")

firstDate = df['Dates'].iloc[0].strftime('%Y-%m-%d')  # Ensuring firstDate is a string for comparison

lastDate = None
all_scores = []
total_averages = []
for index, row in df.iterrows():
    currentDate = row['Dates'].strftime('%Y-%m-%d')
    scoreOnCurrentDate = row['Dad']
    if(lastDate == None):
        all_scores.append(scoreOnCurrentDate)
        lastDate = currentDate
    elif(currentDate == lastDate):
        all_scores.append(scoreOnCurrentDate)
    else:
        tempAverage = round(sum(all_scores)/len(all_scores))
        total_averages.append(tempAverage)
        lastDate = currentDate
        all_scores.append(scoreOnCurrentDate)
print(all_scores)
print(total_averages)




'''
total_Average = []
count_dates = 0
lastDate = None

for index, row in df.iterrows():
    # Format the date
    currentDate = row['Dates'].strftime('%Y-%m-%d')
    averageOnCurrentDate = average_scores_by_date.loc[currentDate, 'Dad']
    print("AVERAGE ON CURRENT DATE", averageOnCurrentDate)
    print(total_Average)

    #check to make sure current date is not the same date as the row before
    if(currentDate != lastDate):
        if(currentDate == firstDate):
            total_Average.append(averageOnCurrentDate)
            lastDate = currentDate
        else:
            total_Average.append(averageOnCurrentDate)
            tempAverage = round(sum(total_Average)/len(total_Average))
            total_Average[-1] = tempAverage
            averageOnCurrentDate = tempAverage
            lastDate = currentDate

    # Directly use the 'Dad' score from the current row
    scoreOnCurrentDate = row['Dad']
    currentHandicap = round((200 - averageOnCurrentDate) * 0.8)
    
    print(f"SCORE: {scoreOnCurrentDate}, AVERAGE ON DATE: {round(averageOnCurrentDate)}, HANDICAP: {currentHandicap}")
    
    

   
 '''