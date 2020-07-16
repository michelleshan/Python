from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def root():
    return "I've started my first web server!"

@app.route('/hello')
def hello():
    return "Hello there!"

@app.route('/like/<int:waffle>')
def like(waffle):
    return "I like the number " + str(waffle) + "!"

@app.route('/template')
def temmppowushgiesjrng():
    return render_template("index.html", phrase="The mystery phrase", characters=["Homer","Marge","Lisa","Bart"])
#front_end_name=back_end_value

if __name__ == "__main__":
    app.run(debug=True)