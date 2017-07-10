from flask import Flask, render_templates, request, redirect, session
app = Flask(__name__)

@app.route('/')
def index():
	