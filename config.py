__author__ = 'My'

# # dialect+driver://username:password@host:port/database
# DIALECT = 'mysql'
# # DRIVER = 'mysqldb'
# DRIVER = 'mysqlconnector'
# TEXT_PATH='D:\\FlaskProject\\Flasktest1\\test'
# USERNAME = 'root'
# PASSWORD = 'root'
# HOST = '127.0.0.1'
# PORT = '3306'
# DATABASE = 'function_test'
# # SQLALCHEMY_DATABASE_URI = "{}+{}://{}:{}@{}:{}/{}?charset=utf8".format(DIALECT,DRIVER,USERNAME,PASSWORD,HOST,PORT,DATABASE)
# SQLALCHEMY_DATABASE_URI = "{}+{}://{}:{}@{}:{}/{}".format(DIALECT,DRIVER,USERNAME,PASSWORD,HOST,PORT,DATABASE)

SQLALCHEMY_TRACK_MODIFICATIONS = False
SQLALCHEMY_DATABASE_URI = 'mssql+pyodbc://sa:catherine@127.0.0.1:1433/data'
TEMPLATES_AUTO_RELOAD = True
SEND_FILE_MAX_AGE_DEFAULT = 0
DEBUG = True


