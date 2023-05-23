import csv
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from gensim import corpora
from gensim.models import LdaModel

# Load NLTK stop words
nltk.download('stopwords')
stop_words = set(stopwords.words('english'))

# Function to perform keyword extraction and topic modeling
def perform_topic_modeling(text, num_topics, num_keywords):
    word_tokens = word_tokenize(text.lower())

    # Remove stop words and punctuation
    filtered_words = [word for word in word_tokens if word.isalnum() and word not in stop_words]

    # Create dictionary and corpus for topic modeling
    dictionary = corpora.Dictionary([filtered_words])
    corpus = [dictionary.doc2bow(filtered_words)]

    # Perform topic modeling using LDA
    lda_model = LdaModel(corpus, num_topics=num_topics, id2word=dictionary)

    # Get the top keywords for each topic
    topics_keywords = lda_model.show_topics(num_topics=num_topics, num_words=num_keywords)

    return topics_keywords

csv_file = "pdf_text.csv" 

# Read text from the CSV file
with open(csv_file, "r", encoding="utf-8") as file:
    reader = csv.reader(file)
    next(reader)  # Skip the header row
    text = next(reader)[0]  # Assuming the text is in the first column

# Perform topic modeling on the text
num_topics = 3  # Set the desired number of topics
num_keywords = 5  # Set the desired number of keywords per topic
topics_keywords = perform_topic_modeling(text, num_topics, num_keywords)

print("Topic modeling results:")
for topic, keywords in topics_keywords:
    print(f"Topic {topic + 1}:")
    print(keywords)
    print()
