class Config(object):
    LOGGER = True
    API_ID =25565263
    API_HASH = "2ead39886be0c1fd87a43ad4d27383f3"
    TOKEN = "7104902055:AAFaFXnNztLTRD60HDTxQvcOMk_jx_EXKPc"  
    OWNER_ID=5269893269
    
    SUPPORT_CHAT = "https://t.me/+7dqm_Z8gbqI2YWU1" 
    START_IMG = "https://envs.sh/Jcx.jpg"
    EVENT_LOGS = (-1002258593361)
    MONGO_DB_URI= "mongodb+srv://bikash:bikash@bikash.3jkvhp7.mongodb.net/?retryWrites=true&w=majority
    "
   
    DATABASE_URL = "postgresql://ok:MXeXzzu_vfSrPaGHmAIeMw@brisk-hound-6395.j77.aws-ap-south-1.cockroachlabs.cloud:26257/defaultdb?sslmode=verify-full"  # A sql database url from elephantsql.com
    CASH_API_KEY = (
        "U0DFLQA565HATSY6"
    )
    TIME_API_KEY = "C7SCKMIAITBJ"

    
    BL_CHATS = [https://t.me/+7dqm_Z8gbqI2YWU1] 
    DRAGONS = []
    DEV_USERS = []  
    DEMONS = [] 
    TIGERS = []  
    WOLVES = [] 

    ALLOW_CHATS = True
    ALLOW_EXCL = True
    DEL_CMDS = True
    INFOPIC = True
    LOAD = []
    NO_LOAD = []
    STRICT_GBAN = True
    TEMP_DOWNLOAD_DIRECTORY = "./"
    WORKERS = 8
    

class Production(Config):
    LOGGER = True


class Development(Config):
    LOGGER = True
