import json
import requests

blue_color = '\033[1;34;40m'
red_color = '\033[1;31;40m'
green_color = '\033[1;32;40m'


print(""" {}
 ____                  _     _       _        
/ ___|  __ ___   _____| |   (_)_ __ | | _____ 
\___ \ / _` \ \ / / _ \ |   | | '_ \| |/ / __|
 ___) | (_| |\ V /  __/ |___| | | | |   <\__ S
|____/ \__,_| \_/ \___|_____|_|_| |_|_|\_\___/
            {}                By: @PauloTheDev     
{}===============================================
""".format(blue_color,red_color, blue_color))


input_title = str(input('{}What will be the title?:{} '.format(red_color,blue_color)))

input_desc = str(input('{}Tell more about this website. Give us a description:{} '.format(red_color,blue_color)))

input_link = str(input('{}And now, the link:{}'.format(red_color,blue_color)))


def write_json(data,filename='src/data.json'):
    with open('src/data.json', 'w') as file:
        json.dump(data,file,indent=4)

    # This function will do the insert of new content

def site_check_status(link):
    request = requests.get(link)

    if request.status_code != 200:
        
        proceed_or_not = str(input("That site seems don't work. Do you really want save it? ").lower())
        
        if proceed_or_not == 'y' or proceed_or_not == 'yes':
            write_json(data)
            print('{}Your new link was saved'.format(green_color))

        else:
            print('{}Closing the application...'.format(red_color))
   
    else:
        write_json(data)
        print('{}Your new link was saved'.format(green_color))
    # This function will verificate if site works correctly

with open ('src/data.json') as json_file:
    data = json.load(json_file)
    area = data['savedlinks']
    
    new_data = {"title": input_title, "desc":input_desc, "link":input_link }
    
    area.append(new_data)
    
    # This with statement will set new contents 

    site_check_status(input_link)
