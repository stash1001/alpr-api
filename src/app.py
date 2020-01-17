from flask import Flask, make_response, request
import json


app = Flask(__name__)


@app.route('/health', methods=['GET'])
def health():
    return make_response("", 200)


@app.route('/', methods=['POST'])
def simple():
    results = request.files['image'].read()
    return make_response(json.dumps(results), 200)


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True, threaded=False)
