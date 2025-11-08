"""
Database initialization and connection management for the Smart Band application.
"""
from peewee import SqliteDatabase

# Initialize the SQLite database
db = SqliteDatabase('cargasafe.db')

def init_db() -> None:
    """
    Initialize the database and create tables if they do not exist.

    """
    db.connect()
    from iam.infrastructure.models import Device
    from health.infrastructure.models import HealthRecord
    db.create_tables([Device, HealthRecord], safe=True)
    db.close()