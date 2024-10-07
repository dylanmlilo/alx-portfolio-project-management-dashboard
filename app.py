from flask import Flask, redirect, url_for, flash, render_template
from routes.routes_landing import landing_bp


app = Flask(__name__)
app.register_blueprint(landing_bp)


if __name__ == "__main__":
    app.run(debug=True, port=4000)
