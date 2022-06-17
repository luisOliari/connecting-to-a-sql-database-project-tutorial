from dotenv import load_dotenv
from  sqlalchemy import create_engine
import pandas as pd
import os

load_dotenv()

connection_string = os.getenv('DB_CONNECTION')
print(connection_string)

# 1) Connect to the database here using the SQLAlchemy's create_engine function

connection_string = os.getenv('DB_CONNECTION')
engine = create_engine(connection_string)
engine.connect()


# 2) Execute the SQL sentences to create your tables using the SQLAlchemy's execute function

#engine.execute("""
#CREATE TABLE IF NOT EXISTS publishers(
#    publisher_id INT NOT NULL,
#    name VARCHAR(255) NOT NULL,
#    PRIMARY KEY(publisher_id)
#);
#""")

# 3) Execute the SQL sentences to insert your data using the SQLAlchemy's execute function

#engine.execute("""
#INSERT INTO publishers(publisher_id,name) values (7,'Alfred A. Knopf');
#""")

# 4) Use pandas to print one of the tables as dataframes using read_sql function
result_dataFrame = pd.read_sql("Select * from publishers;", engine)
#print(result_dataFrame)

print(result_dataFrame.describe())