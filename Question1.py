import csv
from googleapiclient.discovery import build
from collections import Counter
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

# Set up the YouTube Data API client
api_key = "samplekey"  
youtube = build("youtube", "v3", developerKey=api_key)

# Function to extract comments from a video
def extract_comments(video_id):
    comments = []
    nextPageToken = None

    while True:
        # Request comments using the YouTube Data API
        response = youtube.commentThreads().list(
            part="snippet",
            videoId=video_id,
            pageToken=nextPageToken,
            maxResults=100
        ).execute()

        for item in response["items"]:
            comment = item["snippet"]["topLevelComment"]["snippet"]["textDisplay"]
            comments.append(comment)

        nextPageToken = response.get("nextPageToken")

        if not nextPageToken:
            break

    return comments

# Function to perform keyword extraction
def extract_keywords(text, num_keywords):
    stop_words = set(stopwords.words("english"))
    word_tokens = word_tokenize(text.lower())

    # Remove stop words and punctuation
    filtered_words = [word for word in word_tokens if word.isalnum() and word not in stop_words]

    # Count word frequencies
    word_freq = Counter(filtered_words)

    # Get the most common keywords
    keywords = [word for word, freq in word_freq.most_common(num_keywords)]

    return keywords


video_url = "https://www.youtube.com/watch?v=dQw4w9WgXcQ"  # Replace with the YouTube video URL
video_id = video_url.split("=")[-1]  # Extract the video ID from the URL

# Extract comments from the video
comments = extract_comments(video_id)

# Save comments to a CSV file
output_file = "comments.csv"
with open(output_file, "w", encoding="utf-8", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["Comment"])
    writer.writerows(zip(comments))

print(f"Comments extracted and saved to {output_file}.")

# Perform keyword extraction on the comments
all_comments_text = " ".join(comments)
num_keywords = 5  # Set the desired number of keywords to extract
keywords = extract_keywords(all_comments_text, num_keywords)

print("Most demanding topics in the comment section:")
for i, keyword in enumerate(keywords, 1):
    print(f"{i}. {keyword}")
