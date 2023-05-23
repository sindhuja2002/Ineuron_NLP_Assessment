import nltk
from nltk.corpus import stopwords
from nltk.tokenize import sent_tokenize, word_tokenize
from string import punctuation
from heapq import nlargest

# Load NLTK stop words
nltk.download('stopwords')
stop_words = set(stopwords.words('english'))

def summarize_text(text, num_sentences):
    # Tokenize text into sentences
    sentences = sent_tokenize(text)

    # Tokenize text into words
    words = word_tokenize(text.lower())

    # Remove stopwords and punctuation
    words = [word for word in words if word not in stop_words and word not in punctuation]

    # Calculate word frequencies
    word_freq = nltk.FreqDist(words)

    # Calculate sentence scores based on word frequencies
    sentence_scores = {}
    for i, sentence in enumerate(sentences):
        for word in word_tokenize(sentence.lower()):
            if word in word_freq:
                if i in sentence_scores:
                    sentence_scores[i] += word_freq[word]
                else:
                    sentence_scores[i] = word_freq[word]

    # Select the top-ranked sentences for the summary
    summary_sentences = nlargest(num_sentences, sentence_scores, key=sentence_scores.get)
    summary = ' '.join([sentences[i] for i in sorted(summary_sentences)])

    return summary


text_file = "sample_file.txt"  
num_sentences = 3  # Set the desired number of sentences for the summary

# Read text from the file
with open(text_file, "r", encoding="utf-8") as file:
    text = file.read()

# Perform text summarization
summary = summarize_text(text, num_sentences)

print("Text Summary:")
print(summary)
