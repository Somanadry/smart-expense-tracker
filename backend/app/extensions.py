# import sqlite3
# from flask import g


# def get_db(app):
#     if "db" not in g:
#         g.db = sqlite3.connect(app.config["DATABASE"])
#         g.db.row_factory = sqlite3.Row
#     return g.db


# def close_db(e=None):
#     db = g.pop("db", None)
#     if db is not None:
#         db.close()

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
