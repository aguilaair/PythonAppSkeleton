import time
import urllib.request
import os.path
import zipfile
import hashlib

# Variables

config_pname: str = 'My App'
config_pkg = 'doesn\'t'
config_wb = 'aguilaair.tech'
is_enc = True
enc_hash = '4813494d137e1631bba301d5acab6e7bb7aa74ce1185d456565ef51d737677b2'
target_file = 'https://aguilaair.tech/skeleton.zip'

print(f'''


          _____                _____                    _____                    _____                    _____          
         /\    \              |\    \                  /\    \                  /\    \                  /\    \         
        /::\____\             |:\____\                /::\    \                /::\    \                /::\    \        
       /::::|   |             |::|   |               /::::\    \              /::::\    \              /::::\    \       
      /:::::|   |             |::|   |              /::::::\    \            /::::::\    \            /::::::\    \      
     /::::::|   |             |::|   |             /:::/\:::\    \          /:::/\:::\    \          /:::/\:::\    \     
    /:::/|::|   |             |::|   |            /:::/__\:::\    \        /:::/__\:::\    \        /:::/__\:::\    \    
   /:::/ |::|   |             |::|   |           /::::\   \:::\    \      /::::\   \:::\    \      /::::\   \:::\    \   
  /:::/  |::|___|______       |::|___|______    /::::::\   \:::\    \    /::::::\   \:::\    \    /::::::\   \:::\    \  
 /:::/   |::::::::\    \      /::::::::\    \  /:::/\:::\   \:::\    \  /:::/\:::\   \:::\____\  /:::/\:::\   \:::\____\ 
/:::/    |:::::::::\____\    /::::::::::\____\/:::/  \:::\   \:::\____\/:::/  \:::\   \:::|    |/:::/  \:::\   \:::|    |
\::/    / ~~~~~/:::/    /   /:::/~~~~/~~      \::/    \:::\  /:::/    /\::/    \:::\  /:::|____|\::/    \:::\  /:::|____|
 \/____/      /:::/    /   /:::/    /          \/____/ \:::\/:::/    /  \/_____/\:::\/:::/    /  \/_____/\:::\/:::/    / 
             /:::/    /   /:::/    /                    \::::::/    /            \::::::/    /            \::::::/    /  
            /:::/    /   /:::/    /                      \::::/    /              \::::/    /              \::::/    /   
           /:::/    /    \::/    /                       /:::/    /                \::/____/                \::/____/    
          /:::/    /      \/____/                       /:::/    /                  ~~                       ~~          
         /:::/    /                                    /:::/    /                                                        
        /:::/    /                                    /:::/    /                                                         
        \::/    /                                     \::/    /                                                          
         \/____/                                       \/____/                                                           
                                                                                                                         


Hello and welcome to the installer for {config_pname} this is a python program which {config_pkg} require packages.
 We are going to install on you system: 
 - Package 1
 - Package 2
This installer was created by Aguilaair''')


def decrypt(passw):
    if hashlib.sha256(passw.encode()).hexdigest() == enc_hash:
        print('Password accepted!')
        passw_: bool = True
    else:
        print('Password rejected!')
        passw_: bool = False
    return passw_


def download(url: object, fname: object) -> object:
    if input('Do you wanna continue with the installation? (Y/n)') == 'Y':
        print('Thanks, lets proceed with the installation of {config_pname}!')
        # install software here
        # noinspection PyBroadException
        try:
            print('Downloading... ')
            urllib.request.urlretrieve(url, fname)
            print('Downloaded!')
            time.sleep(0.5)
            print('Checking file!')
            time.sleep(0.2)
            if os.path.isfile(fname):
                print('File found, continuing install.')
                filedl = True
            else:
                print('We wern\'t able to find the file!')
                print('Closing program in 3 seconds. Try reopening it to run the install')
                time.sleep(3)
                exit(1)
                filedl = False

        except Exception:
            print('We have had a problem retrieving the file...')
            print('We can try again but may fail, if you have tried already a few times check your internet and contact'
                  ' us at: ' + config_wb)
            print('Closing program in 3 seconds. Try reopening it to run the install')
            time.sleep(3)
            exit(1)
            filedl = False

    else:
        print('That\'s ok c\'ya on the next one! Closing in 3 seconds...')
        time.sleep(3)
        # noinspection PyUnreachableCode
        exit(0)
        filedl = False

    return filedl


def unzip(fname, pth2extract):
    if zipfile.is_zipfile(fname):
        print('Starting...')
        time.sleep(1)
        zip_ref = zipfile.ZipFile(fname, 'r')
        print('File opened')
        time.sleep(0.5)
        zip_ref.extractall(pth2extract)
        print('File extracted!')
        time.sleep(1)
        uz = True
    else:
        print('The zip file is corrupted, please try redownloading!')
        print('Closing program in 3 seconds. Try reopening it to run the download!')
        time.sleep(3)
        exit(1)
        uz = False

    return uz


if is_enc:
    if decrypt(input('This program is protected by a password, please enter it: ')):
        if download(target_file, 'program.zip'):
            if unzip('program.zip', './'):
                print('You can now use ' + config_pname)

        else:
            print('Closing program in 3 seconds. Try reopening it to run the install')
            time.sleep(3)
            exit(1)
    else:
        print('INCORRECT PASSWORD! Closing program in 3 seconds. Try reopening it to run the install')
        time.sleep(3)
        exit(1)
else:
    if download(target_file, 'program.zip'):
        if unzip('program.zip', './'):
            print('You can now use ' + config_pname)

        else:
            print('Closing program in 3 seconds. Try reopening it to run the install')
            time.sleep(3)
            exit(1)
    else:
        print('Unexpected error! Closing program in 3 seconds. Try reopening it to run the install')
        time.sleep(3)
        exit(1)
