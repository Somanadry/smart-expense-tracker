# import os

# BASE_DIR = os.path.abspath(os.path.dirname(__file__))

# class Config:
#     DATABASE = os.path.join(BASE_DIR, "..", "instance", "expenses.db")
import os

BASE_DIR = os.path.abspath(os.path.dirname(__file__))

class Config:
    SQLALCHEMY_DATABASE_URI = "sqlite:///" + os.path.join(BASE_DIR, "..", "instance", "expenses.db")
    SQLALCHEMY_TRACK_MODIFICATIONS = False
