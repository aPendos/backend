from flask import Flask


app = Flask(__name__)


@app.route('/')
def main():
    print(4 + 2)
    return '<h1> Главная страница </h1>'


if __name__ == '__main__':
    app.run(debug=True)