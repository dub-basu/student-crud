from flask import *

from utils import Student

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('base.html')