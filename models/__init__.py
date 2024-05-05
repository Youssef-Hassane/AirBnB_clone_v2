#!/usr/bin/python3
"""This module instantiates an object of class FileStorage or DBStorage"""

import os

from models.engine.db_storage import DBStorage
from models.engine.file_storage import FileStorage

# Check the environment variable 'HBNB_TYPE_STORAGE' to determine
# the type of storage to use (file or database)
# If the variable is not set or is set to 'db', a DBStorage instance is used
# Else, a FileStorage instance is used
storage = (DBStorage() if os.getenv('HBNB_TYPE_STORAGE') == 'db'
           else FileStorage())
"""A unique FileStorage/DBStorage instance for all models.

The type of storage depends on the value of the environment variable
'HBNB_TYPE_STORAGE'. If the variable is not set or is set to 'db',
a DBStorage instance is used. Else, a FileStorage instance is used.
"""

# Reload the storage with the objects already saved in the storage file
# or database
storage.reload()
