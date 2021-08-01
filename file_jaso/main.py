#target dir
import os
import unicodedata

def scan_folder(target_dir):

    entries = os.listdir(target_dir)
    for entry in entries:
        print(entry)
        uni_entry = unicodedata.normalize('NFC', entry)
        os.rename(target_dir + '/'+ entry, target_dir + '/' + uni_entry)
        print(uni_entry)
        if os.path.isfile(target_dir + '/' + uni_entry) == False:
            scan_folder(target_dir + '/' + uni_entry)

if __name__ == '__main__':
    target_dir = 'D:\\...'
    scan_folder(target_dir)
