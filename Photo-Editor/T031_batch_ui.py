#Group: T031
#Contributing Members: Ibtasam Rasool (Leader), Maria Mickel, Liron Bi, Kyle Abbott
#Milestone: 3
#Date of Submission: 4/9/2021

from T031_image_filters import *


def command_execution(commands_list: list)-> None:
    """ loads a given image sepecified by the commands list manipulates image by applying various filters and effects on it specified 
    by the commands list and saves that image by a name specified in the commands list. Team: T031 Developed By: Ibtasam Rasool.
    """
    commands = {
        '3': three_tone, 
        'X': extreme_contrast, 
        'T': sepia, 
        'P': posterize,
        'E': detect_edges,
        'V': flip_vertical,
        'H': flip_horizontal
    }
    
    image = load_image(commands_list[0])
    
    for command_num in range(2, len(commands_list)):
        if(commands_list[command_num] == 'E'):
            image = commands[commands_list[command_num]](image, 15)
        
        elif(commands_list[command_num] == '3'):
            image = commands[commands_list[command_num]](image, AQUA, BLOOD, LEMON)
            
        else:    
            image = commands[commands_list[command_num]](image)
    
    save_as(image, commands_list[1])


#main 
file_name = input("Enter Batch File Name (Include Extention)\n\n: ")
file = open(file_name)

for line in file:
    command_line = line.split()
    command_execution(command_line)
file.close()
