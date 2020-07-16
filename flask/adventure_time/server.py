from flask import Flask, render_template, request
app = Flask(__name__)

@app.route('/')
def root():
    return render_template('index1.html')

@app.route("/fight",)
def fight():
    return render_template("fight.html")

@app.route("/turnaround")
def turnaround():
    return render_template("turnaround.html")

@app.route("/fight/mewtwo")
def mewtwo():
    return render_template("mewtwo.html")


if __name__ == "__main__":
    app.run(debug=True)
