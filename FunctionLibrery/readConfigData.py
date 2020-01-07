import configparser

def readTestData(section, key):
    config = configparser.ConfigParser()
    config.read("..\ConfigFiles\TestData.cfg")
    return config.get(section,key)
def readLocatersData(section,key):
    config = configparser.ConfigParser()
    config.read("..\ConfigFiles\Locaters.cfg")
    return config.get(section,key)

#print(readLocatersData('LoginPage','UserID_Name'))