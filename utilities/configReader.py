from configparser import ConfigParser

def read_configuration(category,key):
    config = configparser()
    config.read("configurations/config.ini")
    return config.get(category,key)