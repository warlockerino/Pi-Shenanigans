import os
from flask import Flask, request, render_template

UPLOAD_FOLDER = 'uploads'


app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route('/', methods=['GET', 'POST'])
def index():
	return "This is the Index"

# Route that will process the file upload
if __name__ == "__main__":
	#0.0.0.0 for visibility in local Wifi
    	app.run(host='0.0.0.0', port=9000, debug=True)
