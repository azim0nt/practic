from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

descriptions = [
"green 2",
"Test product green",
"A digital scale with body composition analysis, Bluetooth sync, and a sleek glass design."
]

vectorizer = TfidfVectorizer()
tfidf_matrix = vectorizer.fit_transform(descriptions)

similarity = cosine_similarity(tfidf_matrix)
print(similarity)
