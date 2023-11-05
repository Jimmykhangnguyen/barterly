
# import libraries
import pandas as pd

"""Load the Dataset"""

path = "barterly-data"

# read in csv data
df_prods = pd.read_csv(path + "/products.csv", index_col=False)
df_trans = pd.read_csv(path + "/transactions.csv", index_col=False)

"""Calculate weighted rating average"""

# add new columns to df_prods dataframe
df_prods["rate_acc"] = len(df_prods)*[0]
df_prods["rate_count"] = len(df_prods)*[0]
df_prods["rate_avg"] = len(df_prods)*[0]

# fill rate_acc and rate_count columns by parsing through transactions
for i in range(len(df_trans)):
    item_ind = df_prods.index[df_prods['item']== df_trans['itemg'][i]].tolist()

    df_prods.loc[item_ind[0], 'rate_acc'] += df_trans['ratingg'][i]
    df_prods.loc[item_ind[0],'rate_count'] += 1

    item_ind = df_prods.index[df_prods['item']== df_trans['itemr'][i]].tolist()
    df_prods.loc[item_ind[0],'rate_acc'] += df_trans['ratingr'][i]
    df_prods.loc[item_ind[0],'rate_count'] += 1

# fill rate_avg
df_prods['rate_avg'] = df_prods['rate_acc'].divide(df_prods['rate_count'])

m = 1 # minimum rate count to be used
C = df_prods['rate_avg'].mean()
def weighted_rating(x, m=m, C=C):
    v = x['rate_count']
    R = x['rate_avg']
    return (v/(v+m) * R) + (m/(m+v) * C)

df_prods['score'] = df_prods.apply(weighted_rating, axis=1)

# rank df_prods based on score
df_prods = df_prods.sort_values('score', ascending=False)

# print the top 5 most highly rated items
df_prods[['item', 'rate_count', 'rate_avg', 'score']].head(5)