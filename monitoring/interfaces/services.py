from flask import Blueprint, request, jsonify


from monitoring.application.services import TelemetryRecordApplicationService


telemetry_api = Blueprint("telemetry_api", __name__)
telemetry_record_service = TelemetryRecordApplicationService()


@telemetry_api.route("/api/v1/telemetry-monitoring/data-records", methods=["POST"])
def create_telemetry_record():
    """
    Create a telemetry record from the current Flask request JSON payload.
    This function reads JSON from flask.request, validates and extracts the following required fields:
    - device_id: unique identifier for the device (string or integer)
    - latitude: latitude coordinate (float)
    - longitude: longitude coordinate (float)
    - temperature: measured temperature (float)
    - humidity: measured humidity (float)
    - created_at: ISO-8601 timestamp or other created-at representation accepted by the service
    It then delegates creation to telemetry_record_service.create_monitoring_record(...) and returns
    a JSON representation of the created record along with an HTTP 201 status code on success.
    Returned JSON structure:
      "id": <record id>,
      "device_id": <device_id>,
      "latitude": <latitude>,
      "longitude": <longitude>,
      "temperature": <temperature>,
      "humidity": <humidity>,
      "created_at": <created_at>
    Behavior on errors:
    - If any required field is missing in the incoming JSON, the function returns a 400 response with
      {"error": "Missing field: '<field_name>'"}.
    - If a ValueError is raised during processing (for example, invalid types or value ranges), the function
      returns a 400 response with {"error": "<error message>"}.
    Returns:
      A tuple suitable for Flask return: (flask.Response, int). On success the response body is JSON and
      the status code is 201. On validation errors the status code is 400.
    Notes:
    - The function reads request JSON directly (no explicit schema validation beyond key presence and
      any validation performed inside telemetry_record_service).
    - Caller/context is expected to be a Flask request handling route where `request` and `jsonify` are available.
    """
    data = request.get_json()

    try:
        device_id = data["device_id"]
        latitude = data["latitude"]
        longitude = data["longitude"]
        temperature = data["temperature"]
        humidity = data["humidity"]
        created_at = data["created_at"]

        record = telemetry_record_service.create_monitoring_record(
            device_id=device_id,
            latitude=latitude,
            longitude=longitude,
            temperature=temperature,
            humidity=humidity,
            created_at=created_at,
        )

        return (
            jsonify(
                {
                    "id": record.id,
                    "device_id": record.device_id,
                    "latitude": record.latitude,
                    "longitude": record.longitude,
                    "temperature": record.temperature,
                    "humidity": record.humidity,
                    "created_at": record.created_at,
                }
            ),
            201,
        )

    except KeyError as e:
        return jsonify({"error": f"Missing field: {str(e)}"}), 400
    except ValueError as e:
        return jsonify({"error": str(e)}), 400


@telemetry_api.route("/api/v1/telemetry-monitoring/data-records", methods=["GET"])
def get_all_telemetry_records():
    """
    Retrieve all telemetry records from the database.

    Returns:
      JSON array of telemetry records:
      [
        {
          "id": <record id>,
          "device_id": <device_id>,
          "latitude": <latitude>,
          "longitude": <longitude>,
          "temperature": <temperature>,
          "humidity": <humidity>,
          "created_at": <created_at>
        },
        ...
      ]

    On error:
      Returns {"error": "<message>"} with HTTP 500.
    """
    try:
        # Get all records as dictionaries
        records = telemetry_record_service.get_monitoring_records()

        records_parsed = list(map(lambda record: record.to_dict(), records))

        return jsonify(records_parsed), 200

    except Exception as e:
        return jsonify({"error": str(e)}), 500
