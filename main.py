from model import *
from view import *
from controller import *
from dotenv import load_dotenv
import os
load_dotenv()
apiKey = os.getenv('API_KEY')

um = UserModel(apiKey)
uv = UserView()
uc = UserController(uv, um)
uv.setController(uc)
uc.run()