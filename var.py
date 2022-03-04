import os
from decouple import config
from heroku3 import from_key
from os import getenv

class Var:
    API_ID = int(os.getenv("API_ID", ""))
    API_HASH = os.getenv("API_HASH", "")
    SESSION = os.getenv("SESSION")
    HNDLR = os.getenv("HNDLR", "!")
    GROUP_MODE = os.getenv("GROUP_MODE", "True")
    SUDO_USERS = list(map(int, getenv("SUDO_USERS").split()))
