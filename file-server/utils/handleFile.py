import os
import json
from datetime import datetime
from config import settings

def get_date():
    return datetime.today().strftime('%Y-%m-%d_%H:%M:%S')

def handleFile(data):
    if not os.path.exists(settings.CURRENT_FILE):
        with open(settings.CURRENT_FILE, 'w') as f:
            f.write('{}')

    print('Comparing with previously generated file.')
    with open(settings.CURRENT_FILE) as current_file:
        current_json = json.load(current_file)

    if data == current_json:
        print('No change.  Ignoring.')
        return -1
    else:
        print('Archiving previously generated file')
        newfilename = f'{settings.FILENAME}_{get_date()}'
        os.rename(settings.CURRENT_FILE, f'{settings.ARCHIVE_DIRECTORY}/{newfilename}')
        print(f'Previous file stored at {newfilename}')
        
    print('Storing new one')    
    with open(settings.CURRENT_FILE, 'w') as file:
        json.dump(data, file)

    print('Saved new file to ' + settings.CURRENT_FILE)
    
    return 1