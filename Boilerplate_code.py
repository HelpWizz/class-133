from flask import Flask,render_template
app = Flask(__name__)

@app.route("/index")
def flask1():
    return render_template('index.html')

app.run(debug = True)