from monitoring.infrastructure.repositories import TelemetryRecordRepository
from monitoring.domain.services import TelemetryRecordService


class TelemetryRecordApplicationService:
    def __init__(self):
        self.telemetry_record_repository = TelemetryRecordRepository()
        self.telemetry_record_service = TelemetryRecordService()

    def create_monitoring_record(
        self,
        device_id: str,
        latitude: float,
        longitude: float,
        temperature: float,
        humidity: float,
        created_at: str | None = None,
    ):
        record = self.telemetry_record_service.create_record(
            device_id=device_id,
            latitude=latitude,
            longitude=longitude,
            temperature=temperature,
            humidity=humidity,
            created_at=created_at,
        )
        self.telemetry_record_repository.save(record)
        return record

    def get_monitoring_records(self):
        return self.telemetry_record_repository.get_all()
