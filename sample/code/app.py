
from flask import Flask
from formfill import formfill_api

app = Flask(__name__)

app.register_blueprint(formfill_api)

if __name__ == "__main__":
        app.run()
