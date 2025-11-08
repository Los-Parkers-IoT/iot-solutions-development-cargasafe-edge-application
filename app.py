from flask import Flask

from monitoring.interfaces.services import telemetry_api
from shared.infrastructure.database import init_db

app = Flask(__name__)
app.register_blueprint(telemetry_api)

first_request = True


@app.before_request
def setup():
    """
    Initialize the database and create a test device on the first request.
    :return: None
    """
    global first_request

    if first_request:
        first_request = False
        init_db()
        # auth_application_service = iam.application.services.AuthApplicationService()
        # auth_application_service.get_or_create_test_device()


if __name__ == "__main__":
    app.run(debug=True)
