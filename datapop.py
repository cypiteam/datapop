"""
File: datapop.py
Author: Curtis Byrd
Date: July 20th, 2020
Email: Curtisb1@umbc.edu
Description: This program acts as a deadmans switch
if the switch is not entered when queued and in an acceptable time frame
it triggers a reaction
"""
DEADMANS_DATA = "deadmans_switch_data.txt"
TRIGGER = '"Trigger":'
TIMER = '"Timer":'
ACTION = '"Action":'
DETONATION = "Detonation:"
RESTART_COMMAND = 'restart'


def read_data():
    """
    Reads the data for the deadman's switch
    :return: a list of all the data for the deadmans switch
    """
    deadmans_file = []

    # opens the deadman's switch data
    with open(DEADMANS_DATA, "r") as f:
        file = f.readlines()

        # strips the /n end character of a each line of text
        for i in range(len(file)):
            file[i] = file[i].strip()
            deadmans_file.append(file[i])

    return deadmans_file

def write_data(switch):
    """
    UNECESSARY
    This function allows user to change the data for the deadmans switch
    this is only for testing purposes until a front end is available
    I put this on hold because I realized it's unnecessary
    :param switch: the old deadmans switch data as a list
    :return: the new deadmans switch data as a list
    """
    for i in range(len(switch)):
        if switch[i] == TRIGGER:
            input('What would you like the trigger to be? Default:[startup]')

def check_input(file, user_input):
    """
    checks if the input the user put in matches the password
    :param file: the deadmans switch data as a list
    :param user_input: the string the user inputted
    :return: returns a boolean that states if the password was correct or not
    """
    correct = False

    # searches the file for the "action"
    for i in range(len(file)):
        # if it matches the user input set correct to true
        if i < len(file) - 1 and file[i] == ACTION and file[i+1] == user_input:
            correct = True
    return correct

def detonate(file):
    """
    Finds what the detonation is in the data and executes it
    :param file: The data for the deadman switch as a list
    :return:
    """
    # searched the file for the detonation command
    for i in range(len(file)):
        if i < len(file) - 1 and file[i] == DETONATION:
            # if the command is restart then restart
            if file[i+1] == RESTART_COMMAND:
                restart()

def restart():
    """
    Restarts the pi. Code adapted from ridgesolution.ie
    :return:
    """
    command = "/usr/bin/sudo /sbin/shutdown -r now"
    import subprocess
    process = subprocess.Popen(command.split(), stdout=subprocess.PIPE)
    output = process.communicate()[0]
    print(output)

if __name__ == '__main__':
    deadmans_data = read_data()
    password = input("You shouldn't see this prompt because we're trying to be sneaky")
    accepted = False
    time_expired = True

    accepted = check_input(deadmans_data, password)
    if accepted:
        print("Yay I don't have to go boom boom")
    if time_expired and not accepted:
        detonate(deadmans_data)




