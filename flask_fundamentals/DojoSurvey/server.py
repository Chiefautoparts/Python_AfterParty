from flask import Flask, render_template, redirect, request
app = Flask(__name__)

@app.route('/')
def index():
	return render_template('index.html')

@app.route('/survey', methods=['POST', 'GET'])
def survey():
	if request.method == 'POST':
		name = request.form['name']
		location = request.form['location']
		favLang = request.form['favLang']
		comment = request.form['comment']
		return render_template('results.html')
	else:
		return redirect('/')

@app.route('/survey/<name>/<location>/<favLang>/<comment>')
def display_results(name, location, favLang, comment):
 	
 	return redirect('results.html')

app.run(debug=True)