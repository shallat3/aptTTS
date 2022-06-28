from msilib.schema import File
from flask import Flask, render_template, request
from gtts import gTTS
from playsound import playsound
import os

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/generateSpeech', methods=["POST"])
def generateSpeech():
    textenter = request.form["textenter"]

    speech = gTTS(text=textenter)
    speech.save("file.mp3")
    playsound("file.mp3")
    os.remove("file.mp3")
    

    return render_template("index.html")



if __name__ == "__main__":
    app.run()

