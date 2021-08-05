def circle(pi, radius):
    print("pi = ", pi)
    print("반지름 = ", radius)
    return pi * radius ** 2

def calculate_volume(length, width, depth):
    return length * width * depth


LOGO = """
                    ####
                ###########
             ####################
    ####### Algorithm 파이썬은 재미있다 #####
         ############################
             ####################
                  ##########
                     ####
"""

def logo_display():
    print(LOGO)
