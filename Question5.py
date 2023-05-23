import fasttext

# Train the FastText language detection model
def train_language_detection_model(input_file, model_file):
    model = fasttext.train_supervised(input=input_file, lr=1.0, epoch=25, wordNgrams=2, bucket=200000, dim=50, loss='hs')
    model.save_model(model_file)

# Evaluate the language detection model
def evaluate_language_detection_model(model_file, eval_file):
    model = fasttext.load_model(model_file)
    result = model.test(eval_file)
    print("Precision:", result.precision)
    print("Recall:", result.recall)
    print("Number of examples:", result.nexamples)

# Predict the language of a text
def predict_language(text, model_file):
    model = fasttext.load_model(model_file)
    predicted_label, _ = model.predict(text)
    predicted_language = predicted_label[0]
    return predicted_language

# Train the model
input_file = "train.txt"  
model_file = "language_detection.bin"
train_language_detection_model(input_file, model_file)

# Evaluate the model
eval_file = "eval.txt"  
evaluate_language_detection_model(model_file, eval_file)

# Predict the language of a text
text = "This is an example sentence."
predicted_language = predict_language(text, model_file)
print("Predicted language:", predicted_language)
