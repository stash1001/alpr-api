from flask import Flask, make_response
app = Flask(__name__)


@app.route('/health', methods=['GET'])
def health():
    return make_response("", 200)


@app.route('/', methods=['POST'])
def simple():
    print("Got it 2")
    return make_response("healthy", 200)


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
