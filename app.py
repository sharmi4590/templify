from flask import Flask
import subprocess

app = Flask(__name__)

@app.route('/')
def index():
    # Return the HTML page
    with open('py.html', 'r') as file:
        return file.read()

@app.route('/run_sharmi')
def run_sharmi():
    # Execute the sharmi.py script and return the output
    result = subprocess.run(['python', 'sharmi.py'], capture_output=True, text=True)
    return result.stdout

if __name__ == '__main__':
    app.run()
