from markupsafe import escape
from flask import Flask
from Code_Poets_Benfords_law import *

app = Flask(__name__)


@app.route("/")

def index():

    return "App regarding the Benford's Law!"

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=8080, debug=True)
