from src.utils.common import CommonFunctions as cm
from src.helpers.common import CommonHelpers as cmhp

from src.utils.utils import UtilsFunctions as ut
from src.helpers.helpers import HelperFunctions as hf

from src.controllers.recipients_manager import RecipientsManager as rcm
from src.services.sendgrid import SendGrid as sdg

class EmailSender:
   
    def __init__(self):
        self.cm = cm()
        self.cmhp = cmhp()
        self.ut = ut()
        self.hf = hf()
        self.sdg = sdg()
        self.rcm = rcm()

    def sending(self):
        task = self.ut.thread({'target':self.send_task})
        task.start()

    def send_email(self, email):
        response = self.sdg.send_email({
                            'api_key':self.cm.get_email_config('api_key'),
                            'sender':self.cm.get_email_config('sender'),
                            'subject':self.cm.get_email_config('subject'),
                            'content':self.hf.get_template(),
                            'recipient':email
                    })
        
        return self.process_response(response)

    def process_response(self, response):
        # Log sent status
        log_message = f"Recipient: {response['recipient']}\nStatus: {response['status_code']}"

        if response['success']:
            log_message += '\n+'
        
        if response['error'] or response['success'] == False:
            log_message += f"Error: {response['error']}\n+"

        self.cmhp.log_send(log_message)

        return response['success']            
    
    def send_task(self):
        self.cm.set_send_status(True)

        recipients_list = self.cm.get_email_config('recipient_list')
        for id, recipient_info in recipients_list.items():

            recipient_email = recipient_info['recipient']

            if not self.cm.get_send_status():
                break

            if id in self.cm.get_email_config('sent_emails'):
                continue

            send_status = self.send_email(recipient_email)

            if send_status:
                self.rcm.append_recipient_in('sent_emails', {id : recipient_info})
                self.cmhp.mark_email_send(recipient_info['checkbox'])
                self.cmhp.update_sent_total()

        self.cmhp.toggle_elems([
                    'btn_send',
                    'btn_stop',
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