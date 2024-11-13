class AttributesConfig:

    def __init__(self):

        self.attributes = {
                            'config':{
                                    'rcp_limit':1000
                            },
                            'color': {
                                    'theme':'#FFC653',
                                    'bg_btn_disabled':'#303030',
                                    'bg_btn_remove':'#7C3239',
                                    'bg_btn_attention':'#7C3239',
                                    'bg_disabled':'#303030',                
                                    'text_disabled':'#6A6A6A',
                                    'labels':'#ffffff',
                                    'btn_text':'#000000',
                                    'btn_text_alt':'#ffffff',
                                    'hover':'#8C6A44',
                                    'titles':'#ffffff',
                                    'input_text':'#ffffff',
                                    'number_count':'#ffffff',
                                    'dark_grey':'#282828',
                                    'graffiti_grey':'#373737',
                                    'list_item':'#ffffff',
                                    'bg_list_item':'#444444',
                                    'bg_list_success':'#3C4D44',
                                    'text_success':'#B5FFB9',
                                    'text_subtitle':'#ffffff',
                                    'black_grey':'#1D1D1D',
                                    'bg_title':'#1D1D1D',
                                    'window_bg':'#000000',
                                    'version':'#ffffff',
                                    'message_text': '#000000',
                                    'soft_text': '#6C6C6C'
                                },
                            'font' : {
                                    'open_sans_eb34': {'family': 'Open Sans Extrabold', 'size':34},
                                    'open_sans_n22': {'family': 'Open Sans', 'size':22},
                                    'open_sans_n18': {'family': 'Open Sans', 'size':18},
                                    'open_sans_n16': {'family': 'Open Sans', 'size':16},
                                    'open_sans_n14': {'family': 'Open Sans', 'size':14},
                                    'open_sans_eb14': {'family': 'Open Sans Extrabold', 'size':14},
                                    'open_sans_n12': {'family': 'Open Sans', 'size':12}
                                },
                            'path' : {
                                    'conf': {
                                            'user':'settings/email_setup.json'
                                        },
                                    'languages': {
                                            'en':'src/i18n/en.json',
                                            'pt_br':'src/i18n/pt_br.json',
                                        },
                                    'log': {
                                            'default':'log'
                                        },
                                    'icon': {
                                            'default':'static'
                                        }
                                },
                            'author' : {
                                    'link': {
                                            'github':'https://github.com/guztavoalves'
                                        },
                                },
                        }