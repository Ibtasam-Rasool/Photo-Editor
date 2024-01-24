#Group: T031
#Contributing Members: Ibtasam Rasool (Leader), Maria Mickel, Liron Bi, Kyle Abbott
#Milestone: 3
#Date of Submission: 4/9/2021

from T031_image_filters import *


def main_menu()-> str:
    """Returns the user input in all caps. T031. Developed By: Maria McKiel.
    
    >>>user_input = main_menu()
    >>>print(user_input)
    """
    menu_commands="\nL)oad S)ave_as\n3)-tone X)treme contrast T)int sepia P)osterize\nE)dge detect D)raw curve V)ertical flip H)orizontal flip\nQ)uit\n\n: "
    
    user_input= input(menu_commands)
    user_input=str.upper(str(user_input))
    return user_input


def check(user_input: str, load: bool) -> (bool, bool, str):
    """Returns whether a given input falls within the correct parameters. Team: T031, Developed By: Liron Bi.
    
    >>>results = check('3', False)
    >>>print(results)
    (True, False, 'No image loaded')
    
    """
    valid_inputs = ['3', 'X', 'T', 'P' , 'E', 'V', 'H', 'D', 'L', 'S', 'Q']
    for x in valid_inputs:
        if x == user_input:
            if x == 'L':
                return (True, True, 'None')
            
            elif not load and user_input != 'Q':
                return (True, False, 'No image loaded')            
            
            else:
                return (True, True, 'None')
    
    return (False, load, 'No such command')


def image_manipulation(user_input: 'str', image: Image) -> Image:
    """returns an image that has either been loaded in or maipulated by a filter. Team T031, Developed By: Kyle Abbott and Ibtasam Rasool.
    
    >>>image = load_image(choose_file())
    >>>filtered_image = image_manipulation('E', image)
    >>>show(filtered_image)
    """
    
    commands = {
        '3': three_tone, 
        'X': extreme_contrast, 
        'T': sepia, 
        'P': posterize,
        'E': detect_edges,
        'V': flip_vertical,
        'H': flip_horizontal,
        'D': draw_curve,
        'L': load_image,
        'S': save_as
    }
    
    if (user_input == 'S'):
        file_name = input('Enter File Name to save as:')
        commands[user_input](image, file_name)
        
    elif(user_input == '3'):
        image = commands[user_input](image, AQUA, BLOOD, LEMON)
        
    elif(user_input == 'D'):
        image = commands[user_input](image, BLOOD)
        
    elif(user_input == 'L'):
        image_file = choose_file()
        image = commands[user_input](image_file)
        
    elif(user_input == 'E'):
            image = commands[user_input](image, 15)    
        
    else:
        image = commands[user_input](image)
        
    return image


#main
image_load = False
run = True
image = None

while run:
    user_input = main_menu()
    valid_input, image_load, err_msg = check(user_input, image_load)
    
    if image_load and valid_input or user_input == 'Q':
        if user_input == 'Q':
            run = False
        
        else:    
            image = image_manipulation(user_input, image)
            show(image)
            
    else:
        print('\n', err_msg)