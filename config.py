# edit the URI below to add your RDS password and your AWS URL
# The other elements are the same as used in the tutorial
# format: (user):(password)@(db_identifier).amazonaws.com:3306/(db_name)

SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://flask:flasktest@flask-db-identifier.cevt7olsswvw.us-east-2.rds.amazonaws.com:3306/db_name'


# Uncomment the line below if you want to work with a local DB
#SQLALCHEMY_DATABASE_URI = 'sqlite:///test.db'

SQLALCHEMY_POOL_RECYCLE = 3600
WTF_CSRF_ENABLED = True
SECRET_KEY = 'C0k6QlwOwRcNTu00YikC4uNHQ8dqM8cIF2Oqu/Ko'
