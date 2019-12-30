from flask import Flask, make_response
app = Flask(__name__)


@app.route('/', methods=['POST'])
def simple():
    print("Got it 2")
    return make_response("", 200)


if __name__ == "__main__":
    app.run(debug=True)
