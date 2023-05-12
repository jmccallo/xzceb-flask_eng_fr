from flask import Flask, render_template, request
from machinetranslation.translator import english_to_french, french_to_english

app = Flask(__name__)

@app.route('/home/project/xzceb-flask_eng_fr/final_project/templates/index.html')
def index():
    return render_template('index.html')

@app.route('/englishToFrench', methods=['POST'])
def translate_english_to_french():
    english_text = request.form['englishText']
    french_text = english_to_french(english_text)
    return french_text

@app.route('/frenchToEnglish', methods=['POST'])
def translate_french_to_english():
    french_text = request.form['frenchText']
    english_text = french_to_english(french_text)
    return english_text

if __name__ == '__main__':
    app.run()
