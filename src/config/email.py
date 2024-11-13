class EmailConfig:

    def __init__(self):

        self.email_config = {}
        
        self.email_config = {
                'api_key':'',
                'sender':'',
                'subject':'',
                'template':{},
                'recipient_list':{},
                'duplicate_recipients':{},
                'selected_recipients':{},
                'sent_emails':{},
                'error_emails':{}
            }