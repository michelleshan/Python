from flask import Flask, render_template, request, session, redirect
app = Flask(__name__)
app.secret_key = 'whoAteAllTheFigBars'

@app.route('/')
def root():
    if 'count' in session:
        print('count exists!')
        session['count'] +=1
    else:
        print('count does NOT exist') 
        session['count'] = 1
    return render_template('bs_counter.html')


@app.route('/destroy_session', methods=['post'])
def destroy():
    session.clear()
    return redirect('/') 

if __name__ == "__main__":
    app.run(debug=True)