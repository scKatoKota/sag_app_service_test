import os

from flask import (Flask, redirect, render_template, request,
                   send_from_directory, url_for)
                   
from dotenv import load_dotenv

app = Flask(__name__)

load_dotenv()

@app.route('/')
def index():
   print('Request for index page received')
   return render_template('index.html')

@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'),
                               'favicon.ico', mimetype='image/vnd.microsoft.icon')

@app.route('/hello', methods=['POST'])
def hello():
   name = request.form.get('name')

   api_key = os.getenv("OPENAI_API_KEY")

   if name:
       print('Request for hello page received with name=%s' % name)
       return render_template('hello.html', name = name, api_key = api_key)
   else:
       print('Request for hello page received with no name or blank name -- redirecting')
       return redirect(url_for('index'))


if __name__ == '__main__':
   app.run()
