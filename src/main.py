"""
Filename: main.py
Description: Bulk email sending with Twilio SendGrid®
Author: Gustavo Alves
Date: 2024-01-11
Site: https://github.com/guztavoalves
Version: 1.0.0
"""
__version__ = "1.0.0"

from src.config.app import AppConfig

import src.config.tkinter as tkc
import src.config.email as emc
import src.config.attributes as attr

from src.utils.common import CommonFunctions as cm
from src.utils.utils import UtilsFunctions as ut
from src.controllers.language_manager import LanguageManager as lm

import src.views.main_viewport as main_view

import customtkinter as ctk

class App:

    def __init__(self):

        self.cm = cm()
        self.ut = ut()
        self.lm = lm()
        
        self.init_email_config()
        self.init_attributes()
        self.init_interface()
        self.init_i18n()

    def init_interface(self):
        self.tkc = tkc.TKinterConfig()
        AppConfig.app['interface'] = ctk.CTk()

        window_size = self.tkc.interface_config['window_size']
        window_resizeble = self.tkc.interface_config['resizable']
        grid_colum = self.tkc.interface_config['grid_columnconfigure']
        icon_file = '/'.join([self.cm.get_attributes_by(['path','icon','default']), self.tkc.interface_config['icon']])

        self.cm.get_attr('interface').iconbitmap(icon_file)
        self.cm.get_attr('interface').geometry(f'{window_size[0]}x{window_size[1]}')
        self.cm.get_attr('interface').resizable(window_resizeble[0], window_resizeble[1])
        self.cm.get_attr('interface').grid_columnconfigure(grid_colum[0], weight=grid_colum[1])

    def init_i18n(self):
        self.lm.set_language_dict()

    def init_email_config(self):
        email_configurations = emc.EmailConfig()
        AppConfig.app['email_config'] = email_configurations.email_config
    
    def init_attributes(self):
        attributes_configurations = attr.AttributesConfig()
        AppConfig.app['attributes'] = attributes_configurations.attributes

    def init_viewport(self, viewport):
        AppConfig.app['viewport'] = viewport
        self.load_view()

    def init_interface_listener(self):
        self.cm.get_attr('interface').mainloop()

    def load_view(self):
        if self.ut.is_viewport('main'):
            self.view = main_view.MainView()
        else:
            exit()

    def main(self, viewport):

        # Init viewport
        self.init_viewport(viewport)
        
        # Make current Viewport
        self.view.make()

        # Init
        self.init_interface_listener()