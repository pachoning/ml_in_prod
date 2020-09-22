import sqlalchemy as db

# specify database configurations
config = {
    'host': 'localhost',
    'port': 3306,
    'user': 'root',
    'password': 'my-secret-pw',
    'database': 'ml_in_prod'
}
db_user = config.get('user')
db_pwd = config.get('password')
db_host = config.get('host')
db_port = config.get('port')
db_name = config.get('database')

# specify connection string
connection_str = f'mysql+pymysql://{db_user}:{db_pwd}@{db_host}:{db_port}/{db_name}'
#
#  connect to database
engine = db.create_engine(connection_str)
connection = engine.connect()

# pull metadata of a table
metadata = db.MetaData(bind=engine)
metadata.reflect(only=['raw_features'])

test_table = metadata.tables['raw_features']
query = db.select([test_table])
ResultProxy = connection.execute(query)
ResultSet = ResultProxy.fetchall()
print(ResultSet)
