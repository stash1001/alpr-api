import json
from openalpr import Alpr
import sys

alpr = Alpr("eu", "openalpr.conf", "/usr/share/openalpr/runtime_data")
if not alpr.is_loaded():
    print("Error loading OpenALPR")
    sys.exit(1)
results = alpr.recognize_file("plate.jpg")
print(json.dumps(results, indent=4))
alpr.unload()
