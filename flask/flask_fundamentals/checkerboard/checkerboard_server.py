from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def root():
    return render_template('index.html')

@app.route('/<int:x>')
def row_amount(x):
    return render_template('index.html', rows=int(x))

@app.route('/<int:x>/<int:y>')
def row_column_amount(x,y):
    return render_template('index.html',rows=int(x),columns=int(y))

if __name__ == "__main__":
    app.run(debug=True)