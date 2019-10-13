import os
import parser
from flask import Flask, request, jsonify, render_template
from flask_cors import CORS

template_dir = os.path.abspath('..')
app = Flask(__name__, template_folder=template_dir)
CORS(app)

@app.route('/', methods=['GET', 'POST'])
def index():
  if request.method == 'POST':
    print(request.json['name'])
    parser.getTextOnTopic(request.json['Topics'], int(request.json['CountWord']))
    return jsonify({'message': "данные получены!"})
  #parser.getTextOnTopic(['physics', 'law'])
  return render_template('index.html')
