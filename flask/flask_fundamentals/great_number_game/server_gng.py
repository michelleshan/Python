from flask import Flask, render_template, request, session, redirect
app = Flask(__name__)
app.secret_key = 'iHateSessions'
import random

@app.route('/')
def root():
    if 'phrase' not in session:
        session['phrase'] = ""
    if 'counter' not in session:
        session['counter'] = 0
    if 'random_number' not in session:
        session['random_number']=random.randint(1,100)
    print(session['random_number'])
    return render_template('index.html')

@app.route('/results',methods=['post'])
def results():
    session['counter'] += 1
    number_input=request.form['number_input']
    if int(number_input) == session['random_number']:
        session['phrase'] = str(session['random_number'])+" was the number!"
        del session['random_number']
        session['submit_leaderboard'] = "hello"
    elif int(number_input) < session['random_number']:
        session['phrase'] = "Too low!"
    elif int(number_input) > session['random_number']:
        session['phrase'] = "Too high!"
    if session['counter'] == 5:
        session['phrase'] = 'You lose!'
    elif session['counter'] >= 5:
        session.clear()
    return redirect('/')

@app.route('/destroy_session')
def destroy():
    session.clear()
    return redirect('/')

# @app.route('/leaderboard')
# def leaderboard():


if __name__ == "__main__":
    app.run(debug=True)