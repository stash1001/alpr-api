from flask import Flask, make_response, request
from openalpr import Alpr
import subprocess
import json
import openalpr

print(openalpr.__file__)


app = Flask(__name__)


def gpu():
    # Lazy GPU detection as nvidia-smi returns nothing if no GPU
    p = subprocess.Popen(
        'nvidia-smi', shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    p.wait()
    if len(p.stdout.readlines()) > 0:
        return True
    else:
        return False


def recogniseplate(jpeg):
    results = alpr.recognize_array(jpeg)
    return results


@app.route('/health', methods=['GET'])
def health():
    return make_response("", 200)


@app.route('/', methods=['POST'])
def simple():
    top_n = int(request.form.get("top_n", 1))
    alpr.set_top_n(top_n)
    results = recogniseplate(request.files['image'].read())
    return make_response(json.dumps(results), 200)


if __name__ == "__main__":
    if gpu():
        configfile = "openalpr-gpu.conf"
    else:
        configfile = "openalpr-cpu.conf"

    alpr = Alpr("eu", configfile, "/usr/share/openalpr/runtime_data")
    alpr.set_default_region("eu")
    alpr.set_detect_region(False)
    app.run(host="0.0.0.0", debug=False, threaded=False)
