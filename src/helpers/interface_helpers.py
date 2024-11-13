from src.utils.common import CommonFunctions as cm
from src.helpers.common import CommonHelpers as cmhp

from src.utils.utils import UtilsFunctions as ut
from src.helpers.ctkinter_helpers import CTkinterHelpers as ctkh

class InterfaceHelpers:

    def __init__(self):
        self.cm = cm()
        self.cmhp = cmhp()
        self.ctkh = ctkh()
        self.ut = ut()

    def set_entry_text(self, entry, text):
        widget = self.cmhp.get_entry_key(entry, 'widget')
        if widget:
            self.ctkh.delete(widget)
            self.ctkh.insert(widget, text)

    def get_api_key(self):
        val = self.get_entry_val('api_key_entry')
        return val if val else None

    def get_remetente(self):
        val = self.get_entry_val('sender_entry')
        return val if val else None

    def get_subject(self):
        val = self.get_entry_val('subject_entry')
        return val if val else None   
    
    def mark_email_reset(self, widget):
        self.ctkh.configure(widget, {'fg_color':self.cm.get_color('bg_list_item')})

    def get_entry_val(self, name):
        widget = self.cmhp.get_entry_key(name, 'widget')
        val = self.ctkh.get(widget) if widget else None
        return val if val else None

    def auto_validate_email(self, e):
        if self.ut.validate_email(self.get_entry_val('search_entry')):
            self.cmhp.enable_elem('btn_search')
        else:
            self.cmhp.disable_elem('btn_search')