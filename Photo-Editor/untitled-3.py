def main_menu() -> 'str':
    #prints out menu (see culearn) and accepts input any input at all doesnt check 
    #print statements here to print out menu
    
    
    return user_input
    



def check(user_input: str, load: bool) -> tuple(bool, bool):    
    commands = {
        '3': three_tone, 
        'X': extreme_contrast, 
        'T': sepia, 
        'P': posterize,
        'E': detect_edges,
        'V': flip_vertical,
        'H': flip_horizontal,
        'D': draw_curve,
        'L': load_image
    }    
    valid_input = True
    # best way to check is use, variable = commands.get('user_input string') 
    #if variable is none then the input was invalid 
    #but if it is None then u have to check for whether it was possibly Q and based on that set 
    
    
    #you must check whether the user wants to load smt here then off of that save true or false into load 
    # once load has been flipped to True it will alwasy be passsed as True so this check shoul really occur once
    
    elif not load and not #('variable for wheter str recieved is legal'):
        print('The Error message for no image and incorrect input')

        
    elif load and not #('variable for wheter str recieved is legal'):
        print('Message for just the wrong input')
        
        
    elif not load and #('variable for wheter str recieved is legal'):
        print('message for just no image loaded')

    
    return valid_input, load 
    
    
def image_manipulation(user_input: 'str', image: Image) -> Image:
    commands = {
        '3': three_tone, 
        'X': extreme_contrast, 
        'T': sepia, 
        'P': posterize,
        'E': detect_edges,
        'V': flip_vertical,
        'H': flip_horizontal,
        'D': draw_curve,
        'L': load_image
    }
    
    #using commands.get(user_input)()
    # where commands.get(user_input) will be equal to a function name such as 'threetone' the brackets after are the parameters
    # the () is the parameter of the function so for majority u will just need to put in the image variable but some require additional parameters
    
    return image
    
    

load_image = False
run = True
image = None

while run:
    user_input = main_menu()
    valid_input, load_image = check(user_input, load_image)
    
    if load_image and valid_input or user_input == 'Q':
        if user_input == 'Q':
            run = False
        
        else:    
            image = image_manipulation(user_input, image)
