from flask import Flask, render_template, request, session, redirect
app = Flask(__name__)
app.secret_key = 'ninja'
import random

@app.route('/')
def root():
    if 'gold' not in session:
        session['gold'] = 0
    if 'activities' not in session:
        session['activities'] = []
    if 'g' not in session:
        session['g'] = 0
    
    return render_template('index.html')

@app.route('/process_money',methods=['post'])
def process():
    if request.form['location'] == 'farm':
        session['g'] = random.randint(10,20)
        session['gold'] += session['g']
        session['activities'].append(f"You earned {session['g']} golds!")
    elif request.form['location'] == 'cave':
        session['g'] = random.randint(5,10)
        session['gold'] += session['g']
        session['activities'].append(f"You earned {session['g']} golds!")
    elif request.form['location'] =='house':
        session['g'] = random.randint(2,5)
        session['gold'] += session['g']
        session['activities'].append(f"You earned {session['g']} golds!")
    elif request.form['location'] == 'casino':
        session['g'] = random.randint(-50,50)
        session['gold'] += session['g']
        if session['g'] > 0:
            session['activities'].append(f"You earned {session['g']} golds!")
        else:
            session['activities'].append(f"Ouch...you lost {session['g']} golds!")
    return redirect('/')

@app.route('/destroy_session',methods=['post'])
def destroy():
    session.clear()
    return redirect('/')

if __name__ == "__main__":
    app.run(debug=True)
