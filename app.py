import pandas as pd
import streamlit as st
from itertools import chain
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
print(all_names,type(all_names[0]))

unique_names = []

