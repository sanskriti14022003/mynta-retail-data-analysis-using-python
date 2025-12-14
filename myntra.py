import pandas as pd
df=pd.read_csv('Myntra Fasion Clothing.csv')
df
df=pd.read_csv('Myntra Fasion Clothing.csv')
df.head(10)
df=pd.read_csv('Myntra Fasion Clothing.csv')
df.tail(5)
df.describe()
df.dtypes
##handling missing values
df.isnull().any()
df_filled=df.fillna(0)
df_filled
##filling the missing values with the mean of the column
df['Product_id_fillNA']=df['Product_id'].fillna(df['Product_id'].mean())
df
df.dtypes
df=df.rename(columns={'URL':'LINK'})
df.head()
df['New DiscountOffer']=df['DiscountOffer'].apply(lambda x:x*2)
df.head()
##data aggression and grouping
df.head()
grouped_mean=df.groupby('DiscountPrice (in Rs)')['Ratings'].mean()
print(grouped_mean)
grouped_sum=df.groupby(['OriginalPrice (in Rs)','Ratings'])['DiscountPrice (in Rs)'].sum()
print(grouped_sum)
df.groupby(['OriginalPrice (in Rs)','DiscountPrice (in Rs)'])['Ratings'].mean()
grouped_agg=df.groupby('OriginalPrice (in Rs)')['DiscountPrice (in Rs)'].agg(['mean','sum','count'])
grouped_agg
df1=pd.DataFrame({'Key':['A','B','C'],'Value1':[1,2,3]})
df2=pd.DataFrame({'Key':['A','B','F'],'Value2':[4,5,6]})
df
df1
df2
pd.merge(df1,df2,on="Key",how="outer")
pd.merge(df1,df2,on="Key",how="inner")
pd.merge(df1,df2,on="Key",how="left")
pd.merge(df1,df2,on="Key",how="right")
import matplotlib.pyplot as plt
df=pd.read_csv('Myntra Fasion Clothing.csv')
x=df['Ratings']
y=df['Reviews']

plt.plot(x,y)
plt.xlabel('x axis')
plt.ylabel('y Axis')
plt.title("Basic line plot")
plt.show()