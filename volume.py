# A program that calculates the volume of a sphere
# Date: 8/8/20
# Created by Astral

def calc_sphere():
    user_radius =  int(input('What is the radius of the sphere? '))
    pi = 3.14159265359
    radius = user_radius
    v = 4.0/3.0*pi*radius**3

    if user_radius > 0:
        print('The volume of the sphere is', v)

    
calc_sphere()