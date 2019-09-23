__author__ = 'fearsd'

 # this module requires to get username and for launch applications on computer.
import os

# sleep is used to print files pretilly.
from time import sleep

# datetime is used to write in logs current time of done command.     
from datetime import datetime

# need for open site in default browser
import webbrowser


class UserExit(KeyboardInterrupt):
    # Raises if user writed 'exit'.
    pass


def create_list():
    ''' 
    Create new list for store tasks.
    :return: empty list.
    '''
    tasks = []
    return tasks


def logger(log, *args):
    '''
    This func creates log.txt and write there all calls of commands.
    :param log: name of command.
    :param *args: additional info about called command.
    :return: None.
    '''

    # 'months' dict requires because of date.month gives num not a name of month
    months = {
        1: 'Jan',
        2: 'Feb',
        3: 'Mar',
        4: 'Apr',
        5: 'May',
        6: 'Jun',
        7: 'Jul',
        8: 'Aug',
        9: 'Sep',
        10: 'Oct',
        11: 'Nov',
        12: 'Dec'
    }

    argument = ''
    for arg in args:
        argument += ' '
        argument += str(arg)

    date = datetime.now()
    # TODO: add date.year
    month = date.month
    day = str(date.day)
    hour = str(date.hour)
    minute = str(date.minute)
    second = str(date.second)

    if len(day) == 1:
        day = '0' + day
    if len(minute) == 1:
        minute = '0' + minute
    if len(second) == 1:
        second = '0' + second

    now_date = str(months[month]) + ' ' + day + ' ' + hour + ':' + minute + ':' + second
    try:
        log_str = open(r"D:\\Log\\log.txt", 'x')
        log_str.write('Called: ' + log + argument + ' at ' + now_date + '\n') # Example: Called: calc 12*3 36 at Jul 14 15:15:13
    except:
        log_str = open(r"D:\\Log\\log.txt", 'a')
        log_str.write('Called: ' + log + argument + ' at ' + now_date + '\n')

    log_str.close()


def invite_for_input():
    '''
    Handle user input.
    :return: command which user called.
    '''

    command = input('Input command(list|new|done|read|open|write|calc|music|exit): ')
    return command


def check_input(command, tasks):
    '''
    Calls functions, which perform commands.
    :param command: command which need to execute.
    :param tasks: current tasks state.
    :return: None.
    '''

    commands = ['list', 'new', 'exit', 'done', 'read', 'open' ,'write', 'calc', 'music']
                      
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
    elif command == 'open':
        open_exe_command()
    elif command == 'write':
        write_command()
    elif command == 'calc':
        calc_command()
    elif command == 'music':
        launch_music_command()
    else:
        exit_command()


def list_command(tasks):
    '''
    Printing tasks.
    :param tasks: current tasks state.
    :return: None.
    '''
    
    logger('list')

    if len(tasks) == 0:
        print('You didn\'t add any tasks, try to choose \'new\' command')
    else:
        for index, task in enumerate(tasks):
            print(index, ':', task)


def new_command(tasks):
    '''
    Handle user new task.
    :param tasks: current tasks state.
    :return: new tasks state.
    '''
    
    new_task = input('Input a task: ')
    tasks.append(new_task)
    logger('new', new_task)
    return tasks


def done_command(tasks):
    '''
    Delete task from tasks which user choosed.
    :param tasks: current tasks state.
    :return: new tasks state. 
    '''

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

    logger('done')
    return tasks


def read_command():
    '''
    Open .txt and other files which user typed.
    :return: None.
    '''
    
    direct = input('Input a directory of file to read\nPlease input it in that format:\nD:\\smth\\smth.txt:\n')
    text = open(direct)
    i = 1
    for all in text.readlines():
        print(" " + str(i) + " ║  " + all[0:-1])
        sleep(0.2)
        i += 1

    logger('read', direct)
    

def open_exe_command():
    '''
    Execute programs on my computer via their alias.
    :return: None.
    '''
    
    username = os.environ.get("USERNAME")
    exes = {
        'subl': 'C:\\Users\\' + username + '\\Desktop\\SublimeText3.lnk',
        'telega': 'C:\\Users\\' + username + '\\Desktop\\Telegram.lnk',
        'chrome':'C:\\Users\\' + username + '\\Desktop\\Chrome.lnk',
        'vscode': 'C:\\Users\\' + username + '\\Desktop\\VSCode.lnk',
        'cmd': 'C:\\Users\\' + username + '\\Desktop\\ConEmu.lnk',
        'discord': 'C:\\Users\\' + username + '\\Desktop\\Discord.lnk',
        'mine': 'C:\\Users\\' + username + '\\Desktop\\Minecraft.lnk',
        'note': 'C:\\Users\\' + username + '\\Desktop\\Notepad++.lnk'
    }
    execution = ''
    
    while execution not in exes.keys():
        execution = input('Input the command(subl|telega|chrome|vscode|cmd|music|discord|mine|note):\n')
        os.popen(exes[execution])

    logger('open', execution)
    

def write_command():
    '''
    Can make new file in directory,
    which user said and append some text into existing file.
    :return: None.
    '''

    direct = input('Input a directory of file to make or append\nPlease input it in that format:\nD:\\smth\\\n')
    name_of_file = input('Input the name of file: ')
    req = input('Is file existing in this directory(yes/no)? ')
    inputs = input('What do you want to write?\n')
    
    if req == 'yes':
        file = open(direct + name_of_file, 'a')
        file.write('\n' + inputs)
        file.close()
    elif req == 'no':
        file = open(direct + name_of_file, 'w')
        file.write('\n' + inputs)
        file.close()
    else:
        print('Bad input')

    logger('write', direct, name_of_file, inputs)


def calc_command():
    '''
    Calculates.
    :return: None.
    ''' 

    to_calc = input('Input things to calc\n')
    res = eval(to_calc)
    print('Result:', res)

    logger('calc', to_calc, res)


def exit_command():
    '''
    Exit from script.
    :return: None.
    :raises: UserExit.
    '''
    
    logger('exit')
    raise UserExit('See you next time!')

def launch_music_command():
    webbrowser.open_new_tab('http://music.yandex.ru/home')

def main():
    '''
    Main func. It starts when the program is called.
	It also calls other functions.
	:return: None.
    '''

    os.makedirs('D:\\Log', exist_ok=True)
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
            print('Something wrong, ', e)


if __name__ == "__main__":
    main()
