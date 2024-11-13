from src.utils.common import CommonFunctions as cm
from src.helpers.common import CommonHelpers as cmhp

from src.helpers.interface_helpers import InterfaceHelpers as ihp
from src.helpers.ctkinter_helpers import CTkinterHelpers as ctkh

from src.controllers.config_loader import ConfigLoader as cfl
from src.controllers.command_manager import CommandManager as cman

class MainView:

    def __init__(self):
        self.cm = cm()
        self.cmhp = cmhp()
        self.ihp = ihp()
        self.ctkh = ctkh()
        self.cfl = cfl()
        self.cman = cman()

    def register_components(self):

        # FRAME COMPONENTS
        self.cmhp.set_frame('left', {'type':'place', 'config':{'x':0, 'y':0}}, {'master':'interface', 'width':340, 'height':600, 'fg_color':self.cm.get_color('dark_grey'), 'bg_color':self.cm.get_color('dark_grey')})
        self.cmhp.set_frame('right', {'type':'place', 'config':{'x':340, 'y':0}}, {'master':'interface', 'width':460, 'height':600, 'fg_color':self.cm.get_color('graffiti_grey'), 'bg_color':self.cm.get_color('graffiti_grey')})
        self.cmhp.set_frame('recipients', {'type':'place', 'config':{'x':360, 'y':20}}, {'master':'interface', 'width':270, 'height':560, 'fg_color':self.cm.get_color('dark_grey'), 'bg_color':self.cm.get_color('graffiti_grey'), 'corner_radius':10})
        self.cmhp.set_frame('box_total_recipients', {'type':'place', 'config':{'x':650, 'y':20}}, {'master':'interface', 'width':130, 'height':90, 'fg_color':self.cm.get_color('dark_grey'), 'bg_color':self.cm.get_color('graffiti_grey'), 'corner_radius':10})
        self.cmhp.set_frame('box_total_duplicated', {'type':'place', 'config':{'x':650, 'y':120}}, {'master':'interface', 'width':130, 'height':90, 'fg_color':self.cm.get_color('dark_grey'), 'bg_color':self.cm.get_color('graffiti_grey'), 'corner_radius':10})
        self.cmhp.set_frame('box_configuration_title', {'type':'place', 'config':{'x':20, 'y':120}}, {'master':'interface', 'width':300, 'height':40, 'fg_color':self.cm.get_color('bg_title'), 'bg_color':self.cm.get_color('dark_grey'), 'corner_radius':5})
        self.cmhp.set_frame('box_sent', {'type':'place', 'config':{'x':20, 'y':550}}, {'master':'interface', 'width':300, 'height':30, 'corner_radius':5, 'fg_color':self.cm.get_color('dark_grey'), 'bg_color':self.cm.get_color('dark_grey'), 'border_color':self.cm.get_color('theme'), 'border_width':1})
        self.cmhp.set_frame('info_total_recipients', {'type':'place', 'config':{'x':660, 'y':50}}, {'master':'interface', 'width':110, 'height':50, 'bg_color':self.cm.get_color('dark_grey'), 'fg_color':self.cm.get_color('graffiti_grey'), 'corner_radius':5})
        self.cmhp.set_frame('info_total_duplicated', {'type':'place', 'config':{'x':660, 'y':150}}, {'master':'interface', 'width':110, 'height':50, 'bg_color':self.cm.get_color('dark_grey'), 'fg_color':self.cm.get_color('graffiti_grey'), 'corner_radius':5})
        
        # SCROLLABLE FRAME COMPONENTS
        self.cmhp.set_scrollable_frame('recipients_scrollable_frame', {'type':'pack', 'config':{'pady':125, 'padx':10, 'anchor':'center'}}, {'master':{'type':'frames','name':'recipients'}, 'width':230, 'height':320, 'bg_color':self.cm.get_color('dark_grey'), 'fg_color':self.cm.get_color('graffiti_grey')})
        
        # Textbox
        #self.cmhp.set_textbox('recipients_textbox', {'type':'pack', 'config':{'pady':125, 'padx':10, 'anchor':'center'}}, {'master':{'type':'frames','name':'recipients'}, 'wrap': None, 'state':'disabled', 'width':250, 'height':330, 'text_color':self.cm.get_color('input_text'), 'font':self.cm.get_font('open_sans_n12'), 'bg_color':self.cm.get_color('dark_grey'), 'fg_color':self.cm.get_color('graffiti_grey')})

        # LABEL COMPONENTS
        self.cmhp.set_label('title_app', {'type':'place', 'config':{'x':20, 'y':10}}, {'master':'interface', 'text':self.cm._t('PyEnvia'),'text_color':self.cm.get_color('theme'), 'font':self.cm.get_font('open_sans_eb34'), 'bg_color':self.cm.get_color('dark_grey'),'anchor':'w'})
        self.cmhp.set_label('subtitle_app', {'type':'place', 'config':{'x':20, 'y':60}}, {'master':'interface','text':self.cm._t('Bulk email sending with\nTwilio SendGrid®'),'text_color':self.cm.get_color('text_subtitle'),'font':self.cm.get_font('open_sans_n16'),'bg_color':self.cm.get_color('dark_grey'),'anchor':'w','justify':'left'})
        self.cmhp.set_label('title_configurations', {'type':'place', 'config':{'x':30, 'y':125}}, {'master':'interface', 'text':self.cm._t('Settings'), 'text_color':self.cm.get_color('titles'), 'font':self.cm.get_font('open_sans_n16'), 'bg_color':self.cm.get_color('bg_title'), 'anchor':'w'})
        self.cmhp.set_label('api_label', {'type':'place', 'config':{'x':20, 'y':180}}, {'master':'interface', 'text':self.cm._t('API Key'), 'font':self.cm.get_font('open_sans_n14'), 'anchor':'w', 'text_color':self.cm.get_color('labels'), 'bg_color':self.cm.get_color('dark_grey'), 'fg_color':self.cm.get_color('bg_title'), 'corner_radius':60, 'height': 25})
        self.cmhp.set_label('sender_label', {'type':'place', 'config':{'x':20, 'y':250}}, {'master':'interface', 'text':self.cm._t('Verified Sender by SendGrid®'), 'font':self.cm.get_font('open_sans_n14'), 'text_color':self.cm.get_color('labels'), 'anchor':'w', 'bg_color':self.cm.get_color('dark_grey'), 'fg_color':self.cm.get_color('bg_title'), 'corner_radius':60, 'height': 25})
        self.cmhp.set_label('subject_label', {'type':'place', 'config':{'x':20, 'y':320}}, {'master':'interface', 'text':self.cm._t('Subject'), 'font':self.cm.get_font('open_sans_n14'), 'text_color':self.cm.get_color('labels'), 'anchor':'w', 'bg_color':self.cm.get_color('dark_grey'), 'fg_color':self.cm.get_color('bg_title'), 'corner_radius':60, 'height': 25})
        self.cmhp.set_label('message_file_label', {'type':'place', 'config':{'x':20, 'y':390}}, {'master':'interface', 'text':self.cm._t('Message / html file'), 'font':self.cm.get_font('open_sans_n14'), 'text_color':self.cm.get_color('labels'), 'anchor':'w', 'bg_color':self.cm.get_color('dark_grey'), 'fg_color':self.cm.get_color('bg_title'), 'corner_radius':60, 'height': 25})
        self.cmhp.set_label('sent_label', {'type':'place', 'config':{'x':30, 'y':555}}, {'master':'interface', 'text':self.cm._t('Sent'), 'font':self.cm.get_font('open_sans_n14'), 'text_color':self.cm.get_color('labels'), 'anchor':'w', 'bg_color':self.cm.get_color('dark_grey'), 'height':14})
        self.cmhp.set_label('recipients_title_label', {'type':'place', 'config':{'x':380, 'y':30}}, {'master':'interface', 'text':self.cm._t('Recipients'), 'font':self.cm.get_font('open_sans_n18'), 'text_color':self.cm.get_color('titles'), 'anchor':'w', 'bg_color':self.cm.get_color('dark_grey')})
        self.cmhp.set_label('selected_label', {'type':'place', 'config':{'x':650, 'y':220}}, {'master':'interface', 'text':self.cm._t('Selected:'), 'font':self.cm.get_font('open_sans_n14'), 'text_color':self.cm.get_color('titles'), 'anchor':'w', 'bg_color':self.cm.get_color('graffiti_grey')})
        self.cmhp.set_label('delete_label', {'type':'place', 'config':{'x':650, 'y':390}}, {'master':'interface', 'text':self.cm._t('All:'), 'font':self.cm.get_font('open_sans_n14'), 'text_color':self.cm.get_color('titles'), 'anchor':'w', 'bg_color':self.cm.get_color('graffiti_grey')})
        self.cmhp.set_label('total_recipient_label', {'type':'place', 'config':{'x':650, 'y':25}}, {'master':'interface', 'text':self.cm._t('Total recipients'), 'font':self.cm.get_font('open_sans_n12'), 'text_color':self.cm.get_color('labels'), 'anchor':'center', 'bg_color':self.cm.get_color('dark_grey'), 'width':130, 'height':14})
        self.cmhp.set_label('total_recipients_label', {'type':'place', 'config':{'x':650, 'y':125}}, {'master':'interface', 'text':self.cm._t('Total duplicates'), 'font':self.cm.get_font('open_sans_n12'), 'text_color':self.cm.get_color('labels'), 'anchor':'center', 'bg_color':self.cm.get_color('dark_grey'), 'width':130, 'height':14})
        self.cmhp.set_label('version_label', {'type':'place', 'config':{'x':290, 'y':28}}, {'master':'interface', 'text':f"v{self.cm.get_attr('version')}", 'font':self.cm.get_font('open_sans_n12'), 'text_color':self.cm.get_color('version'), 'anchor':'w', 'bg_color':self.cm.get_color('dark_grey')})
        self.cmhp.set_label('total_recipients_number', {'type':'place', 'config':{'x':670, 'y':55}}, {'master':'interface', 'text':0, 'text_color':self.cm.get_color('number_count'), 'bg_color':self.cm.get_color('graffiti_grey'), 'fg_color':self.cm.get_color('graffiti_grey'), 'font':self.cm.get_font('open_sans_n14'), 'width':90, 'height':40, 'anchor':'center', 'justify':'center'})
        self.cmhp.set_label('total_duplicate_number', {'type':'place', 'config':{'x':670, 'y':155}}, {'master':'interface', 'text':0, 'text_color':self.cm.get_color('number_count'), 'bg_color':self.cm.get_color('graffiti_grey'), 'fg_color':self.cm.get_color('graffiti_grey'), 'font':self.cm.get_font('open_sans_n14'), 'width':90, 'height':40, 'anchor':'center', 'justify':'center'})
        self.cmhp.set_label('total_sent_number', {'type':'place', 'config':{'x':110, 'y':555}}, {'master':'interface', 'text':0, 'text_color':self.cm.get_color('number_count'), 'bg_color':self.cm.get_color('dark_grey'), 'fg_color':self.cm.get_color('dark_grey'), 'font':self.cm.get_font('open_sans_n14'), 'width':200, 'height':20, 'anchor':'e', 'justify':'right'})

        # ENTRY COMPONENTS
        self.cmhp.set_entry('api_key_entry', {'type':'place', 'config':{'x':20, 'y':210}}, {'master':'interface', 'fg_color':self.cm.get_color('graffiti_grey'), 'bg_color':self.cm.get_color('dark_grey'), 'text_color':self.cm.get_color('input_text'), 'corner_radius':5, 'width':300, 'height':35, 'border_width':0})
        self.cmhp.set_entry('sender_entry', {'type':'place', 'config':{'x':20, 'y':280}}, {'master':'interface', 'fg_color':self.cm.get_color('graffiti_grey'), 'bg_color':self.cm.get_color('dark_grey'), 'text_color':self.cm.get_color('input_text'), 'corner_radius':5, 'width':300, 'height':35, 'border_width':0})
        self.cmhp.set_entry('subject_entry', {'type':'place', 'config':{'x':20, 'y':350}}, {'master':'interface', 'fg_color':self.cm.get_color('graffiti_grey'), 'bg_color':self.cm.get_color('dark_grey'), 'text_color':self.cm.get_color('input_text'), 'corner_radius':5, 'width':300, 'height':35, 'border_width':0})
        self.cmhp.set_entry('search_entry', {'type':'place', 'config':{'x':370, 'y':65}}, {'master':'interface', 'state':'disabled', 'fg_color':self.cm.get_color('graffiti_grey'), 'bg_color':self.cm.get_color('dark_grey'), 'text_color':self.cm.get_color('input_text'), 'corner_radius':5, 'width':175, 'height':35, 'border_width':0})
        self.cmhp.set_entry('new_email_entry', {'type':'place', 'config':{'x':370, 'y':485}}, {'master':'interface', 'fg_color':self.cm.get_color('graffiti_grey'), 'bg_color':self.cm.get_color('dark_grey'), 'text_color':self.cm.get_color('input_text'), 'corner_radius':5, 'width':190, 'height':35, 'border_width':0})

        # BUTTON COMPONENTS
        self.cmhp.set_button('btn_insert_new_email', {'type':'place', 'config':{'x':565, 'y':485}}, {'master':'interface', 'command':self.cman.cmd_insert_new_recipient, 'text':self.cm._t('Register'), 'text_color':self.cm.get_color('btn_text'), 'text_color_disabled':self.cm.get_color('text_disabled'), 'bg_color':self.cm.get_color('graffiti_grey'), 'fg_color':self.cm.get_color('theme'), 'hover_color':self.cm.get_color('hover'), 'corner_radius':5, 'width':40, 'height':35})
        self.cmhp.set_button('btn_view', {'type':'place', 'config':{'x':240, 'y':420}}, {'master':'interface', 'command':self.cman.cmd_view_file, 'state':'disabled', 'text':self.cm._t('Preview'),'width':80, 'height':35, 'font':self.cm.get_font('open_sans_n12'), 'text_color':self.cm.get_color('btn_text'), 'text_color_disabled':self.cm.get_color('text_disabled'),  'bg_color':self.cm.get_color('dark_grey'), 'fg_color':self.cm.get_color('theme'), 'hover_color':self.cm.get_color('hover')})
        self.cmhp.set_button('btn_load_template', {'type':'place', 'config':{'x':20, 'y':420}}, {'master':'interface', 'command':self.cman.cmd_select_file, 'text':self.cm._t('Choose file...'), 'width':215, 'height':35, 'font':self.cm.get_font('open_sans_n14'), 'text_color':self.cm.get_color('btn_text_alt'), 'text_color_disabled':self.cm.get_color('text_disabled'), 'bg_color':self.cm.get_color('dark_grey'), 'fg_color':self.cm.get_color('graffiti_grey'), 'hover_color':self.cm.get_color('hover')})
        self.cmhp.set_button('btn_send', {'type':'place', 'config':{'x':20, 'y':475}}, {'master':'interface', 'command':self.cman.cmd_send, 'state':'disabled', 'text':self.cm._t('SEND'), 'width':170, 'height':55, 'font':self.cm.get_font('open_sans_n22'), 'text_color':self.cm.get_color('btn_text'), 'text_color_disabled':self.cm.get_color('text_disabled'), 'bg_color':self.cm.get_color('dark_grey'), 'fg_color':self.cm.get_color('theme'), 'hover_color':self.cm.get_color('hover')})
        self.cmhp.set_button('btn_stop', {'type':'place', 'config':{'x':195, 'y':475}}, {'master':'interface', 'command':self.cman.cmd_stop, 'state':'disabled', 'text':self.cm._t('STOP\nSENDING'), 'width':125, 'height':55, 'font':self.cm.get_font('open_sans_n14'), 'text_color':self.cm.get_color('btn_text'), 'text_color_disabled':self.cm.get_color('text_disabled'), 'bg_color':self.cm.get_color('dark_grey'), 'fg_color':self.cm.get_color('theme'), 'hover_color':self.cm.get_color('hover')})
        self.cmhp.set_button('btn_search', {'type':'place', 'config':{'x':550, 'y':65}}, {'master':'interface', 'command':self.cman.cmd_search, 'state':'disabled', 'text':self.cm._t('Search'), 'width':70, 'height':35, 'font':self.cm.get_font('open_sans_n12'), 'text_color':self.cm.get_color('btn_text'), 'text_color_disabled':self.cm.get_color('text_disabled'), 'bg_color':self.cm.get_color('dark_grey'), 'fg_color':self.cm.get_color('theme'), 'hover_color':self.cm.get_color('hover')})
        self.cmhp.set_button('btn_load_recipient_list', {'type':'place', 'config':{'x':370, 'y':530}}, {'master':'interface', 'command':self.cman.cmd_load_list_file, 'text':self.cm._t('Load list'), 'width':255, 'height':40, 'font':self.cm.get_font('open_sans_n12'), 'text_color':self.cm.get_color('btn_text'), 'text_color_disabled':self.cm.get_color('text_disabled'), 'corner_radius':10, 'bg_color':self.cm.get_color('graffiti_grey'), 'fg_color':self.cm.get_color('theme'), 'hover_color':self.cm.get_color('hover')})
        self.cmhp.set_button('btn_export_selection', {'type':'place', 'config':{'x':650, 'y':250}}, {'master':'interface', 'command':self.cman.cmd_export_selected, 'state':'disabled', 'text':self.cm._t('Export\nselected'), 'width':130, 'height':60, 'font':self.cm.get_font('open_sans_n14'), 'text_color':self.cm.get_color('btn_text'), 'text_color_disabled':self.cm.get_color('text_disabled'), 'fg_color':self.cm.get_color('theme'), 'bg_color':self.cm.get_color('graffiti_grey'), 'hover_color':self.cm.get_color('hover')})
        self.cmhp.set_button('btn_export_list', {'type':'place', 'config':{'x':650, 'y':420}}, {'master':'interface', 'command':self.cman.cmd_export_list, 'state':'disabled', 'text':self.cm._t('Export all'), 'width':130, 'height':40, 'font':self.cm.get_font('open_sans_n14'), 'text_color':self.cm.get_color('btn_text'), 'text_color_disabled':self.cm.get_color('text_disabled'), 'fg_color':self.cm.get_color('theme'), 'bg_color':self.cm.get_color('graffiti_grey'), 'hover_color':self.cm.get_color('hover')})
        self.cmhp.set_button('dev_label', {'type':'place', 'config':{'x':650, 'y':540}}, {'master':'interface', 'command':self.cman.cmd_open_dev_home, 'text':'\n'.join([self.cm._t('Developed by'),'@guztavoalves']), 'font':self.cm.get_font('open_sans_n12'), 'text_color':self.cm.get_color('soft_text'), 'anchor':'center',  'width':130, 'height':40, 'corner_radius':0, 'hover_color':self.cm.get_color('graffiti_grey'), 'bg_color':self.cm.get_color('graffiti_grey'), 'fg_color':self.cm.get_color('graffiti_grey')})
        self.cmhp.set_button('btn_select_duplicated', {'type':'place', 'config':{'x':370, 'y':110}}, {'master':'interface', 'command':self.cman.cmd_select_duplicated, 'state':'disabled', 'text':self.cm._t('Sel. duplicates'), 'width':95, 'height':30, 'font':self.cm.get_font('open_sans_n12'), 'text_color':self.cm.get_color('btn_text'), 'text_color_disabled':self.cm.get_color('text_disabled'), 'fg_color':self.cm.get_color('theme'), 'bg_color':self.cm.get_color('graffiti_grey'), 'hover_color':self.cm.get_color('hover')})
        self.cmhp.set_button('btn_select_all', {'type':'place', 'config':{'x':468, 'y':110}}, {'master':'interface', 'command':self.cman.cmd_select_all, 'state':'disabled', 'text':self.cm._t('Sel. all'), 'width':70, 'height':30, 'corner_radius':5, 'font':self.cm.get_font('open_sans_n12'), 'text_color':self.cm.get_color('btn_text'), 'text_color_disabled':self.cm.get_color('text_disabled'), 'fg_color':self.cm.get_color('theme'), 'bg_color':self.cm.get_color('graffiti_grey'), 'hover_color':self.cm.get_color('hover')})
        self.cmhp.set_button('btn_deselect_all', {'type':'place', 'config':{'x':540, 'y':110}}, {'master':'interface', 'command':self.cman.cmd_deselect_all, 'state':'disabled', 'text':self.cm._t('Desel. all'), 'width':80, 'height':30, 'corner_radius':5, 'font':self.cm.get_font('open_sans_n12'), 'text_color':self.cm.get_color('btn_text'), 'text_color_disabled':self.cm.get_color('text_disabled'), 'fg_color':self.cm.get_color('theme'), 'bg_color':self.cm.get_color('graffiti_grey'), 'hover_color':self.cm.get_color('hover')})
        self.cmhp.set_button('btn_save_configurations', {'type':'place', 'config':{'x':260, 'y':125}}, {'master':'interface', 'command':self.cman.cmd_save, 'text':self.cm._t('Save'), 'width':50, 'height':30, 'corner_radius':5, 'font':self.cm.get_font('open_sans_n14'), 'text_color':self.cm.get_color('btn_text'), 'text_color_disabled':self.cm.get_color('text_disabled'), 'fg_color':self.cm.get_color('theme'), 'bg_color':self.cm.get_color('graffiti_grey'), 'hover_color':self.cm.get_color('hover'), 'state':'disabled'})
        self.cmhp.set_button('btn_delete_selected', {'type':'place', 'config':{'x':650, 'y':320}}, {'master':'interface', 'command':self.cman.cmd_remove_selected, 'state':'disabled', 'text':self.cm._t('Delete\nselected'), 'width':130, 'height':60, 'font':self.cm.get_font('open_sans_n14'), 'text_color':self.cm.get_color('btn_text_alt'), 'text_color_disabled':self.cm.get_color('text_disabled'), 'fg_color':self.cm.get_color('bg_btn_remove'), 'bg_color':self.cm.get_color('graffiti_grey'), 'hover_color':self.cm.get_color('hover')})
        self.cmhp.set_button('btn_clear_list', {'type':'place', 'config':{'x':650, 'y':470}}, {'master':'interface', 'command':self.cman.cmd_clean_list, 'state':'disabled', 'text':self.cm._t('Delete all'), 'width':130, 'height':40, 'font':self.cm.get_font('open_sans_n14'), 'text_color':self.cm.get_color('btn_text_alt'), 'text_color_disabled':self.cm.get_color('text_disabled'), 'fg_color':self.cm.get_color('bg_btn_remove'), 'bg_color':self.cm.get_color('graffiti_grey'), 'hover_color':self.cm.get_color('hover')})
        self.cmhp.set_button('btn_clear_configurations', {'type':'place', 'config':{'x':200, 'y':125}}, {'master':'interface', 'width':50, 'height':30, 'text':self.cm._t('Reset'), 'command':self.cman.cmd_clear_config, 'text_color':self.cm.get_color('btn_text_alt'), 'bg_color':self.cm.get_color('dark_grey'), 'text_color_disabled':self.cm.get_color('text_disabled'), 'fg_color':self.cm.get_color('bg_btn_remove'), 'hover_color':self.cm.get_color('hover'), 'corner_radius':5})

    def make(self):
        self.cm.get_attr('interface').title(f"{self.cm._t('PyEnvia')} v{self.cm.get_attr('version')} | {self.cm._t('Bulk email sending.')}")
        self.ctkh.configure(self.cm.get_attr('interface'), {'fg_color':self.cm.get_color('window_bg')})

        # Register Viewport
        # Elements
        self.register_components()

        # Place All Viewport
        # Elements
        self.cmhp.render_viewport_components()

        # Get previous
        # User configurations saved
        self.cfl.load_config()

        self.cmhp.get_entry_key('search_entry', 'widget').bind('<KeyRelease>', self.ihp.auto_validate_email)

        self.cmhp.enable_elem('btn_save_configurations')
        self.cmhp.update_sent_total()