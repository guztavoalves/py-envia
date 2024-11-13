from src.utils.common import CommonFunctions as cm
from src.helpers.common import CommonHelpers as cmhp

from src.helpers.helpers import HelperFunctions as hf

class ExportRecipients:

    def __init__(self):      
        self.cm = cm()
        self.cmhp = cmhp()
        self.hf = hf()

    def export(self, recipients):
        if len(recipients):
            recipients_found = []
            for id, recipient in recipients.items():
                if 'recipient' in recipient:
                    recipients_found.append(recipient['recipient'])

            recipients_export = '\n'.join(recipients_found)

            path = self.hf.asksaveas_txt()
            self.cmhp.show_message(self.cm._t('Successfully exported!')) if self.cm.save_file(path, recipients_export) else self.cmhp.show_message(self.cm._t('Failed to export!'))