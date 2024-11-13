from src.config.app import AppConfig

from src.utils.common import CommonFunctions as cm
from src.helpers.common import CommonHelpers as cmhp

from src.utils.utils import UtilsFunctions as ut
from src.helpers.ctkinter_helpers import CTkinterHelpers as ctkh

import pandas as pd

class RecipientsManager:

    def __init__(self):
        self.cm = cm()
        self.cmhp = cmhp()
        self.ut = ut()
        self.ctkh = ctkh()

    def clear_list(self):
        recipient_list = self.cm.get_email_config('recipient_list')
        for key, recipient_info in recipient_list.items():

            if 'checkbox' in recipient_info:
                self.ctkh.forget(recipient_info['checkbox'])
                
                self.ctkh.destroy(recipient_info['checkbox'])
        
        self.cm.set_email_config('recipient_list', {})
        self.cm.set_email_config('duplicate_recipients', {})
        self.cm.set_email_config('selected_recipients', {})

        self.cmhp.update_recipients_total()
        self.cmhp.update_duplicate_total()

    def remove_selected(self):
        recipients_list = self.cm.get_email_config('recipient_list')
        recipients_duplicated = self.cm.get_email_config('duplicate_recipients')
        recipients_selected = self.cm.get_email_config('selected_recipients')

        if not len(recipients_selected):
            self.cmhp.show_message(self.cm._t('Select at least one item from the list'))
            return

        for id, recipient_info in recipients_selected.copy().items():

            if id in recipients_list:
                self.remove_from_recipient_list(id)
            
            if id in recipients_duplicated:
                self.remove_from_duplicated_list(id)     

            self.remove_from_selected_list(id)

            self.ctkh.forget(recipient_info['checkbox'])

            self.ctkh.destroy(recipient_info['checkbox'])

        self.cmhp.update_recipients_total()
        self.cmhp.update_duplicate_total()

    def remove_from_recipient_list(self, id):
        AppConfig.app['email_config']['recipient_list'].pop(id, None)

    def remove_from_duplicated_list(self, id):
        AppConfig.app['email_config']['duplicate_recipients'].pop(id, None)

    def remove_from_selected_list(self, id):
        AppConfig.app['email_config']['selected_recipients'].pop(id, None)

    def get_recipient_by_id(self, id):
        recipients_list = self.cm.get_email_config('recipient_list')
        return recipients_list.get(id, None)

    def search_duplicated(self):
        recipients_tmp = {}
        recipients_duplicated = []
        recipients_list = self.cm.get_email_config('recipient_list')

        for id, recipient in recipients_list.items():

            if 'recipient' in recipient:
                if recipient['recipient'] not in recipients_tmp:
                    recipients_tmp[recipient['recipient']] = [id]

                else:
                    recipients_tmp[recipient['recipient']].append(id)

        for recipient, ids in recipients_tmp.items():
            if len(ids) > 1:
                recipients_duplicated.extend(ids[1:])

        for recipient_id in recipients_duplicated:
            if recipient_id in recipients_list:
                self.append_recipient_in('duplicate_recipients', {recipient_id : recipients_list[recipient_id]})

        self.cmhp.update_duplicate_total()

        if len(self.cm.get_email_config('duplicate_recipients')):
            self.select_duplicated()
        else:
            self.cmhp.show_message(self.cm._t('The recipient list\ndoes not contain duplicate emails.'))
            self.cmhp.disable_elem('btn_select_duplicated')

    def set_recipient_selected(self, recipient):
        self.append_recipient_in('selected_recipients', recipient)

    def append_recipient_in(self, conf, val):
        self.cm.update_email_conf(conf, val)

    def select_duplicated(self):
        recipients = self.cm.get_email_config('duplicate_recipients')
        for id, recipient_info in recipients.items():
            if 'checkbox' in recipient_info:
                self.ctkh.select(recipient_info['checkbox'])
                self.recipient_clicked(id)
                self.move_widget_to_top(id)

    def process_recipients(self, filepath):
        recipients_limit = self.cm.get_config('rcp_limit')
        recipients_total = len(pd.read_csv(filepath, usecols=[0]))
        chunksize = self.ut.ceil(recipients_total / 10)+1

        if recipients_total > recipients_limit:
            self.cmhp.show_message('Load only 1000 contacts per file')
            return

        self.cmhp.show_message('Processing email list...', False)        

        for rcp in pd.read_csv(filepath, chunksize=chunksize, sep=r"[;|,\n]", engine='python', nrows=recipients_limit, header=None):
 
            recipient_list = rcp.stack().tolist()
            for recipient in recipient_list:
                self.process_recipients_task(recipient)

        self.cmhp.close_dialogbox()
        self.cmhp.toggle_recipients_tools()
    
    def process_recipients_task(self, recipient):
        recipient = recipient.strip().lower()
        if self.ut.validate_email(recipient):
            self.process_place_recipients([recipient])    

    def process_place_recipients(self, recipients):
        for recipient in recipients:
            self.load_recipient_in_scrollable_frame(recipient)

    def update_recipients_textbox(self, recipient):
        component_widget = self.cm.get_component_by_name('recipients_textbox','widget')
        if recipient and component_widget:
            self.ctkh.configure(component_widget, {'state':'normal'})
            self.ctkh.insert(component_widget, f'{recipient}\n', 0.0)
            self.ctkh.configure(component_widget, {'state':'disabled'}) 

    def load_recipient_in_box(self, recipient):        
        item_id = self.cm.get_uniq()
        recipient = recipient.strip()

        self.update_recipients_textbox(recipient)
        self.append_recipient_in('recipient_list', {
                                    item_id : {
                                        'recipient': recipient,
                                        'frame': None,
                                        'checkbox': None
                                    }
                                })
        
        self.cmhp.update_recipients_total()

    def load_recipient_in_scrollable_frame(self, recipient):
        item_id = self.cm.get_uniq()
        recipient = recipient.strip()

        recipient_checkbox = self.ctkh.make_checkbox(
                                        {
                                            'master':self.cm.get_component_key('scrollable_frames', 'recipients_scrollable_frame', 'widget'),
                                            'onvalue':'selected',
                                            'offvalue':'unselected',
                                            'command':lambda rcid=item_id: self.recipient_clicked(rcid),
                                            'font':self.cm.get_font('open_sans_n14'),
                                            'text':f'{recipient}',
                                            'checkbox_height':15,
                                            'checkbox_width':15,
                                            'corner_radius':5,
                                            'text_color':self.cm.get_color('list_item'),
                                            'text_color_disabled':self.cm.get_color('text_disabled'),
                                            'height':20,
                                            'width':300,
                                            'hover':True,
                                            'border_width':1,
                                            'border_color':self.cm.get_color('dark_grey'),
                                            'hover_color':self.cm.get_color('theme')
                                        }
                                    )

        self.ctkh.pack(recipient_checkbox,{'padx':5, 'pady':5})

        self.append_recipient_in('recipient_list', {
                                    item_id : {
                                        'recipient': recipient,
                                        'frame': None,
                                        'checkbox': recipient_checkbox
                                    }
                                })
        
        self.cmhp.update_recipients_total()

    def recipient_clicked(self, id):
        recipient = self.get_recipient_by_id(id)
        widget = recipient.get('checkbox', None)

        if widget:
            
            if self.ctkh.is_selected(widget) == 'unselected':
                self.remove_from_selected_list(id)

            else:
                self.set_recipient_selected({id : recipient})

        self.cmhp.toggle_selected_tools()

    def search_recipient_by_email(self, email):
        found = False
        email = email.strip()
        if not self.ut.validate_email(email):
            self.cmhp.show_message(self.cm._t('Enter a valid email'))
            return None

        recipient_list = self.cm.get_email_config('recipient_list')
        for id, recipient_info in recipient_list.items():
            if 'recipient' in recipient_info and email == recipient_info['recipient']:
                self.ctkh.select(recipient_info['checkbox'])
                self.recipient_clicked(id)
                self.move_widget_to_top(id)
                found = True

        if not found:
            self.cmhp.show_message(f"{self.cm._t('No results found for:')}\n{email}")

    def move_widget_to_top(self, id):
        recipient_info = self.get_recipient_by_id(id)

        # remove
        self.ctkh.forget(recipient_info['checkbox'])

        # pack        
        self.ctkh.pack(recipient_info['checkbox'],{'before':self.cmhp.get_scrollable_frame_key('recipients_scrollable_frame','widget').winfo_children()[0],'padx':5, 'pady':5})