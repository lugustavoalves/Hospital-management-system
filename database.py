"""
This module provides the database setup and utility functions for interacting
with the database for a healthcare management system.

It establishes the connection to the database, configures the SQLAlchemy engine, 
and provides helper functions to manage database sessions.
"""

import contextlib
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Localhost SQL Server
DATABASE_URL = "mssql+pyodbc://sa:DB_Password@localhost/Hospital?driver=ODBC+Driver+17+for+SQL+Server"
engine = create_engine(DATABASE_URL)

# Create the session factory
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Base class for ORM models
Base = declarative_base()


def get_db():
    """
    Dependency generator function for obtaining a database session.

    This function is typically used with FastAPI dependency injection
    to provide a database session to API routes.

    Yields:
        db (Session): SQLAlchemy database session.
    """
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@contextlib.contextmanager
def get_db_cli():
    """
    Context manager for obtaining a database session in command-line tools or scripts.

    Manages session creation, commits transactions, and handles rollbacks in case of exceptions.

    Yields:
        s (Session): SQLAlchemy database session.
    """
    s = SessionLocal()
    try:
        yield s
        s.commit()
    except Exception as e:
        s.rollback()
        raise e
    finally:
        s.close()
