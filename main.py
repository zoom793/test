from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return 'مرحبًا، هذا خادم Flask يعمل!'

if __name__ == '__main__':
    app.run(debug=True)
