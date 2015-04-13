from flask import Flask


if __name__ == "__main__":
    # To allow aptana to receive errors, set use_debugger=False
    app = Flask(__name__)
    app.debug = True
    app.run(host='0.0.0.0')