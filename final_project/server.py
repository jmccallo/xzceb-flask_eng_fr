from flask import Flask, render_template, request
from machinetranslation.translator import english_to_french, french_to_english

app = Flask(__name__, static_folder="static")

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/englishToFrench', methods=['GET','POST'])
def translate_english_to_french():
    if request.method == 'POST':
        english_text = request.form['englishText']
        french_text = english_to_french(english_text)
        return french_text
    elif request.method == 'GET':
        text_to_translate = request.args.get('textToTranslate')
        french_text = english_to_french(text_to_translate)
        return french_text

@app.route('/frenchToEnglish', methods=['GET','POST'])
def translate_french_to_english():
    if request.method == 'POST':
        french_text = request.form['frenchText']
        english_text = french_to_english(french_text)
        return english_text
    elif request.method == 'GET':
        text_to_translate = request.args.get('textToTranslate')
        english_text = french_to_english(text_to_translate)
        return english_text


if __name__ == '__main__':
    app.run(debug=True, port=8080)
