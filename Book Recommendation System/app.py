
import streamlit as st
import numpy as np
import pickle
from PIL import Image
tab1, tab2 = st.tabs(["Popular", "Book-Recommender"])
with tab1:
    
    image = Image.open("img1.jpg")
    new_image = image.resize((1000,250))
    st.image(new_image)
    
    
    st.header("Top 10 books")
    popular_df = pickle.load(open('popular.pkl', 'rb'))
    book_pivot= pickle.load(open('book_pivot.pkl', 'rb'))
    book_list = book_pivot.index.values
    image_url = popular_df['Image-URL-M'].tolist()
    book_title = popular_df['Book-Title'].tolist() 
    book_author = popular_df['Book-Author'].tolist()
    total_ratings = popular_df['Book-Rating'].tolist()
    avg_ratings = popular_df['avg_rating'].tolist()
    
    col1,col2,col3,col4,col5=st.columns(5)
    with col1:
        st.image(image_url[0])
        st.text(book_author[0])
        st.text("Ratings:" + str(total_ratings[0]))
        st.text("Avg.Rating:" + str(round(avg_ratings[0],2)))
    with col2:
        st.image(image_url[1])
        st.text(book_author[1])
        st.text("Ratings:" + str(total_ratings[1]))
        st.text("Avg.Rating:" + str(round(avg_ratings[1],2)))
    with col3:
        st.image(image_url[2])
        st.text(book_author[2])
        st.text("Ratings:" + str(total_ratings[2]))
        st.text("Avg.Rating:" + str(round(avg_ratings[2],2)))
    with col4:
        st.image(image_url[3])
        st.text(book_author[3])
        st.text("Ratings:" + str(total_ratings[3]))
        st.text("Avg.Rating:" + str(round(avg_ratings[3],2)))
    with col5:
        st.image(image_url[4])
        st.text(book_author[4])
        st.text("Ratings:" + str(total_ratings[4]))
        st.text("Avg.Rating:" + str(round(avg_ratings[4],2)))
    
    col1,col2,col3,col4,col5=st.columns(5) 
    with col1:
        st.image(image_url[5])
        st.text(book_author[5])
        st.text("Ratings:" + str(total_ratings[5]))
        st.text("Avg.Rating:" + str(round(avg_ratings[5],2)))
    with col2:
        st.image(image_url[6])
        st.text(book_author[6])
        st.text("Ratings:" + str(total_ratings[6]))
        st.text("Avg.Rating:" + str(round(avg_ratings[6],2)))
    with col3:
        st.image(image_url[7])
        st.text(book_author[7])
        st.text("Ratings:" + str(total_ratings[7]))
        st.text("Avg.Rating:" + str(round(avg_ratings[7],2)))
    with col4:
        st.image(image_url[8])
        st.text(book_author[8])
        st.text("Ratings:" + str(total_ratings[8]))
        st.text("Avg.Rating:" + str(round(avg_ratings[8],2)))
    with col5:
        st.image(image_url[9])
        st.text(book_author[9])
        st.text("Ratings:" + str(total_ratings[9]))
        st.text("Avg.Rating:" + str(round(avg_ratings[9],2)))

with tab2:
    image2 = Image.open("img2.jpg")
    new_image2 = image2.resize((1000,250))
    st.image(new_image2)
    st.header('Book Recommender System')
    
    
    similarity = pickle.load(open('similarity.pkl', 'rb'))
    book_pivot= pickle.load(open('book_pivot.pkl', 'rb'))
    books = pickle.load(open('books.pkl', 'rb'))
    book_names = pickle.load(open('book_names.pkl','rb'))

    def fetch_poster(suggestion):
        book_name = []
        ids_index = []
        poster_url = []

        for book_id in suggestion:
            book_name.append(book_pivot.index[book_id])

        for name in book_name: 
            ids = np.where(books['Book-Title'] == name)[0][0]
            ids_index.append(ids)

        for idx in ids_index:
            url = books.iloc[idx]['Image-URL-L']
            poster_url.append(url)

        return poster_url



    def recommend_book(book_name):
        books_list = []
        book_id = np.where(book_pivot.index == book_name)[0][0]
        similar_items=sorted(list(enumerate(similarity[book_id])),key=lambda x:x[1],reverse=True)[1:7]
        suggestion=[]
        for i in similar_items:
            suggestion.append(i[0])



        poster_url = fetch_poster(suggestion)

        for i in similar_items:
            books_list.append(book_pivot.index[i[0]])
        return books_list , poster_url       



    selected_books = st.selectbox(
        "Type or select a book from the dropdown",
        book_names
    )

    if st.button('Show Recommendation'):
        recommended_books,poster_url = recommend_book(selected_books)

        col1, col2,col3 = st.columns(3)

        with col1:
            st.text(recommended_books[0])
            st.image(poster_url[0])
        with col2:
            st.text(recommended_books[1])
            st.image(poster_url[1])
        with col3:
            st.text(recommended_books[2])
            st.image(poster_url[2])

        col4, col5,col6= st.columns(3)

        with col4:
            st.text(recommended_books[3])
            st.image(poster_url[3])

        with col5:
            st.text(recommended_books[4])
            st.image(poster_url[4])
        with col6:
            st.text(recommended_books[5])
            st.image(poster_url[5])
