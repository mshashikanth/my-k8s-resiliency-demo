from flask import Flask
import os

app = Flask(__name__)

@app.route('/')
def hello_world():
    # Added a simple environment variable to show pod details
    pod_name = os.getenv('HOSTNAME', 'unknown_pod')
    return f'Hello from Backend! Running on Pod: {pod_name}\n'

@app.route('/health')
def health_check():
    return 'OK', 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)