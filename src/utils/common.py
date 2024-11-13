from src.config.app import AppConfig
from src.helpers.ctkinter_helpers import CTkinterHelpers as ctkh

import os, json, time, webbrowser, uuid

class CommonFunctions:

    def __init__(self):
        
        self.ctkh = ctkh()
    
    def get_attr(self, attr):
        return AppConfig.get_attr(attr)
    
    def get_attr_key(self, attr, key):
        attributes = self.get_attr(attr)
        return attributes.get(key, None)

    def set_attr_key(self, attr, key, val):
        AppConfig.app[attr][key] = val

    def update_attr(self, attr, val):
        AppConfig.app[attr] = val

    def update_attr_key(self, attr, key, val):
        AppConfig.app[attr][key].update(val)

    def lang(self, key):
        language = self.get_attr('language')
        language_dict = language.get('dict', None)
        return language_dict.get(key, key)

    def _t(self, text):
        return self.lang(text)
    
    def get_attributes_by_type(self, type):
        return self.get_attributes().get(type, None)
    
    def get_attributes_by(self, keys=[]):

        attr = self.get_attributes()
        for k in keys:
            attr = attr.get(k, None)
            if not attr: break

        return attr

    def get_json(self, path):
        if self.path_exists(path):
            dict_data = self.open_file(path)
            return json.loads(dict_data)

        return None
    
    def save_json(self, path, data):
        json_data = json.dumps(data)

        if self.save_file(path, json_data):
            return True
        
        else:
            return False  
    
    def save_file(self, path, data):
        abs_path = self.abspath(path)
        path_info = self.path_split(abs_path)

        if not self.path_exists(path_info[0]):
            self.mkdir(path_info[0], 755)

        with open(abs_path, 'w', encoding='UTF-8') as file:
            file.write(data)

            if self.path_exists(abs_path):
                return True
            else:
                return False

    def open_file(self, path):
        with open(path, 'r', encoding='UTF-8') as file:
            return file.read()

    def append_file(self, path, data):
        abs_path = self.abspath(path)
        path_info = self.path_split(abs_path)

        if not self.path_exists(path_info[0]):
            self.mkdir(path_info[0], 755)

        with open(abs_path, 'a', encoding='UTF-8') as file:

            if isinstance(data, list):

                for item in data:
                    file.write(f'{item}\n')

            else:
                file.write(f'{data}\n')

        True if self.path_exists(abs_path) else False

    def mkdir(self, path, mode=511, dir_fd=None):
        return os.mkdir(path, mode, dir_fd)

    def startfile(self, filepath):
        return os.startfile(filepath)

    def path_exists(self, path):
        return os.path.exists(path)
    
    def abspath(self, path):
        return os.path.abspath(path)
    
    def path_split(self, path):
        return os.path.split(path)
    
    def path_splitext(self, path):
        return os.path.splitext(path)
    
    def sleep(self, tme):
        time.sleep(tme)

    def get_current_language(self):
        return self.get_attr('language').get('default', None)
    
    def set_component_clear(self):
        AppConfig.app['components'][self.get_attr('viewport')] = {}

    def set_component_val_by_type(self, type, val):
        AppConfig.app['components'][self.get_attr('viewport')][type] = val

    def set_component_val_by_name(self, type, name, val):
        AppConfig.app['components'][self.get_attr('viewport')][type][name] = val

    def update_component_val_by_name(self, type, name, val):
        AppConfig.app['components'][self.get_attr('viewport')][type][name].update(val)

    def set_email_config(self, conf, val):
        AppConfig.app['email_config'][conf] = val

    def update_email_conf(self, conf, val):
        AppConfig.app['email_config'][conf].update(val)

    def truncate(self, limit, txt):
        return txt[:limit] + '...' if len(txt) >= limit else txt 
    
    def get_basename(self, path):
        return os.path.basename(path)
    
    def get_email_config(self, conf):
        if conf in self.get_attr('email_config'):
            return self.get_attr('email_config')[conf]

        return None
    
    def get_font(self, key):
        if key in self.get_attributes_by_type('font'):
            font_config = self.get_attributes_by_type('font')[key]
            return self.ctkh.generate_font(font_config['family'], font_config['size'])

        return None
    
    def get_config(self, key):
        return self.get_attributes_by_type('config')[key]
    
    def get_color(self, key):
        return self.get_attributes_by_type('color')[key]
    
    def get_path(self, type, key):
        return self.get_attributes_by_type('path')[type][key]
    
    def has_components_in_viewport(self):
        return True if self.get_attr('viewport') in self.get_attr('components') else False

    def get_component(self, type, name):
        return self.get_components_by_type(type).get(name, None)
        
    def get_component_key(self, type, name, key):
        widget = self.get_component(type, name)
        if key in widget:
            return widget[key]
        
        return None

    def get_components(self, viewport=False):
        current_viewport = self.get_attr('viewport')

        if viewport:           
            return self.get_attr_key('components',current_viewport)
        
        else: 
            return self.get_attr('components')

    def get_components_in_viewport(self):
        return self.get_components(True)
    
    def get_all_components(self):            
        if self.has_components_in_viewport():
            return self.get_components_in_viewport()
        
        return None
    
    def get_components_by_type(self, type):
        if self.has_components_in_viewport() and type in self.get_components_in_viewport():
            components = self.get_components_in_viewport()
            return components[type]
        
        return None
    
    def get_component_by_name(self, name, key=None):
        components = self.get_all_components()
        found = None
        for type in components.keys():
            if name in components[type]:
                found = components[type][name]

                if key and key in found:
                    found = found[key]
                
                break

        return found  
    
    def get_attributes(self):
        return self.get_attr('attributes')
    
    def open_link(self, link):
        webbrowser.open(link)

    def set_send_status(self, status):
        AppConfig.app['send'] = {'status':status, 'id':self.get_uniq()}

    def get_send_status(self):
        return self.get_attr_key('send','status')
    
    def get_send_id(self):
        return self.get_attr_key('send','id')
    
    def get_uniq(self):
        return uuid.uuid4().hex   
    
    def get_component_master(self, config):

        if config['master'] == 'interface':
            config['master'] = self.get_attr('interface')
            return config        
       
        if isinstance(config['master'], dict) and 'type' in config['master'] and 'name' in config['master']:            
            config['master'] = self.get_component_key(config['master']['type'], config['master']['name'], 'widget')
            return config
        
        return config