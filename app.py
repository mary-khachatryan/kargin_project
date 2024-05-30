import pandas as pd
import streamlit as st
import plotly.express as px
from pytube import YouTube
import matplotlib.pyplot as plt



def video_info(video_url):
    video = YouTube(video_url)
    likes_count = (video.initial_data["contents"]["twoColumnWatchNextResults"]["results"]["results"]["contents"][0]["videoPrimaryInfoRenderer"]["videoActions"]["menuRenderer"]["topLevelButtons"][0]["segmentedLikeDislikeButtonViewModel"]["likeButtonViewModel"]["likeButtonViewModel"]["toggleButtonViewModel"]["toggleButtonViewModel"]["defaultButtonViewModel"]["buttonViewModel"]["accessibilityText"]).split()[5]
    views_count = video.views
    name_video  = video.title
    likes = int(likes_count.replace(",", ''))
    print(likes)
    lpv_persent = ((likes) * 100 / views_count)
   
    
    labels = 'views without likes', 'likes'
    sizes = [100-lpv_persent, lpv_persent]
    explode = (0, 0.1) 
   
    fig1, ax1 = plt.subplots(figsize=(2, 1))
    wedges,text, autotexts = ax1.pie(sizes, explode=explode,
        shadow=False, autopct='%1.1f%%', startangle=40)
    ax1.axis('equal') 
    ax1.legend(wedges,labels, loc="center left", bbox_to_anchor=(1, 0, 0.5, 0.5))

    plt.setp(autotexts, size=4, weight="bold")
    
    ax1.set_title(name_video,size = 5)

    st.pyplot(fig1,clear_figure=False, use_container_width=False)
    




df = pd.read_csv('data_csv.csv')

for i in df.columns:
    if 'Unnamed:' in i:
        print(i)
        df.pop(i)

url = "https://www.youtube.com/watch?v=VJDJs9dumZI"
print(YouTube(url))
# f = df.rename(columns={"Կարգին մարդ ": "writer",'Շատ տարածված արտահայտություն' : "common_phrase",'Տեքստ': 'Text',
#                        'Հիմնական դերասաններ':"Main_Actors", 'հիմնական դերասանների քանակ': "Main_actors_count",
#                        'Դերերի անուններ' : 'Role_names', 'Վայր' :'Place', 'Լուսավորվածություն': 'Lighting','Լեզուներ':"lang"
#  })
# f.to_csv("data_csv.csv") 
new_df = df.fillna(value = "None")

def statistic(column_name):
    listof_data = []
    for i in new_df[column_name]:
        for j in i.split(','):
            name = j.strip()
            if " " in name:
                lst = name.split(' ')
                for k in lst:
                    listof_data.append(k.strip(" "))
            else:
                listof_data.append(name)
    unique_names = []
    unique_names_count ={}
    for i in listof_data:
        if i not in unique_names:
            unique_names.append(i)
            unique_names_count[i] = listof_data.count(i)
        

    df_unique_names = pd.DataFrame(list(unique_names_count.items()), columns=['Name', 'Count'])
    df_unique_names = df_unique_names.sort_values(by = "Count",axis=0,ascending=False).head(20)
    # print(df_unique_names,type(df_unique_names))
    fig = px.bar(df_unique_names, x='Name', y='Count', title=f'Count of Unique {column_name} Top 20')
    st.plotly_chart(fig)


st.write("YouTube Video Like Percentage Visualizer")
video1 = st.text_input("Yutube link")
if st.button("Next"):
    video_info(video1)
    


statistic("Main_Actors")
statistic("Place")
statistic("Role_names")



