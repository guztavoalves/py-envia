from src.utils.common import CommonFunctions as cm
from src.helpers.common import CommonHelpers as cmhp

from src.utils.utils import UtilsFunctions as ut
from src.helpers.helpers import HelperFunctions as hf
from src.helpers.interface_helpers import InterfaceHelpers as ihp

from src.controllers.export_recipients import ExportRecipients as xp
from src.controllers.email_sender import EmailSender as sd
from src.controllers.recipients_manager import RecipientsManager as rcm

from src.helpers.ctkinter_helpers import CTkinterHelpers as ctkh

class CommandManager:

    def __init__(self):
        self.cm = cm()
        self.cmhp = cmhp()
        self.ihp = ihp()
        self.ctkh = ctkh()
        self.ut = ut()
        self.hf = hf()
        self.xp = xp()
        self.sd = sd()
        self.rcm = rcm()

    def cmd_export_selected(self):
         self.xp.export(self.cm.get_email_config('selected_recipients'))
     
    def cmd_export_list(self):
         self.xp.export(self.cm.get_email_config('recipient_list'))

    def cmd_stop(self):
        self.cmhp.toggle_elems([
                            'btn_stop',
                            'btn_send',
                            'search_entry',
                            'btn_clear_list',
                            'btn_select_duplicated',
                            'btn_delete_selected',
                            'btn_load_recipient_list',
                            'btn_export_selection',
                            'btn_export_list',
                            'btn_select_all',
                            'btn_deselect_all'
                    ])

        self.cm.set_send_status(False)

    def cmd_send(self):

        if not self.ihp.get_entry_val('api_key_entry'):
            self.cmhp.show_message(self.cm._t('Enter your API Key'))

        elif not self.ut.validate_email(self.ihp.get_entry_val('sender_entry')):
            self.cmhp.show_message(self.cm._t('Enter a valid email'))

        elif not self.ut.validate_subject(self.ihp.get_entry_val('subject_entry')):
            self.cmhp.show_message(self.cm._t('Enter a valid subject. From 5 to 100 characters'))

        elif not self.hf.get_template():
            self.cmhp.show_message(self.cm._t('Select a valid template file'))

        elif len(self.cm.get_email_config('recipient_list')) <= 0:
            self.cmhp.show_message(self.cm._t('Load the recipient list'))

        else:

            self.cmhp.toggle_elems([
                            'btn_stop',
                            'btn_send',
                            'search_entry',
                            'btn_clear_list',
                            'btn_select_duplicated',
                            'btn_delete_selected',
                            'btn_load_recipient_list',
                            'btn_export_selection',
                            'btn_export_list',
                            'btn_select_all',
                            'btn_deselect_all'
                        ])
            
            self.sd.sending()

    def cmd_select_all(self):
        recipient_list = self.cm.get_email_config('recipient_list')
        for id, recipient_info in recipient_list.items():
            if 'checkbox' in recipient_info:
                self.ctkh.select(recipient_info['checkbox'])
                self.rcm.recipient_clicked(id)

    def cmd_deselect_all(self):
        recipients_selected = self.cm.get_email_config('selected_recipients')
        for id, recipient_info in recipients_selected.copy().items():
            if 'checkbox' in recipient_info:
                self.ctkh.deselect(recipient_info['checkbox'])
                self.rcm.recipient_clicked(id)

    def cmd_view_file(self):
        template_filepath = self.hf.get_template_path()
        if template_filepath:
            self.cm.startfile(template_filepath)
        
        else:
            self.cmhp.show_message(self.cm._t('No file to preview'))

    def cmd_search(self):
        self.rcm.search_recipient_by_email(self.ihp.get_entry_val('search_entry'))

    def cmd_load_list_file(self):
        file_obj = self.hf.askopenfile_recipients()

        if file_obj:
            task = self.ut.thread({'target':self.rcm.process_recipients, 'args':(file_obj.name,)})
            task.start()   

    def cmd_clean_list(self):
        self.rcm.clear_list()
        self.cmhp.toggle_recipients_tools()

    def cmd_insert_new_recipient(self):
        email = self.ihp.get_entry_val('new_email_entry')

        if email and self.ut.validate_email(email):
            self.insert_new_recipient(email)
            self.cmhp.update_recipients_total()
            self.cmhp.clear_entry('new_email_entry')

        else:
            self.cmhp.show_message(self.cm._t('Enter a valid email'))

        self.cmhp.toggle_recipients_tools()

    def cmd_select_duplicated(self):
        self.rcm.search_duplicated()
        self.cmhp.toggle_selected_tools()

    def cmd_remove_selected(self):
        self.rcm.remove_selected()
        self.cmhp.toggle_recipients_tools()
        self.cmhp.toggle_selected_tools()        

    def cmd_open_dev_home(self):
        link = self.cm.get_attributes_by(['author','link','github'])
        if link:
            self.cm.open_link(link)

    def cmd_save(self):
        app_config = {
                        'api_key' : self.ihp.get_api_key(),
                        'sender' : self.ihp.get_remetente(),
                        'subject' : self.ihp.get_subject(),
                        'template' : {'path': self.hf.get_template_path()},
                    }
        
        self.cm.set_email_config('api_key', app_config['api_key'])
        self.cm.set_email_config('sender', app_config['sender'])
        self.cm.set_email_config('subject', app_config['subject'])
        self.cm.set_email_config('template', app_config['template'])
        
        self.cm.save_json(self.cm.get_path('conf','user'), app_config)

    def cmd_clear_config(self):
        self.cmhp.clear_entry('api_key_entry')
        self.cmhp.clear_entry('sender_entry')
        self.cmhp.clear_entry('subject_entry')
        self.cmhp.clear_entry('search_entry')

        self.cm.set_email_config('api_key', '')
        self.cm.set_email_config('sender', '')
        self.cm.set_email_config('subject', '')
        self.cm.set_email_config('template', {})

        self.ctkh.configure(self.cmhp.get_button_key('btn_load_template','widget'), {'text':self.cm._t('Choose file...')})

        self.cm.set_email_config('template',{})

    def cmd_select_file(self):
        file_obj = self.hf.askopenfile_template()
        self.cmhp.set_template_file(file_obj.name)

    def insert_new_recipient(self, email):
        if self.ut.validate_email(email):
            self.rcm.process_place_recipients([email])