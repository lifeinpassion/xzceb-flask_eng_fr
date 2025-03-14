
from machinetranslation import translator
from flask import Flask, render_template, request
import json

app = Flask("Web Translator")

@app.route("/englishToFrench")
def englishToFrench():
    textToTranslate = request.args.get('textToTranslate')
    # Write your code here
    output = translator.englishToFrench(textToTranslate)
    return "Translated text to French" + ":" + output

@app.route("/frenchToEnglish")
def frenchToEnglish():
    textToTranslate = request.args.get('textToTranslate')
    # Write your code here
    output = translator.frenchToEnglish(textToTranslate)
    return "Translated text to English" + ":" + output

@app.route("/")
def renderIndexPage():
    # Write the code to render template
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=8080)

#host="0.0.0.0", port=8080