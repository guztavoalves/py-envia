from src.utils.common import CommonFunctions as cm

from tkinter import filedialog
import json, re, csv, threading, math

class UtilsFunctions:

    def __init__(self):

        self.cm = cm()

    def is_viewport(self, viewport):
        return True if self.cm.get_attr('viewport') == viewport else False

    def validate_email(self, email):
        if email:
            return True if re.match(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$', email) else False

    def validate_emails(self, list):
        if len(list):
            return [em for em in list if self.validate_email(em)]

    def validate_subject(self, val):
        if 5 <= len(val) <= 100:
            return True
        
        return False
    
    def ceil(self, val):
        return math.ceil(val)

    def open_csv_file(self, path):
        with open(path, newline='', encoding='UTF-8') as file:
            csv_data = csv.reader(file, delimiter=',')
            items = []
            for item in csv_data:
                items.append(item)
            return items

    def process_items_json(self, data):
        items = []
        for e in json.loads(data)['items']:
            items.append(e)

        return items if len(items) else None

    def process_items_txt(self, data):
        items = data.splitlines()
        return items if len(items) else None

    def process_items_csv(self, path):
        items = self.ut.open_csv_file(path)[0]
        return items if len(items) else None
    
    def process_by_types(self, path, types):
        data = self.cm.open_file(path)

        if not data:
            return None

        _, ext = self.cm.path_splitext(path)

        if ext == '.txt' and ext in types:
            return self.process_items_txt(data)
        
        elif ext == '.json' and ext in types:
            return self.process_items_json(data)

        elif ext == '.csv' and ext in types:
            return self.process_items_csv(path)

        else:
            return None
    
    def thread(self, configs):
        return threading.Thread(**configs)
    
    def asksaveas(self, filetypes, defaultext):

        options = []

        for type in filetypes:
            ftype_ext = f'*.{type}'
            ftype_name = f'{type}' + self.cm._t(' file')

            options.append((ftype_name,ftype_ext))

        return filedialog.asksaveasfilename(filetypes=options, defaultextension='.'+defaultext)

    def askopenfile(self, filetypes, defaultext, mode):

        all_ftypes = []
        options = []

        for type in filetypes:
            ftype_ext = f'*.{type}'
            ftype_name = f'{type}' + self.cm._t(' file')

            all_ftypes.append(ftype_ext)
            options.append((ftype_name,ftype_ext))

        options.insert(0, (self.cm._t('All allowed files'),all_ftypes))

        return filedialog.askopenfile(filetypes=options, defaultextension='.'+defaultext, mode=mode)
