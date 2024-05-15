import pydantic_settings
from dotenv import load_dotenv


class Config(pydantic_settings.BaseSettings):
    BS_ACCESS_KEY: str
    BS_USER: str
    BS_URL: str = 'http://hub.browserstack.com/wd/hub'
    TIMEOUT: float = 10
    APP_URL: str = 'bs://sample.app'


load_dotenv()
config = Config()
