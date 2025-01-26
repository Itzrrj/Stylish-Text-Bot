import os

class Config(object):

      BOT_TOKEN = os.environ.get("BOT_TOKEN", "7843411053:AAF86Uj3A3mbxMHo1gnysbwGaf5hPakkFKU")
      API_ID = int(os.environ.get("API_ID", 19593445))
      API_HASH = os.environ.get("API_HASH")
      OWNER_ID = int(os.environ.get("OWNER_ID"))

