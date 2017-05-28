from flask import Flask, render_template

from tasks import add

app = Flask(__name__)


@app.route("/")
def hello_world():
    add.delay(4, 4)
    return "ok"


def main():
    app.run(host="0.0.0.0", debug=True)


if __name__ == "__main__":
    main()
