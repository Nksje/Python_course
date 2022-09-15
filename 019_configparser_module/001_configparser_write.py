from configparser import ConfigParser

config = ConfigParser()

config['DEFAULT'] = {
    'login': 'MyLogin',
    'pass': 'MyPass'
}

config['EMAIL'] = {
    'email': 'python@mrartful.com',
    'email_pass': 'dsf342asda'
}

config['DATABASE'] = {
    'name': 'db_name',
    'pass': 'db_pass',
    'host': 'localhost'
}

with open('config.ini', 'w') as configfile:
    config.write(configfile)