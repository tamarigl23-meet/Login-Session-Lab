from flask import Flask, render_template, request, url_for, redirect
from flask import session as login_session

app = Flask(__name__)
app.config['SECRET_KEY'] = 'super-secret-key'

@app.route('/', methods=['GET', 'POST'] ) # What methods are needed?
def home():
	if request.method == 'POST':
		try:
			login_session['quote'] = request.form['quote']
			login_session['author_quote'] = request.form['author_quote']
			login_session['author_age'] = request.form['author_age']
			return render_template('thanks.html')
		except:
			return render_template('error.html')

	else:
		return render_template('home.html')


@app.route('/error')
def error():

	return render_template('error.html')


@app.route('/display')
def display():

	return render_template('display.html',quote1=login_session['quote'], author_quote1=login_session['author_quote'], author_age1 =login_session['author_age']) # What variables are needed?


@app.route('/thanks')
def thanks():

	return render_template('thanks.html')


if __name__ == '__main__':
	app.run(debug=True)