class Config:
    db_user = "DevAuth"
    db_password = "Dev123456"
    db_host = "db"
    db_port = "3306"
    db_name = "DevDb"
    SQLALCHEMY_DATABASE_URI = f"mysql+pymysql://{db_user}:{db_password}@{db_host}:{db_port}/{db_name}"
    SQLALCHEMY_TRACK_MODIFICATIONS = False