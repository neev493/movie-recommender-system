import streamlit as st
import pickle
import pandas as pd
import requests

def fetch_poster(movie_id):
    url = "https://api.themoviedb.org/3/movie/{}?language=en-US".format(movie_id)
    headers = {
        "accept": "application/json",
        "Authorization": "Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiI3ZGJlZGQ4ZDhhMzZlYzcxMzViYTgwYTg0MTRhMmYxNyIsIm5iZiI6MTcyNjg1Mzg0NC4xNjAwOTksInN1YiI6IjY2ZWRiMDQ2NmQwY2QyNjQ4M2ZlMWU3ZiIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.ythMfLX_JwcbmutdZTSbqxbAklCoU-QHUcExyTUhbfg"
    }
    response = requests.get(url, headers=headers)
    data = response.json()
    return "https://image.tmdb.org/t/p/w500/" + data['poster_path']

def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distances = similarity[movie_index]
    movies_list = sorted(list(enumerate (distances)), reverse=True, key=lambda x:x[1])[1:6]
    recommended_movies = []
    recommended_movies_poster = []
    for i in movies_list:
        movie_id = movies.iloc[i[0]].movie_id
        recommended_movies.append(movies.iloc[i[0]].title)
        # fetch poster from an api
        recommended_movies_poster.append(fetch_poster(movie_id))
    return recommended_movies, recommended_movies_poster

movies_dict = pickle.load(open('movie_dict.pkl','rb'))
movies = pd.DataFrame(movies_dict)

similarity = pickle.load(open('similarity.pkl','rb'))

# A dataframe was created here as not necessarily in every system the direct pandas might work. In my system
# it worked but that does not mean it will work for all so dumping the values through "pickle.dump(new_df.to_dict(), open('movie_dict.pkl','wb'))"
# and then making it in dataframe through the above line of code. Then we can access it through "movies['title'].values"

st.title('Movie Recommender System')

selected_movie_name = st.selectbox(
"How would you like to be contacted?",
movies['title'].values,
)
if st.button("Recommend"):
    names, posters = recommend(selected_movie_name)
    col1, col2, col3, col4, col5 = st.columns(5)
    with col1:
        st.text(names[0])
        st.image(posters[0])
    with col2:
        st.text(names[1])
        st.image(posters[1])
    with col3:
        st.text(names[2])
        st.image(posters[2])
    with col4:
        st.text(names[3])
        st.image(posters[3])
    with col5:
        st.text(names[4])
        st.image(posters[4])