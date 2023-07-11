
import pandas as pd
data =pd.read_csv('2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv')

grey_c=len(data[data["Primary Fur Color"]=='Gray'])
red_c=len(data[data["Primary Fur Color"]=='Cinnamon'])
black_c=len(data[data["Primary Fur Color"]=='Black'])

data_dict={
    "Fur Color":['Gray','Cinnamon','Black'],
    "Count":[grey_c,red_c,black_c]
}

df=pd.DataFrame(data_dict)
df.to_csv('squirrel_count.csv')
print(df)

