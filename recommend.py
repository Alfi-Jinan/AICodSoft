import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import linear_kernel

data = {
    'title': ['The Shawshank Redemption', 'The Godfather', 'The Dark Knight', 'Pulp Fiction', 'Fight Club'],
    'genre': ['Drama', 'Crime, Drama', 'Action, Crime, Drama', 'Crime, Drama', 'Drama'],
    'description': ['Two imprisoned men bond over a number of years, finding solace and eventual redemption through acts of common decency.',
                    'The aging patriarch of an organized crime dynasty transfers control of his clandestine empire to his reluctant son.',
                    'When the menace known as The Joker emerges from his mysterious past, he wreaks havoc and chaos on the people of Gotham.',
                    'The lives of two mob hitmen, a boxer, a gangster and his wife, and a pair of diner bandits intertwine in four tales of violence and redemption.',
                    'An insomniac office worker and a devil-may-care soap maker form an underground fight club that evolves into much more.']
}

movies_df = pd.DataFrame(data)

tfidf_vectorizer = TfidfVectorizer(stop_words='english')
tfidf_matrix = tfidf_vectorizer.fit_transform(movies_df['genre'])

cosine_sim = linear_kernel(tfidf_matrix, tfidf_matrix)

def recommend_movies(user_profile, cosine_sim, movies_df):
    user_profile_vector = tfidf_vectorizer.transform([user_profile])
    sim_scores = linear_kernel(user_profile_vector, tfidf_matrix).flatten()

    sim_indices = sim_scores.argsort()[::-1]

    recommended_movies = []
    for idx in sim_indices[1:6]:  
        recommended_movies.append(movies_df['title'][idx])

    return recommended_movies

if __name__ == "__main__":
    user_profile = 'Drama'  
    recommendations = recommend_movies(user_profile, cosine_sim, movies_df)
    print("Recommended Movies based on User's Preference:")
    for movie in recommendations:
        print("-", movie)
