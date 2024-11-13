from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail

from src.utils.common import CommonFunctions as cm

class SendGrid:

    def __init__(self):        
        self.cm = cm()

    def send_email(self, msettings):
        api_key = msettings['api_key']
        sender_mail = msettings['sender']
        recipient = msettings['recipient']
        subject = msettings['subject']
        mail_content = msettings['content']

        message = Mail(
                from_email=sender_mail,
                to_emails=recipient,
                subject=subject,
                html_content=mail_content
            )

        try:

            sg = SendGridAPIClient(api_key.strip())
            response = sg.send(message)

            return {
                'recipient':recipient,
                'status_code':response.status_code,
                'body':response.body,
                'headers':response.headers,
                'success':True if 202==response.status_code else False,
                'error':None
            }

        except Exception as e:

            return {
                'recipient':recipient,
                'status_code':None,
                'body':None,
                'headers':None,
                'success':None,
                'error':str(e)
            }