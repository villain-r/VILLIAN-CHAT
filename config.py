from os import getenv

from dotenv import load_dotenv

load_dotenv()

API_ID = "24833955"
# -------------------------------------------------------------
API_HASH = "176360aef3e85805ea17d304adf63f18"
# --------------------------------------------------------------
BOT_TOKEN = getenv("BOT_TOKEN", None)
MONGO_URL = getenv("MONGO_URL", None)
OWNER_ID = int(getenv("OWNER_ID", "8081953831"))
SUPPORT_GRP = "LOYAL_KINGDOM"
UPDATE_CHNL = "LOYAL_IMPERIAL"
OWNER_USERNAME = "ll_AMRIT_ll"
