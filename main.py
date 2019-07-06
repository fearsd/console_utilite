__author__ = 'fearsd'

import os                # this module requires to get username and for start apps in open_command() 
from time import sleep   # sleep() requires into read_command()

class UserExit(KeyboardInterrupt):
    pass


def create_list():
    tasks = list()

    return tasks


def invite_for_input():
    command = input('Input command(list|new|done|read|open|write|cls|exit): ')
    
    return command


def check_input(command, tasks):
    commands = ['list', 'new', 'exit', 'done', 'read', 'cls' ,'open' ,'write']
                      
    if command not in commands:
        print('Bad input')
    elif command == 'list':
        list_command(tasks)
    elif command == 'new':
        new_command(tasks)
    elif command == 'done':
        done_command(tasks)
    elif command == 'read':
        read_command()
    elif command == 'cls':
        cls_command()
    elif command == 'open':
        open_exe_command()
    elif command == 'write':
        write_command()
    else:
        exit_command()



def list_command(tasks):
    if len(tasks) == 0:
        print('You didn\'t add any tasks, try to choose \'new\' command')
    else:
        for index, task in enumerate(tasks):
            print(index, ':', task)


def new_command(tasks):
    new_task = input('Input a task: ')
    tasks.append(new_task)
    try:
        task_file = open(r"D:\\IT\\Projects\\console_utilite\\test.txt", 'x')
    except:
        task_file = open(r"D:\\IT\\Projects\\console_utilite\\test.txt", 'w')
    for item in tasks:
        task_file.write(item + '\n')

    return tasks


def done_command(tasks):
    if len(tasks) == 0:
        print('You didn\'t add any tasks, try to choose \'new\' command')
    else:
        print('Choose the number of task: ')
        for index, task in enumerate(tasks):
            print(index, ':', task)
        
        inp = int(input())
        for ind, task in enumerate(tasks):
            if inp == ind:
                print(task, 'is done')
                tasks.remove(task)
        task_file = open(r"D:\\IT\\Projects\\console_utilite\\test.txt", 'w')
        for item in tasks:
            task_file.write(item + '\n')   
        
    return tasks

def read_command():

    direct = input('Input a directory of file to read\nPlease input it in that format:\nD:\\smth\\smth.txt:\n')
    text = open(direct)
    i = 1
    for all in text.readlines():
        print(" " + str(i) + " ║  " + all[0:-1])
        sleep(0.2)
        i += 1
    

def cls_command():
    print('\033c')


def open_exe_command():
    username = os.environ.get("USERNAME")
    exes = {
        'subl': 'C:\\Users\\' + username + '\\Desktop\\SublimeText3.lnk',
        'telega': 'C:\\Users\\' + username + '\\Desktop\\Telegram.lnk',
        'chrome':'C:\\Users\\' + username + '\\Desktop\\Chrome.lnk',
        'vscode': 'C:\\Users\\' + username + '\\Desktop\\VSCode.lnk',
        'cmd': 'C:\\Users\\' + username + '\\Desktop\\ConEmu.lnk',
        'music': 'D:\\Music\\Shadows.mp3',
        'discord': 'C:\\Users\\' + username + '\\Desktop\\Discord.lnk',
        'mine': 'C:\\Users\\' + username + '\\Desktop\\Minecraft.lnk',
        'note': 'C:\\Users\\' + username + '\\Desktop\\Notepad++.lnk'
    }
    execution = ''
    while execution not in exes.keys():
        execution = input('Input the command(subl|telega|chrome|vscode|cmd|music|discord|mine|note):\n')
        os.popen(exes[execution])
        
def write_command():
    # it is new command which will can make new file in directory
    # which user said, and append some text into existing file
    direct = input('Input a directory of file to make or append\nPlease input it in that format:\nD:\\smth\\\n')
    name_of_file = input('Input the name of file: ')
    req = input('Is file existing in this directory(yes/no)? ')
    inputs = input('What do you want to write?\n')
    
    if req == 'yes':
        file = open(direct + name_of_file, 'a')
        file.write('\n' + inputs)
    elif req == 'no':
        file = open(direct + name_of_file, 'w')
        file.write('\n' + inputs)
    else:
        print('Bad input')

def exit_command():
    raise UserExit('See you next time!')


def main():
    list_with_tasks = create_list()
    while True:
        try:
            command = invite_for_input()
            check_input(command, list_with_tasks)
        except UserExit as e:
            print(e)
            break
        except KeyboardInterrupt:
            print('Shutting down, bye')
            break
        except Exception as e:
            print('Something wrong,', e)


main()
