#Group: T031
#Contributing Members: Ibtasam Rasool (Leader), Maria Mickel, Liron Bi, Kyle Abbott
#Milestone: 3
#Date of Submission: 4/9/2021

from Cimpl import choose_file, create_color, set_color, load_image, get_color, Image, Color, show, copy, get_width, get_height, save_as
from  simple_Cimpl_filters import grayscale
from point_manipulation import _take_first, sort_points
import numpy


LEMON=create_color(255,255,0) 
PINK=create_color(255,0,255)
AQUA=create_color(0,255,255)
BLACK=create_color(0,0,0)
GRAY=create_color(128,128,128)
WHITE=create_color(255,255,255)
BLOOD=create_color(255,0,0)
BLUE=create_color(0,0,255)
GREEN=create_color(0,255,0)


def red_channel(image: Image) -> Image:
    """Return a red only copy of the image; that is, an image that contains
    only the red component of the original image. Written by Kyle Abbott
    
    >>> image = load_image(choose_file())
    >>> red_image = red_channel(image)
    >>> show(red_image)
    """
    new_image = copy(image)
    
    # Removes green and blue colours from image
    for x, y, (r, g, b) in image:
        
        Redscale = create_color(r, 0, 0)
        set_color(new_image, x, y, Redscale)
    return new_image


def green_channel(image: Image) -> Image:
    """
    Returns the green only version of a given image. Written by Liron Bi
    
    >>>image = load_image(file)
    >>>green_image = green_filter(image)
    >>>show(green_image)
    """
    new_image = copy(image) #copies the image so the original is not replaced
    
    for x, y, (r, g, b) in image: #finds the color, and x and y coordinates of the pixel
        green = create_color(0, g, 0) #keeps only the green in the colour
        set_color(new_image, x, y, green) #replaces old colour
    return new_image #returns the new image


def blue_channel(original_image:Image)-> Image:
    copy_image = copy(original_image)
    """
    Returns an image where the only colour expressed is blue. Written by Maria Mckiel.
    >>>original_image = c.load_image(c.choose_file())
    >>>blue_color=blue_channel(original_image)
    >>>c.show(blue_color)
    """
    for x, y, (r, g, b) in copy_image:
        pixel_color_blue=create_color(0,0,b)
        set_color(copy_image,x,y,pixel_color_blue)
    return copy_image


def combine(red_image: Image, green_image: Image, blue_image: Image) -> Image:
    """Returns an image with the combined color values from the pixels of the three filtered images the
    red_filter, green_filter and blue_filter. Written By Ibtasam Rasool

    Example 1:
    >>>red_image=load_image(choose_file())
    >>>green_image=load_image(choose_file())
    >>>blue_image=load_image(choose_file())
    >>>show(combine(red_image, green_image, blue_image))
    
    Example 2:
    >>>red_image=load_image(choose_file())
    >>>show(red_image)
    >>>green_image=load_image(choose_file())
    >>>show(green_image)
    >>>blue_image=load_image(choose_file())
    >>>show(blue_image)
    >>>show(combine(red_image, green_image, blue_image))
    >>>save_as(combined, 'combined-image.png')
    """
    combined_image=copy(red_image)
    for x,y,color in combined_image:
        color=get_color(red_image, x, y)
        red=color[0]
        color=get_color(green_image, x, y)
        green=color[1]
        color=get_color(blue_image, x, y)
        blue=color[2]
        combined_color=create_color(red, green, blue)
        set_color(combined_image, x, y, combined_color)

    return(combined_image)


def three_tone(original_image:Image, color_1, color_2, color_3)-> Image:
    '''
    Returns an image where the colours are one of the three parametersm color_1,color_2, or color_3. It returns color_1 if the average value of the brightness is less than 84, returns color_2 if the average value of the brightness is between 84 and less than 170, and returns color_3 if the average value of the brightness is between 170 and 255. Team: T031, Developed By: Maria McKiel.
    
    >>>original_image = load_image(choose_file())
    >>>three_tone_pic=three_tone(original_image,AQUA,LEMON,PINK)
    >>>show(three_tone_pic)
    
    >>>original_image = load_image(choose_file())
    >>>three_tone_pic=three_tone(original_image,BLOOD,BLUE,GREEN)
    >>>show(three_tone_pic)
    
    >>>original_image = load_image(choose_file())
    >>>three_tone_pic=three_tone(original_image,BLACK,WHITE,GRAY)
    >>>show(three_tone_pic)
    '''
    copy_image=copy(original_image) #creates a copy of the image so the original is not destroyed
    
    for x,y,(r,g,b) in copy_image:
        avg_brightness=(r+g+b)/3 #determines the average brightness in the pixel
        if 0 <= avg_brightness < 85: 
            set_color(copy_image,x,y,color_1) #sets the pixel to the new colour based of the average brightness
        if 85 <= avg_brightness < 171:
            set_color(copy_image,x,y,color_2) #sets the pixel to the new colour based of the average brightness
        if 171 <= avg_brightness <=255:
            set_color(copy_image,x,y,color_3) #sets the pixel to the new colour based of the average brightness
    return copy_image #returns the modified image


def extreme_contrast(image:Image):
    """Return an extreme contrast version of original image where all rgb
    values from 0 to 127 is set to 0 and all rgb values from 128 to 255 is set
    to 255. Team: T031, Developed By: Kyle Abbott. 
    
    >>> image = load_image(choose_file())
    >>> extreme_image = extreme_contrast(image)
    >>> show(extreme_image)
    """
    new_image = copy(image)
    
    # Changes contrast to extreme level
    
    for x, y, (r, g, b) in image:
        if r <= 127:
            r=0
        else:
            r=255
        
        if g <= 127:
            g=0
        else:
            g=255
                
        if b <= 127:
            b=0
        else:
            b=255
            
    
        ext_cont = create_color(r, g, b)
        set_color(new_image, x, y, ext_cont)
    return new_image


def sepia(image: Image) -> Image:
    """
    Returns a grayscaled then yellow tinted version of a given image. Yellow tint is dependant on the value of the color. 
    Team: T031, Developed By: Liron Bi.
    
    >>>image = load_image(file)
    >>>sepia_image = sepia(image)
    >>>show(sepia_image)
    """
    new_image = grayscale(copy(image)) #copies the image so the original is not replaced
    
    for x, y, (r, g, b) in new_image: #finds the color, and x and y coordinates of the pixel
        if r < 63:
            b *= 0.9
            r *= 1.1
        elif r <= 191:
            b *= 0.85
            r *= 1.15
        else:
            b *= 0.93
            r *= 1.08
        sepia = create_color(round(r), round(g), round(b))
        set_color(new_image, x, y, sepia) #replaces old colour
    return new_image #returns the new image


def _adjust_component(component_val: int) -> int:
    """Returns the mid point of a pixel range that is decided depending on the
    range that a given pixel falls within, the ranges for pixel values are 
    0-63, 64-127, 128-191, 192-255 with the mid points being, 31, 95, 159, 223
    respectively. Team: T031, Developed by Ibtasam Rasool.
    
    >>>_adjust_component(0)
    31
    >>>_adjust_component(50)
    31
    >>>_adjust_component(80)
    95
    >>>_adjust_component(150)
    159
    >>>_adjust_component(200)
    223
    >>>_adjust_component(255)
    223
    """
      
    if(component_val <= 63):
            adjusted_val=(0+63)//2
        
    elif(component_val <= 127 and component_val > 63):
            adjusted_val=(63+127)//2   
    
    elif(component_val <= 191 and component_val > 127):
            adjusted_val=(127+191)//2  
            
    elif(component_val <= 255 and component_val > 191):
            adjusted_val=int(191+255)//2     
    
    return adjusted_val


def posterize(original_image: Image) -> Image:
    """Returns an image that has been posterized, having all of its pixels r,g,b values changed to 1 of 4 values depending
    on what range the pixles original values resided in the 4 possible values are
    31, 95, 159, 223 corresponding to the ranges, 0-63, 64-127, 128-191, 192-255 respecitvely. Team: T031, Developed by Ibtasam Rasool.
    
    >>>image=load_image(choose_file())
    >>>posterized_image=posterize(image)
    >>>show(posterized_image)
    """
    
    posterized = copy(original_image)
    
    for x, y, (r, g, b) in original_image:
        adjusted_red = _adjust_component(r) 
        adjusted_green = _adjust_component(g) 
        adjusted_blue = _adjust_component(b) 
        adjusted_color = create_color(adjusted_red, adjusted_green, adjusted_blue)
        set_color(posterized, x, y, adjusted_color)
        
    return posterized


def detect_edges(original_image:Image, threshold:int)->Image:
    """Returns images where the only two colours are black and white. The color is based off the difference of the brightness of the pixel and the brightness of the pixel below it. Team: T031, Developed By: Maria McKiel. 
    
    >>>edges_image=detect_edges(original_image,50)
    show(edges_image)
    >>>edges_image=detect_edges(original_image,15)
    show(edges_image)
    """
    COPY=copy(original_image)
    HEIGHT=get_height(COPY)
    WIDTH=get_width(COPY)
    
    for x, y,(r,g,b) in COPY:
        if y != HEIGHT-1:
            color=get_color(original_image, x, y+1)
            avg_color= (sum(color))/3
            avg_brightness=((r+g+b)/3)
            difference= abs(avg_brightness - avg_color)
            if difference >= threshold:
                set_color(COPY,x,y,BLACK)
            else:
                set_color(COPY,x,y,WHITE)
        else:
            set_color(COPY,x,y,WHITE)
    return COPY


def _interpolation (points: list) -> list:
    """Returns, of at least two points, the coefficeints of an interpolating polynomial (can be linear or quadratic) or of a
    quadratic regression polynimial, the type of polynomial depends on
    the number of points passed in, three or two points will result in an interpolating polynomial
    greater than three points will result in a quadratic regression polynomial. Team: T031, Developed by: Ibtasam Rasool.
    
    >>>_interpolation([(1,1), (2,4)])
    [ 3. -2.]
    >>>_interpolation([(2.5, 4.5), (5.2, 9.1),(7.3, 20)])
    [ 0.72641093 -3.88966049  9.68408289]
    >>>_interpolation([(1,3), (3,7), (8, 2), (10,-2)])
    [-0.28571429  2.48247978  1.27493261]
    """
    x_coordinates=[]
    y_coordinates=[]
    if (len(points) == 2):
        poly_degree = 1
    else:
        poly_degree = 2
    
    for coordinate in points:
        x, y = coordinate
        x_coordinates.append(x)
        y_coordinates.append(y)
         
    poly_equation = numpy.polyfit(x_coordinates, y_coordinates, poly_degree)
    return(poly_equation)


def _exhaustive_search(max_x: int, polycoeff: list, val: int) -> int:
    """
    Solves f(x)-val=0 for x between 0 and max_x where polycoeff contains the
    coefficients of f, using EPSILON of 1 (as we only need ints for pixels).
    Returns None if there is no solution between the bounds. Team: T031 Written by: Liron Bi Student Number: 101203282
    
    >>> _exhaustive_search(639,[6.33e-03,-3.80e+00,5.57e+02],0)
    253
    >>> _exhaustive_search(639,[7.24e-04,-1.19e+00,4.51e+02],0)
    590
    >>> _exhaustive_search(639,[7.24e-04,-1.19e+00,4.51e+02],479)
    None
    """
    
    EPSILON = 1
    step = 0.01
    guess = 0
    
    while guess < max_x:
        if abs(numpy.polyval(polycoeff, guess) - val) < EPSILON:
            return round(guess)
        else:
            guess += step


def _image_border_finding(size:list, polycoeff:list) -> list:
    """Returns the coordinate of the pixels where the function meets the border. Team: T031 Written by: Liron Bi Student Number: 101203282
    >>>_image_border_finding([400,400], [-5.0e-03, 2.5e+00, -2.0e+02])
    [(100, 0), (399, 1)]
    >>>_image_border_finding([400,400], [5.0e-03, -2.5e+00, 4.0e+02])
    [(0, 399), (399, 199)]
    >>>
    """
    lst_of_intersections=[]
    pixel_x= size[0]
    pixel_y= size[1]
    new_polycoeff = polycoeff.copy()
    
    if _exhaustive_search(pixel_x-1, polycoeff, 0) != None:
        root=(numpy.roots(polycoeff))
        root=root.tolist()
        for i in range(len(root)):
            if 0 <= round(root[i]) < pixel_x-1:
                coordinates = (round(root[i]), 0)
                lst_of_intersections.append(coordinates)                
    
    if _exhaustive_search(pixel_x-1, polycoeff, pixel_y) != None:
        new_polycoeff[len(polycoeff)-1] = polycoeff[len(polycoeff)-1] - pixel_y
        root=(numpy.roots(new_polycoeff))
        root=root.tolist()
        for i in range(len(root)):
            if 0 <= round(root[i]) < pixel_x-1:
                coordinates = (round(root[i]), pixel_y-1)
                lst_of_intersections.append(coordinates)                
                
    if 0 <= round(numpy.polyval(polycoeff, 0)) <= pixel_y-1:
        coordinates = (0, round(numpy.polyval(polycoeff, 0)))
        if coordinates != (0, 0):
            lst_of_intersections.append(coordinates)
        
    if 0 <= round(numpy.polyval(polycoeff, pixel_x-1)) <= pixel_y-1:
        coordinates = (pixel_x-1, round(numpy.polyval(polycoeff, pixel_x-1)))
        if coordinates != (pixel_x-1, 0):
            lst_of_intersections.append(coordinates)
    
    lst_of_intersections = sort_points(lst_of_intersections)
    return lst_of_intersections


def draw_curve(image:Image, color:Color, pointlist: list = None)-> Image:
    """Returns a copy of an Image with a quadratic curve draw on it. T031. Developed By: Kyle Abbott.
    
    """
    new_image= copy(image)
    height=get_height(new_image)
    width=get_width(new_image)
    image_size=[width, height] 
    
    if pointlist == None:
        pointlist= []
        print(str(width),"pixels in x and",str(height),"pixels in y")
        num_points= int(input("How many points do you want to use (MUST be >= 2): "))
        
        x=0
        while x < num_points:
            x+=1
            #getting x coordinate
            message= "Horizontal Coordinate(x) " + str(x)+ ": "
            x_point= int(input(message))
            #getting y coordinate
            message= "Vertical Coordinate(y) " + str(x)+ ": "
            y_point= int(input(message))
            pointlist.append((x_point, y_point))
        
    pointlist= sort_points(pointlist)   
    interpol=_interpolation(pointlist)   
    border=_image_border_finding(image_size, interpol)

    for x, y, (r, g ,b) in new_image:
        if x >= border[0][0] and x <= border[1][0]:
            if len(interpol) > 2:
                y_draw=round((interpol[0])*(x**2)+(interpol[1])*(x)+interpol[2])
            elif len(interpol) == 2:
                y_draw=round((interpol[0])*(x)+interpol[1])
            
            w=0
            while w <= 5:
                wchange=-2+ w
                drawwidth=x+wchange
                w+= 1
                if drawwidth >= 0 and drawwidth < width:
                    h=0
                    while h <= 5:
                        hchange = -2 + h
                        drawheight = y_draw+hchange
                        h+= 1
                        if drawheight  >= 0 and drawheight < height:
                            set_color(new_image, drawwidth, drawheight, color)

    return new_image


def flip_horizontal(image: Image) -> Image:
    """
    Returns the give image flipped horizontally. Team: T031, Developed By: Liron Bi.
    
    >>>image = load_image(file)
    >>>horizontal_image = flip_horizontal(image)
    >>>show(horizontal_image)
    """
    new_image = copy(image) #copies the image so the original is not replaced
    
    for x, y, (r, g, b) in image: #finds the color, and x and y coordinates of the pixel
        new_color = create_color(r, g, b)
        set_color(new_image, get_width(image) - x -1, y, new_color) #replaces old colour
    return new_image #returns the new image


def flip_vertical (original_image: Image) -> Image:
    """Returns an image that has been flipped (reflected) across the x-axis so the image
    relative to its original orientation will be upside down. Team: T031, developed by: Ibtasam Rasool.
    
    Example 1:
    >>>image = load_image(choose_file())
    >>>show(image)
    >>>flipped_image = flip_vertical(image)
    >>>show(flipped_image)
    """
    
    flipped_image=copy(original_image)
    image_width = get_width(original_image)
    image_height = get_height(original_image)
    
    for x in range(image_width):
        for y in range((image_height//2)):
            color_pos_a = get_color(original_image, x, y)
            color_pos_b = get_color(original_image, x, (image_height-1)-y)
            set_color(flipped_image, x, y, color_pos_b)
            set_color(flipped_image, x, (image_height-1)-y, color_pos_a)
    
    return (flipped_image)









    
    
