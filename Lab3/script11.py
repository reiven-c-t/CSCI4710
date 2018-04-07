# Question11
import pandas as pd
import matplotlib.pyplot as plt

df_pieces = []
path = "names/"

years = range(2013, 2017)
for year in years:
    df_year = pd.read_csv(path + "yob" + str(year) + ".txt", names=["name", "sex", "births"])
    df_year["year"] = year
    df_pieces.append(df_year)

names = pd.concat(df_pieces, ignore_index=True)

# output a few lines of one of the data frames
print(df_year.head())


# sum births by gender
print(names.groupby("sex")["births"].sum())

print(type(names))
print(names.index)
n = names.groupby("name")["births"].sum()
print(type(n))
#note a hierarchical index was created
print(n.index)
n1 = n.reset_index(name="birthcount")

# top 10 birth names
top10 = n1.sort_values(by='birthcount', ascending=False)[:10]
# select the name column converts the dataframe to a series
# which can be converted to a list
print(top10['name'])
print(type(top10['name']))
l_top10 = top10['name'].tolist()
print(l_top10)

# select the births for names in the top 10 list
df_top10 = names[names['name'].isin(l_top10)]
# select name and birth count columns
df_top10births = df_top10[['name','births']]
# sum births for each name
df_top10sum = df_top10.groupby('name')['births'].sum()
df_top10sum = df_top10sum.reset_index(name='births')

# create bar chart
plt.style.use('ggplot')
df_top10sum.plot(kind="bar",x=df_top10sum["name"],
                              title="Birth Names",
                              legend=False)
plt.gcf().subplots_adjust(bottom=0.2)
plt.show()