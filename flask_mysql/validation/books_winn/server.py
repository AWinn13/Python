from flask_app.controllers import authors_controller, books_controller
from flask_app import app
#! ALWAYS IMPORT CONTROLLERS


if __name__ == "__main__":
    app.run(debug=True)


