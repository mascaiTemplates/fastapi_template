from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

from . import users # IMPORTANT: intended to register models for alembic (should be at the end of the file)
