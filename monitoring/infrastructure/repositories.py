from monitoring.domain.entities import TelemetryRecord
from monitoring.infrastructure.models import TelemetryRecordModel
import logging
from playhouse.shortcuts import model_to_dict

logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s [%(levelname)s] %(name)s: %(message)s"
)


logger = logging.getLogger("cargasafe.monitoring.repository")

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
        logger.debug("Inserted TelemetryRecordModel: %s", model_to_dict(record))

        output= TelemetryRecord(
            id=record.id,
            device_id=record.device_id,
            latitude=record.latitude,
            longitude=record.longitude,
            temperature=record.temperature,
            humidity=record.humidity,
            created_at=record.created_at,
        )

        output.id = record.id
        return output

    @staticmethod
    def get_all() -> list[TelemetryRecord]:
        records = []
        query = TelemetryRecordModel.select()
        for record in query:

            payload = TelemetryRecord(
                    id=record.id,
                    device_id=record.device_id,
                    latitude=record.latitude,
                    longitude=record.longitude,
                    temperature=record.temperature,
                    humidity=record.humidity,
                    created_at=record.created_at,
                )
            payload.id = record.id
            records.append(payload)
            
            logger.debug("Fetched record: %s", model_to_dict(record))

        return records
