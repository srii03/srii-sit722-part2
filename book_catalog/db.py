from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os

# Load the DATABASE_URL from an environment variable, with a default value
DATABASE_URL = os.getenv(
    "DATABASE_URL", 
    "postgresql://lib_postgres_db_user:vABkDXl758bv3Gz6LaQeSPc8WWpwCosA@dpg-crtog2u8ii6s73agc630-a.oregon-postgres.render.com/lib_postgres_db"
)

# Create the engine, using echo=True for logging SQL queries for debugging
engine = create_engine(DATABASE_URL, echo=True)

# Define the base class for all models
Base = declarative_base()

# Create session factory
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Dependency to get a database session
def get_db():
    db = SessionLocal()
    try:
        yield db  # Provide the session to the calling context
    finally:
        db.close()  # Ensure the session is always closed
