
#Game Settings

display_height = 600
display_width = 480
Title = "Jump!"
FPS = 60
Font_name = 'Comic Sans MS'
HS_file = 'Highscore.txt'
spritesheet = ''
# Player Properties

player_ACC = 0.5
player_Friction = -0.12
player_grav = 0.7
player_jump = 20


# Starting Platorms
plat_list = [
    (0, display_height - 40, display_width, 40),
    (display_width / 2 - 50, display_height * 3 / 4, 100, 20),
    (125, display_height - 350, 100, 20),
    (300, display_height - 500, 70, 20),

]


#Colours
black = (0,0,0)
white = (255,255,255)
red = (255,0,0)
green = (0,255,0)
blue = (135,206,250)
grey = (192, 192, 192)
yellow = (255,255,102)
orange = (255,128,0)
brown = (204,102,0)

dark_red = (160,0,0)
dark_blue = (0,0,205)
dark_green = (0,160,0)
dark_yellow = (255,255,51)
