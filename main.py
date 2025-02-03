from model import *
from dotenv import load_dotenv
import os
load_dotenv()
apiKey = os.getenv('API_KEY')

UM = UserModel(apiKey)

UM.fetchData()