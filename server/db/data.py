import os
from server.api.db_utils import *

def rebuild_tables():
    exec_sql_file('sql/tables.sql')