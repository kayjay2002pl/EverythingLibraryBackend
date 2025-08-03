import os

from dotenv import load_dotenv

load_dotenv()
env = os.environ

ROOT_PATH = env.get("ROOT_PATH", "api")

POSTGRES_HOST = env.get("POSTGRES_HOST")
POSTGRES_PORT = env.get("POSTGRES_PORT")
POSTGRES_DB = env.get("POSTGRES_DB")
POSTGRES_USER = env.get("POSTGRES_USER")
POSTGRES_PASSWORD = env.get("POSTGRES_PASSWORD")

SQLALCHEMY_DATABASE_URL = f"postgresql+psycopg2://{POSTGRES_USER}:{POSTGRES_PASSWORD}\
@{POSTGRES_HOST}:{POSTGRES_PORT}/{POSTGRES_DB}"