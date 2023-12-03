import streamlit as st
import pickle
import pandas as pd

def recommend(movie):
    movie_index = movies_list[movies_list['title'] == movie].index[0]
    distances = similarity[movie_index]
    movie_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:10]

    recommend_movies = []
    for i in movie_list:
        recommend_movies.append(movies_list.iloc[i[0]].title)
    return recommend_movies


movies_list=pickle.load(open('recommend.pkl','rb'))
movies_list = pd.DataFrame(movies_list)

similarity=pickle.load(open('similarity.pkl','rb'))
st.title('Content Based Recommendation')

user_movie = st.selectbox('what would like to watch?',movies_list['title'].values)
# if user_movie in movies_list:

if st.button('click me to select your next movie'):
    recommendation = recommend(user_movie)
    for i in recommendation:
        st.write(i)
# else:
#     st.write(f"Movie '{user_movie}' not found in the dataset.")