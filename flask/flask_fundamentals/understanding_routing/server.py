from flask import Flask
app = Flask(__name__)

@app.route('/')
def root():
    return "Hello World!"

@app.route('/dojo')
def dojo():
    return "Dojo!"

@app.route('/say/<first_name>')
def hi_name(first_name):
    return "Hi "+str.capitalize(first_name)+"!"

@app.route('/say/repeat/<int:num>/<word>')
def numstring(num,word):
    return word*num

if __name__ == "__main__":
    app.run(debug=True)