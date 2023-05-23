import os
import whisper
from gtts import gTTS




# Transcribe audio file using Whisper
def transcribe_audio(audio_file):
    model = whisper.load_model("english")
    result = model.transcribe(audio_file)
    return result["text"]

# Convert text to audio in a different language using gTTS
def convert_text_to_audio(text, language, output_file):
    tts = gTTS(text=text, lang=language)
    tts.save(output_file)

# Set the input audio file path
audio_file = "audio_file.wav"

# Transcribe the audio file
transcription = transcribe_audio(audio_file)

# Set the desired language for audio conversion (e.g., "fr" for French)
desired_language = "fr"

# Convert the transcribed text to audio in the desired language
output_file = "output_audio.mp3"
convert_text_to_audio(transcription, desired_language, output_file)

print("Audio conversion complete!")
