from flask import Flask, render_template
app = Flask(__name__)

@app.route('/play')
def play():
    return render_template('playground_index.html')

@app.route('/play/<int:x>')
def repeatboxes(x):
    return render_template('boxes.html',repeat_times=int(x))

@app.route('/play/<int:x>/<color>')
def addcolor(x,color):
    return render_template('boxes.html',repeat_times=int(x),box_color=color)

if __name__ == "__main__":
    app.run(debug=True)