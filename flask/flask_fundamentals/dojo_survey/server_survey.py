from flask import Flask, render_template, request
app = Flask(__name__)

@app.route('/',methods=['GET'])
def welcome():
    return render_template('index_bs.html')

@app.route('/result',methods=['POST'])
def result():
    print(request.form)
    name=request.form['name']
    email=request.form['email']
    location=request.form['locations']
    language=request.form['language']
    comment=request.form['comment']
    newsletter=request.form['newsletter']
    content=request.form['content']
    return render_template('result.html',name=name,location=location,language=language,newsletter=newsletter,content=content,comment=comment)

if __name__ == "__main__":
    app.run(debug=True)