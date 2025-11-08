from monitoring.domain.entities import TelemetryRecord
from monitoring.infrastructure.models import TelemetryRecordModel


class TelemetryRecordRepository:
    def __init__(self):
        pass

    @staticmethod
    def save(data) -> TelemetryRecord:
        record = TelemetryRecordModel.create(
            device_id=data.device_id,
            latitude=data.latitude,
            longitude=data.longitude,
            temperature=data.temperature,
            humidity=data.humidity,
            created_at=data.created_at,
        )

        return TelemetryRecord(
            device_id=record.device_id,
            latitude=record.latitude,
            longitude=record.longitude,
            temperature=record.temperature,
            humidity=record.humidity,
            created_at=record.created_at,
        )

    @staticmethod
    def get_all() -> list[TelemetryRecord]:
        records = []
        query = TelemetryRecordModel.select()
        for record in query:
            records.append(
                TelemetryRecord(
                    device_id=record.device_id,
                    latitude=record.latitude,
                    longitude=record.longitude,
                    temperature=record.temperature,
                    humidity=record.humidity,
                    created_at=record.created_at,
                )
            )
        return records
