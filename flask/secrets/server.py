from flask import Flask, render_template, request
app = Flask(__name__)

@app.route('/') #GET ROUTE, receiving information
def root():
    return render_template('index.html')

@app.route('/tell_secret', methods=["POST"]) #POST route, sending information
def secret():
    print(request.form['secret'])
    return render_template('secret.html',secret=request.form['secret']) #NOT OK LINE

if __name__ == "__main__":
    app.run(debug=True)