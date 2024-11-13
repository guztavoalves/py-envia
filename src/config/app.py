class AppConfig:

    app = {
            'interface' : None,
            'viewport' : '',
            'version' : '1.0.0',
            'language' : {'default': 'en', 'dict': {}},
            'components' : {},
            'attributes' : {},
            'email_config' : {},
            'send' : {},
        }

    @classmethod
    def get_configs(cls):
        return cls.app

    @classmethod
    def get_attr(cls, attr):
        return cls.app.get(attr, None)
        
    @classmethod
    def update_attr(cls, attr, val):
        cls.app[attr] = val
