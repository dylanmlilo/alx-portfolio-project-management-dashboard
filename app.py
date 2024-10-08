from flask import Flask
from routes.routes_landing import landing_bp
from routes.routes_home import home_bp
from routes.routes_sections import sections_bp
from routes.routes_gis_data import gis_data_bp
from routes.routes_strategic import strategic_bp


app = Flask(__name__)
app.register_blueprint(landing_bp)
app.register_blueprint(home_bp)
app.register_blueprint(sections_bp)
app.register_blueprint(gis_data_bp)
app.register_blueprint(strategic_bp)


if __name__ == "__main__":
    app.run(debug=True, port=4000)
