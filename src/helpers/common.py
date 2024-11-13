from src.utils.common import CommonFunctions as cm
from src.helpers.helpers import HelperFunctions as hf
from src.helpers.ctkinter_helpers import CTkinterHelpers as ctkh

class CommonHelpers:

    def __init__(self):
        self.cm = cm()
        self.hf = hf()
        self.ctkh = ctkh()

    def log_send(self, data):
        log_path = self.cm.get_attributes_by(['path','log','default'])
        send_id = self.cm.get_send_id()
        filename = (send_id if send_id else '') + '_send.log'
        
        log_filepath = '/'.join([log_path,filename])
        self.cm.append_file(log_filepath, data)

    def background_frame(self):
        return self.ctkh.make_frame({'master':self.cm.get_attr('interface'), 'width':800, 'height':600, 'bg_color':'#000000', 'fg_color':self.cm.get_color('graffiti_grey'), 'corner_radius':0})

    def create_dialogbox(self):
        self.close_dialogbox()
        widget_config = {'master':self.cm.get_attr('interface'), 'bg_color':'transparent', 'fg_color':self.cm.get_color('theme'), 'corner_radius':10}
        widget = self.ctkh.make_frame(widget_config)
        self.set_component('dialogbox', 'dialogbox_frame', None, widget_config, widget)

    def create_label_message(self, message):
        widget_config = {'master':self.cm.get_component_key('dialogbox', 'dialogbox_frame', 'widget'), 'text':message, 'font':self.cm.get_font('open_sans_n16'), 'text_color':self.cm.get_color('message_text'), 'bg_color':self.cm.get_color('theme'), 'width':300, 'anchor':'center', 'justify':'center'}
        widget = self.ctkh.make_label(widget_config)
        self.set_component('dialogbox', 'message_label', None, widget_config, widget)

    def create_close_button(self):
        widget_config = {'master':self.cm.get_component_key('dialogbox', 'dialogbox_frame', 'widget'), 'text':'Fechar', 'font':self.cm.get_font('open_sans_n14'), 'text_color':self.cm.get_color('btn_text_alt'), 'bg_color':self.cm.get_color('theme'), 'fg_color':self.cm.get_color('dark_grey'), 'hover_color':self.cm.get_color('hover'), 'corner_radius':100, 'width':70, 'height':30}
        widget = self.ctkh.make_button(widget_config)
        self.set_component('dialogbox', 'btn_close', None, widget_config, widget)

    def show_message(self, message, close=True):
        self.create_dialogbox()
        self.create_label_message(message)

        self.ctkh.place(self.cm.get_component_key('dialogbox', 'dialogbox_frame', 'widget'), {'relx':0.5, 'rely':0.5, 'anchor':'center'})

        if close:
            self.create_close_button()
            self.ctkh.configure(self.cm.get_component_key('dialogbox', 'btn_close', 'widget'), {'command':self.close_dialogbox})
            self.ctkh.pack(self.cm.get_component_key('dialogbox', 'btn_close', 'widget'), {'pady':5, 'padx':5, 'anchor':'e'})

        self.ctkh.pack(self.cm.get_component_key('dialogbox', 'message_label', 'widget'), {'pady':(20, 50), 'padx':20, 'anchor':'center'})
        self.cm.sleep(1)

    def set_template_file(self, path):
        if self.cm.path_exists(path):
            self.cm.set_email_config('template',{'path':path})
            filename_tiny = self.cm.truncate(20, self.cm.get_basename(self.hf.get_template_path()))
            self.ctkh.configure(self.get_button_key('btn_load_template', 'widget'), {'text':filename_tiny})

            self.enable_elem('btn_view')

        return False

    def close_dialogbox(self):
        if self.cm.get_components_by_type('dialogbox'):
            for key, value in self.cm.get_components_by_type('dialogbox').items():
                self.ctkh.destroy(value['widget'])

            self.drop_components('dialogbox')

    def mark_email_send(self, widget):
        self.ctkh.configure(widget, {'font':self.cm.get_font('open_sans_eb14'),'text_color':self.cm.get_color('text_success')})

    def update_sent_total(self):
        count = len(self.cm.get_email_config('sent_emails'))
        self.ctkh.configure(self.get_label_key('total_sent_number','widget'), {'text':count})

    def update_duplicate_total(self):
        self.ctkh.configure(self.get_label_key('total_duplicate_number', 'widget'), {'text':len(self.cm.get_email_config('duplicate_recipients'))})

    def update_recipients_total(self):
        count = len(self.cm.get_email_config('recipient_list'))
        self.ctkh.configure(self.get_label_key('total_recipients_number', 'widget'), {'text':count})

    def disable_list_tools(self):        
        self.toggle_deselect_all()
        self.disable_search_entry()

    def disable_search_entry(self):
        self.get_entry_key('search_entry','widget').delete('0', 'end')

    def toggle_selected_tools(self):

        if self.has_recipient_selected():
            self.enable_elems([
                                'btn_deselect_all',
                                'btn_export_selection',
                                'btn_delete_selected'
                            ])

        else:
            self.disable_elems([
                                'btn_deselect_all',
                                'btn_export_selection',
                                'btn_delete_selected'
                            ])
           
    def toggle_recipients_tools(self):

        if self.has_recipients_in_list():
            self.enable_elems([
                                'btn_send',
                                'search_entry',
                                'btn_clear_list',
                                'btn_search',
                                'btn_select_duplicated',
                                'btn_export_list',
                                'btn_select_all'
                            ])

        else:
            self.disable_elems([
                                'btn_send',
                                'search_entry',
                                'btn_clear_list',
                                'btn_search',
                                'btn_select_duplicated',
                                'btn_export_list',
                                'btn_select_all'
                            ])
            
            self.replace_component('recipients_scrollable_frame')

    def has_recipient_selected(self):
        return True if len(self.cm.get_email_config('selected_recipients')) else False

    def has_recipients_in_list(self):
        return True if len(self.cm.get_email_config('recipient_list')) else False

    def get_entry_key(self, name, key):
        return self.cm.get_component_key('entries', name, key)

    def disable_elems(self, keylist):
        for key in keylist:
            self.disable_elem(key)

    def disable_elem(self, name):
        elem = self.cm.get_component_by_name(name, 'widget')
        self.disable_state(elem)

    def disable_state(self, elem):
        if elem.cget('state') == 'normal':
            self.ctkh.configure(elem, {'state':'disabled'})

    def enable_elems(self, keylist):
        for key in keylist:
            self.enable_elem(key)

    def enable_elem(self, name):
        elem = self.cm.get_component_by_name(name, 'widget')
        self.enable_state(elem)

    def enable_state(self, elem):
        if elem.cget('state') == 'disabled':
            self.ctkh.configure(elem, {'state':'normal'})        

    def toggle_elems(self, keylist):
        for key in keylist:
            self.toggle_elem(key)

    def toggle_elem(self, key):
        elem = self.cm.get_component_by_name(key, 'widget')

        if elem.cget('state') == 'disabled':
            self.enable_state(elem)

        else:
            self.disable_state(elem)

    def replace_component(self, name):
        component = self.cm.get_component_by_name(name)
        
        if component:

            # remove
            self.ctkh.forget(component['widget'])
            self.ctkh.destroy(component['widget'])

            # make new
            self.reset_component_by_name(name)
            self.render_element(component)

    def make_components(self, type, config):
        config = self.cm.get_component_master(config)

        match(type):

            case 'frames':
                return self.ctkh.make_frame(config)
            
            case 'scrollable_frames':
                return self.ctkh.make_scrollabel_frame(config)
            
            case 'buttons':
                return self.ctkh.make_button(config)
            
            case 'labels':
                return self.ctkh.make_label(config)
                        
            case 'entries':
                return self.ctkh.make_entry(config)

            case 'checkboxes':
                return self.ctkh.make_checkbox(config)
            
            case 'textboxes':
                return self.ctkh.make_textbox(config)
            
        return None

    def render_elements(self, widgets):
        if len(widgets):
            for name in widgets:
                self.render_element(widgets[name])

    def render_element(self, widget):
        if widget:

            if 'type' in widget['position'] and 'config' in widget['position']:

                if widget['position']['type'] == 'place':
                    self.ctkh.place(widget['widget'],widget['position']['config'])
                
                else:
                    self.ctkh.pack(widget['widget'],widget['position']['config'])

    def render_by_name(self, name):
        component = self.cm.get_component_by_name(name)
        if component:
            self.render_elements(component['widget'])
            
    def render_by_type(self, type):       
        if self.cm.has_components_in_viewport() and type in self.cm.get_components_in_viewport() and len(self.cm.get_components_by_type(type)):
            self.render_elements(self.cm.get_components_by_type(type))

    def render_viewport_components(self):
        if self.cm.has_components_in_viewport() and len(self.cm.get_components_in_viewport()):
            for type in self.cm.get_components_in_viewport().keys():
                self.render_by_type(type)

    def clear_entry(self, key):
        self.ctkh.delete(self.get_entry_key(key, 'widget'))

    def set_component(self, type, name, position, config, comp=None):

        if not self.cm.has_components_in_viewport():
            self.cm.set_component_clear()

        if not self.cm.get_components_by_type(type):
            self.cm.set_component_val_by_type(type, {})
        
        if not self.cm.get_component_by_name(name):
            self.cm.set_component_val_by_name(type, name, {})

        if not comp:
            comp = self.make_components(type, config)

        self.cm.update_component_val_by_name(type, name, {'type':type, 'config': config, 'position': position, 'widget': comp})

    def set_frame(self, name, position, config, comp=None):
        return self.set_component('frames', name, position, config, comp)
    
    def set_scrollable_frame(self, name, position, config, comp=None):
        return self.set_component('scrollable_frames', name, position, config, comp)
    
    def set_button(self, name, position, config, comp=None):
        return self.set_component('buttons', name, position, config, comp)
    
    def set_entry(self, name, position, config, comp=None):
        return self.set_component('entries', name, position, config, comp)
        
    def set_label(self, name, position, config, comp=None):
        return self.set_component('labels', name, position, config, comp)
            
    def set_textbox(self, name, position, config, comp=None):
        return self.set_component('textboxes', name, position, config, comp)
    
    def reset_component_by_name(self, name):
        component = self.cm.get_component_by_name(name)
        
        if component:
            self.reset_component(name, component['type'], component['position'], component['config'])

    def reset_component(self, name, type, position, config):        
        self.set_component(type, name, position, config, None)

    def set_textbox(self, name, position, config, comp=None):
        return self.set_component('textboxes', name, position, config, comp)
    
    def set_checkboxe(self, name, position, config, comp=None):
        return self.set_component('checkboxes', name, position, config, comp)

    def get_frame_key(self, name, key):
        return self.cm.get_component_key('frames', name, key)
    
    def get_scrollable_frame_key(self, name, key):
        return self.cm.get_component_key('scrollable_frames', name, key)
    
    def get_checkboxe_key(self, name, key):
        return self.cm.get_component_key('checkboxes', name, key)
        
    def get_textbox_key(self, name, key):
        return self.cm.get_component_key('textboxes', name, key)
    
    def get_label_key(self, name, key):
        return self.cm.get_component_key('labels', name, key)
    
    def get_button_key(self, name, key):
        return self.cm.get_component_key('buttons', name, key)
    
    def get_button(self, name):
        return self.cm.get_component('buttons', name)
    
    def get_entry(self, name):
        return self.cm.get_component('entries', name)
        
    def get_label(self, name):
        return self.cm.get_component('labels', name)
    
    def get_checkboxe(self, name):
        return self.cm.get_component('checkboxes', name)
    
    def drop_component(self, type, name):
        self.cm.get_components_by_type(type).pop(name, None)
    
    def drop_components(self, type):
        self.cm.get_components_in_viewport().pop(type, None)

    def drop_frame(self, name):
        return self.drop_component('frames', name)
    
    def drop_scrollable_frame(self, name):
        return self.drop_component('scrollable_frames', name)
    
    def drop_button(self, name):
        return self.drop_component('buttons', name)
    
    def drop_entry(self, name):
        return self.drop_component('entries', name)
    
    def drop_label(self, name):
        return self.drop_component('labels', name)
    
    def drop_checkboxe(self, name):
        return self.drop_component('checkboxes', name)
    
    def drop_textboxes(self, name):
        return self.drop_component('textboxes', name)
