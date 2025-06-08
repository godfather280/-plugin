import re
from os import getenv

from dotenv import load_dotenv
from pyrogram import filters

load_dotenv()

SUKH = getenv("SUKH", "mongodb+srv://tanishbokade555:<Tanishq@12345>@cluster0.b9hlgkz.mongodb.net/?retryWrites=true&w=majority")
