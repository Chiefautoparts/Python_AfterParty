from flask import Flask, render_template, redirect, request
app = Flask(__name__)

@app.route('/')
def index():
	print '********test*********'
	return render_template('index.html')

@app.route('/process/<name>', methods=['GET'])
def process(name):
		print request.method
		name = request.form['name']
		print name
		print '***************************************************************************'
		return redirect('/', name)

app.run(debug=True)
