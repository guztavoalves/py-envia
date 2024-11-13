from src.config.app import AppConfig
from src.utils.common import CommonFunctions as cm

class LanguageManager:

    def __init__(self):
        self.cm = cm()

    def set_language_dict(self):
        current_language = self.cm.get_current_language()
        lang_path = self.cm.get_attributes_by_type('path')['languages'][current_language]
        language_dict = self.cm.get_json(lang_path)
        AppConfig.app['language'].update({'dict' : language_dict})