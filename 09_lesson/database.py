from sqlalchemy import create_engine

connection_string = 'postgresql://user:password@localhost:5432/mydatabase'

engine = create_engine(connection_string)

