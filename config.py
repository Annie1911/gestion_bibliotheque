import os #manipulation de chemein et acces au systeme

BASE_DIR  = os.path.abspath(os.path.dirname(__file__))


class Config :
    SQLACHEMY_DATABASE_URI = f"sqlite:///{os.path.join(BASE_DIR,'database','library.db')}"
    
    SQLALCHEMY_TRACK_MODIFICATIONS = False #Désactive des trucs inutiles.