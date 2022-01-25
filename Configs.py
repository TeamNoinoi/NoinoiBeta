import os

class Config(object):
    APP_ID = int(os.environ.get("APP_ID", 6))
    API_HASH = os.environ.get("API_HASH", None)
    TOKEN = os.environ.get("TOKEN", None)
    BOT_US = os.environ.get("BOT_US", "")
    WELCOME_TEXT = os.environ.get("WELCOME_TEXT", None)
    RULES = os.environ.get("RULES", None)
    UPDATE_CHANNEL = os.environ.get("UPDATE_CHANNEL", "BAZIGARXD")

    
def get_list_key(name, required=False):
    if name in DEFAULTS:
        default = DEFAULTS[name]
    else:
        default = None
    if not (data := env.list(name, default=default)) and not required:
        log.warn("No list key: " + name)
        return []
    elif not data:
        log.critical("No list key: " + name)
        sys.exit(2)
    else:
        return data


def get_bool_key(name, required=False):
    if name in DEFAULTS:
        default = DEFAULTS[name]
    else:
        default = None
    if not (data := env.bool(name, default=default)) and not required:
        log.warn("No bool key: " + name)
        return False
    elif not data:
        log.critical("No bool key: " + name)
        sys.exit(2)
    else:
        return data
