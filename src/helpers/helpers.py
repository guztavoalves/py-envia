from src.utils.common import CommonFunctions as cm
from src.utils.utils import UtilsFunctions as ut

class HelperFunctions:    

    def __init__(self):
        self.cm = cm()
        self.ut = ut()

    def get_recipients_selected(self):
        return self.cm.get_email_config('selected_recipients')

    def get_template_path(self):
        template_info = self.cm.get_email_config('template')
        template_filepath = template_info.get('path', None)
        
        if template_filepath and self.cm.path_exists(self.cm.abspath(template_filepath)):
            return template_filepath

        return None

    def get_template(self):
        template_path = self.get_template_path()
        if template_path:
            return self.cm.open_file(template_path)

        return None

    def askopenfile_template(self):
        return self.ut.askopenfile(['html','txt'], 'html', 'r')

    def askopenfile_recipients(self):
        return self.ut.askopenfile(['csv','txt'], 'txt', 'r')

    def asksaveas_txt(self):
        return self.ut.asksaveas(['txt'], 'txt')
