from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

SQLALCHEMY_DATABASE_URL = (
    "mysql+pymysql://k8s:123456@localhost:33306/k8sdeploytool?charset=utf8mb4"
)

engine = create_engine(
    SQLALCHEMY_DATABASE_URL, pool_recycle=3600, pool_pre_ping=True, echo=True
)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
