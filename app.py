from flask import Flask, render_template

app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
	return render_template('page.html')

@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'),
                          'favicon.ico',mimetype='image/vnd.microsoft.icon')