from flask import Flask, render_template, request, redirect, session 
import random

app = Flask(__name__)
app.secret_key = 'foxtrot uniform charlie kilo'

@app.route('/')
def index():
	return render_template('index.html')

@app.route('/number')
def number():
	num = random.randrange(0,101)
	session['guess'] = num
	status = ''
	if request.POST > num:
		status = 'Too high'
		return redirect('/', status)
	elif request.POST < num:
		status = 'Too Low'
		return redirect('/', status)
	else:
		status = 'CORRECT'
		return redirect('/', status)

app.run(debug=True)