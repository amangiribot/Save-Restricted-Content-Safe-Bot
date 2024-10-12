# safe_repo
# Note if you are trying to deploy on vps then directly fill values in ("")

from os import getenv

API_ID = int(getenv("API_ID", "23401377"))
API_HASH = getenv("API_HASH", "a253e1cdcb1bdbad27dc4f1fcefca125")
BOT_TOKEN = getenv("BOT_TOKEN", "7931739724:AAFaIFwHf_w1MSogbcGYowUg67Qyotuyzto")
OWNER_ID = list(map(int, getenv("OWNER_ID", "7608856647").split()))
MONGO_DB = getenv("MONGO_DB", "mongodb+srv://amangiri11:amangiri525@cluster10.s8js2.mongodb.net/?retryWrites=true&w=majority&appName=Cluster10")
LOG_GROUP = getenv("LOG_GROUP", "1002452036381")
CHANNEL_ID = int(getenv("CHANNEL_ID", "7608856647"))
