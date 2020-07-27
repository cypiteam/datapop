"""
File:    test_restart.py
Author:  Curtis Byrd
Date:    July 20th 2020
E-mail:  curtisb1@umbc.edu
Description: Tests if the restart code actually works
"""
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
    restart()
