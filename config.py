from os import environ

API_ID = int(environ.get("API_ID", "31024360"))
API_HASH = environ.get("API_HASH", "8419dab9aac814d0dd1f0a9ed3e63a3e")
BOT_TOKEN = environ.get("BOT_TOKEN", "8363693750:AAFOx0bEdCRurEYQxnLDFNxMoMlZBmliY3M")

# Make Bot Admin In Log Channel With Full Rights
LOG_CHANNEL = int(environ.get("LOG_CHANNEL", "-1003542287615"))
ADMINS = int(environ.get("ADMINS", "6891095964"))

# Warning - Give Db uri in deploy server environment variable, don't give in repo.
DB_URI = environ.get("DB_URI", "mongodb+srv://AmitChoudhary9:585xpplus@cluster0.ysfdfgv.mongodb.net/?appName=Cluster0") # Warning - Give Db uri in deploy server environment variable, don't give in repo.
DB_NAME = environ.get("DB_NAME", "vjjoinrequetbot")

# If this is True Then Bot Accept New Join Request 
NEW_REQ_MODE = bool(environ.get('NEW_REQ_MODE', Ture))
