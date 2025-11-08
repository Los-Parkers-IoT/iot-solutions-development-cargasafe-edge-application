from peewee import Model, AutoField, CharField, FloatField, DateTimeField
from shared.infrastructure.database import db


class TelemetryRecordModel(Model):
  id = AutoField()
  device_id = CharField()
  latitude = FloatField()
  longitude = FloatField()
  temperature = FloatField()
  humidity = FloatField()
  created_at = DateTimeField()
  
  
  class Meta:
    database = db
    table_name = 'telemetry_records'