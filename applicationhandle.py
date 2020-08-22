import os, sys
import subprocess

def openApplication(name, directory):
    try:
        command = '"' + directory + name + '"'
        print("Command:",command)
        #os.system(command)
        subprocess.Popen(command, shell=True,
                           stdout=subprocess.PIPE, 
                           stderr=subprocess.PIPE)
    except Exception as e:
        print("Error: ",e)
        print("Unable to open the application {} | {}".format(name, directory))

