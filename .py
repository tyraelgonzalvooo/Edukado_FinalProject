from dotenv import load_dotenv
import os

load_dotenv("env.env")
passwordDB = os.getenv("DATABASEPASSWORD")
