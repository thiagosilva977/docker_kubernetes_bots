import sys
import json
with open('config/config.json','r') as myfile:
    CONFIG = json.load(myfile)
sys.path.append(CONFIG['main_path'])

if __name__ == '__main__':
    print('Inicializando código de bot 2')
    print('Algum texto a ser exibido')
