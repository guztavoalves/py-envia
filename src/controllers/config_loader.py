from src.utils.common import CommonFunctions as cm
from src.helpers.common import CommonHelpers as cmhp

from src.helpers.interface_helpers import InterfaceHelpers as ihp
from src.helpers.helpers import HelperFunctions as hf
from src.helpers.ctkinter_helpers import CTkinterHelpers as ctkh

class ConfigLoader:

    def __init__(self):
        self.cm = cm()
        self.cmhp = cmhp()
        self.ihp = ihp()
        self.hf = hf()
        self.ctkh = ctkh()

    def load_config(self):        
        settings = self.cm.get_json(self.cm.get_path('conf','user'))

        if settings and len(settings):

            if 'api_key' in settings and settings['api_key']:
                self.cm.set_email_config('api_key', settings['api_key'])
                self.ihp.set_entry_text('api_key_entry', self.cm.get_email_config('api_key'))

            if 'sender' in settings and settings['sender']:
                self.cm.set_email_config('sender', settings['sender'])
                self.ihp.set_entry_text('sender_entry', self.cm.get_email_config('sender'))

            if 'subject' in settings and settings['subject']:
                self.cm.set_email_config('subject', settings['subject'])
                self.ihp.set_entry_text('subject_entry', self.cm.get_email_config('subject'))

            if 'template' in settings and settings['template'] and 'path' in settings['template']:
                template_path = settings['template'].get('path', None)
                self.cmhp.set_template_file(template_path)