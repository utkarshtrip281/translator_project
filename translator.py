from flask import Flask , render_template , request
from googletrans import Translator
app = Flask(__name__)

@app.route('/' , methods =["GET", "POST"])
def hello_world():
    if request.method == "POST":
        text = request.form.get("input")
        src = request.form.get("option1")
        dest = request.form.get("option2")
        translator = Translator()
        content = {
            "src" : text ,
            "dest" : translator.translate(text , dest , src).text
        }
        print(text , src , dest , translator.translate(text , dest , src).text)
        return render_template("result.html" , content = content)
    return render_template("ut2.html")
app.run()