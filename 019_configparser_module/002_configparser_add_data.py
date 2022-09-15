from configparser import ConfigParser

config = ConfigParser()
config.read('config.ini')

# sections prints all sections of config file except default
print(config.sections())

# Each section can be accessed by indexing it
print(config['EMAIL'])
print(list(config['EMAIL']))

# Every data can be accessed by indexing section and then indexing setting
print(config['EMAIL']['email_pass'])

config.add_section('NEWLOGIN')
config.set('NEWLOGIN', 'login', 'new_login')
config.set('NEWLOGIN', 'pass', 'new_pass')

with open('config.ini', 'w') as configfile:
    config.write(configfile)
