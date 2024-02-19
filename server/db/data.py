import os
from api.db_utils import *

def rebuild_tables():
    exec_sql_file('src/db/tables.sql')