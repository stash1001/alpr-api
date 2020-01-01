from flask import Flask, make_response
from openalpr import Alpr
import subprocess

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


@app.route('/health', methods=['GET'])
def health():
    return make_response("", 200)


@app.route('/', methods=['POST'])
def simple():
    print("Got it 2")
    return make_response("healthy", 200)


if __name__ == "__main__":
    if gpu():
        configfile = "openalpr-gpu.conf"
    else:
        configfile = "openalpr-cpu.conf"

    alpr = Alpr("eu", configfile, "/usr/share/openalpr/runtime_data")
    app.run(host="0.0.0.0", debug=True)
