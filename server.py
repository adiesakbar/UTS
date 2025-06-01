from flask import Flask, send_file

app = Flask(__name__)

@app.route('/')
def index():
    return send_file("log_detection.csv", as_attachment=False)

if __name__ == '__main__':
    app.run(debug=True, port=5000)
