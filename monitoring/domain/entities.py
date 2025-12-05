from datetime import datetime


class TelemetryRecord: 
  def __init__(self, device_id: str, latitude: float, longitude: float, temperature: float, humidity: float, created_at: datetime, id: int = None):
    self.id = id
    self.device_id = device_id
    self.latitude = latitude
    self.longitude = longitude
    self.temperature = temperature
    self.humidity = humidity
    self.created_at = created_at
  
  def to_dict(self) -> dict:
    return {
      "id": self.id,
      "device_id": self.device_id,
      "latitude": self.latitude,
      "longitude": self.longitude,
      "temperature": self.temperature,
      "humidity": self.humidity
    }