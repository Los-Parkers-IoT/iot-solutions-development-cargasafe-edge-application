from monitoring.domain.entities import TelemetryRecord
from dateutil.parser import parse
from datetime import timezone, datetime

class TelemetryRecordService:
  def __init__(self):
    pass
  
  @staticmethod
  def create_record(device_id: str, latitude: float, longitude: float, temperature: float, humidity: float, created_at: str | None) -> TelemetryRecord:
    try:
      
      if created_at:
        parsed_created_at = parse(created_at).astimezone(timezone.utc)
      else:
        parsed_created_at = datetime.now(timezone.utc)
                
      record = TelemetryRecord(
        device_id=device_id,
        latitude=latitude,
        longitude=longitude,
        temperature=temperature,
        humidity=humidity,
        created_at=parsed_created_at
      )
      return record
    except Exception as e:
      raise ValueError(f"Failed to create TelemetryRecord: {e}")
    