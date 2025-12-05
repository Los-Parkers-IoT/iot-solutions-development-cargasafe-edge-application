import requests

class MonitoringApi:
  def __init__(self):
    self.baseUrl = 'https://iot-solutions-development-cargasafe.onrender.com/api/v1/telemetry'
    pass
  

  def saveTelemetryData(self, monitoringSessionId, temperature, humidity, latitude, longitude):
      try:

        response = requests.post(self.baseUrl, json={
          "monitoringSessionId": monitoringSessionId,
          "temperature": temperature,
          "humidity": humidity,
          "vibration": 0,
          "longitude": longitude,
          "latitude": latitude
        })

        response.raise_for_status()
        return response.json()

      except requests.exceptions.RequestException as e:
        print(f"[Error] POST {self.baseUrl} failed: {e}")


