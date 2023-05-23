import csv
from collections import Counter
import PyPDF2

# Function to extract text from a PDF file
def extract_text_from_pdf(file_path):
    text = ""
    with open(file_path, "rb") as file:
        reader = PyPDF2.PdfFileReader(file)
        num_pages = reader.numPages

        for page in range(num_pages):
            page_obj = reader.getPage(page)
            text += page_obj.extractText()

    return text


pdf_file = "pdf_file.pdf"  

# Extract text from the PDF
text = extract_text_from_pdf(pdf_file)

# Save text to a CSV file
output_file = "pdf_text.csv"
with open(output_file, "w", encoding="utf-8", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["Text"])
    writer.writerow([text])

print(f"Text extracted and saved to {output_file}.")

# Find the most repeated word in the PDF
words = text.split()
word_freq = Counter(words)
most_common_word = word_freq.most_common(1)[0][0]

print(f"The most repeated word in the PDF is: {most_common_word}")

