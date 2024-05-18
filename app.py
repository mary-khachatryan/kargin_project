import pandas as pd
import streamlit as st
import plotly.express as px
df = pd.read_csv('data_csv.csv')
for i in df.columns:
    if 'Unnamed:' in i:
        print(i)
        df.pop(i)

# f = df.rename(columns={"Կարգին մարդ ": "writer",'Շատ տարածված արտահայտություն' : "common_phrase",'Տեքստ': 'Text',
#                        'Հիմնական դերասաններ':"Main_Actors", 'հիմնական դերասանների քանակ': "Main_actors_count",
#                        'Դերերի անուններ' : 'Role_names', 'Վայր' :'Place', 'Լուսավորվածություն': 'Lighting','Լեզուներ':"lang"
#  })
# f.to_csv("data_csv.csv") 




new_df = df.fillna(value = "None")
all_names = []
for i in new_df["Main_Actors"]:
    for j in i.split(','):
        
        name = j.strip()
        if " " in name:
          lst = name.split(' ')
          for k in lst:
              all_names.append(k.strip(" "))
        else:
            all_names.append(name)

unique_names = []
unique_names_count ={}
for i in all_names:
    if i not in unique_names:
        unique_names.append(i)
        unique_names_count[i] = all_names.count(i)
        

df_unique_names = pd.DataFrame(list(unique_names_count.items()), columns=['Name', 'Count'])
df_unique_names = df_unique_names.sort_values(by = "Count",axis=0,ascending=False).head(20)
print(df_unique_names,type(df_unique_names))
fig = px.bar(df_unique_names, x='Name', y='Count', title='Count of Unique Names Top 20')
st.plotly_chart(fig)
