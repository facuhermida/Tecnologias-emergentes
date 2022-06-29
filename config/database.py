from sqlalchemy import create_engine, MetaData
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

engine = create_engine("mysql+pymysql://root:MySQLTECEm$2022@137.184.200.34:3306/tecnologias_emergentes")

meta = MetaData()

conn = engine.connect()


#SQLALCHEMY_DATABASE_URL = "sqlite:///./sql_app.db"
#SQLALCHEMY_DATABASE_URL = "mysql://root:MySQLTECEm$2022@USAL/db"

#engine = create_engine(
 #   SQLALCHEMY_DATABASE_URL
#)
#SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

#Base = declarative_base()