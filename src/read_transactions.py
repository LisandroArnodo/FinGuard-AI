from sqlalchemy import create_engine
import pandas as pd


# Datos para conectarnos a PostgreSQL
DATABASE_URL = "postgresql://fingard_user:fingard_password@localhost:5432/fraud_database"


# Crear conexión con la base de datos
engine = create_engine(DATABASE_URL)


# Consulta SQL para obtener las transacciones
query = """
SELECT *
FROM transactions;
"""


# Leer datos desde PostgreSQL usando pandas
df = pd.read_sql(query, engine)


# Mostrar los datos
print(df)