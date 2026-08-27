import pandas as pd
from sklearn.cluster import KMeans
import plotly.graph_objects as go

df = pd.read_csv("all_countries.csv")

#first country
target = df["countryISO3"].iloc[0]

subcats = []
for country, subcat in zip(df["countryISO3"], df["Subcategory"]):
    if country != target:
        break
    else:
        subcats.append(subcat)

country_hours_map = {}
hour_list = []

for row_index, (country, hours) in enumerate(zip(df["countryISO3"], df["hoursPerDayCombined"])):
    if country == target:
        hour_list.append(hours)
    if  row_index == len(df)-1 or df["countryISO3"].iloc[row_index+1] != target:
        country_hours_map[country] = hour_list
        hour_list = []
        target = df["countryISO3"].iloc[row_index]
        hour_list.append(hours)

# country_hours_map is 
    # key: "country name"
    # value: list of hours for that country

df = pd.DataFrame.from_dict(country_hours_map, orient = "index", columns = subcats)
df.index.name = "Country"
# df.to_csv("output.csv")

# #calculate the best k ---------------------------------------------------------------------

subcat_frame = df[subcats]
# inertias = []
# ks = range(2,50)
# for k in ks:
#     km = KMeans(n_clusters = k, n_init = 'auto', random_state = 2028)
#     km.fit(subcat_frame)
#     inertias.append(km.inertia_)

# fig = go.Figure()
# fig.add_trace(go.Scatter(x=list(ks), y=inertias))
# fig.show()
#--------------------------------------------------------------------------------------------

#do kmeans
k = 7
km = KMeans(n_clusters=k, n_init=100, random_state = 2028)
km.fit(subcat_frame)

clustersize = []
for cluster in range(k):
    clustersize.append(int(sum(km.labels_==cluster)))
print(clustersize)