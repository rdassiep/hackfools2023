from flask import Flask, render_template

app = Flask(__name__)


@app.route('/', methods=['GET'])
def home():
    return render_template('index.html')

@app.route('/index.html', methods=['GET'])
def index():
    return render_template('index.html')


@app.route('/portfolio.html', methods=['GET'])
def portfolio():
    return render_template('portfolio.html')


@app.route('/pricing.html', methods=['GET'])
def pricing():
    return render_template('pricing.html')


if __name__ == '__main__':
    app.run(debug=True)