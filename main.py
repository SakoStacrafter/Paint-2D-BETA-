import os 
import time

yellow_block = '🟨 '
orange_block = '🟧 '	
red_block = '🟥 '
purple_block = '🟪 '
blue_block	= '🟦 '
green_block =	'🟩 '
brown_block = '🟫 '
if os.name == 'posix':
    brick_block = '🟫 '
else:
    brick_block = '🧱 '
white_block = '⬜ '
list_CP = {"yellow_block": yellow_block, "orange_block": orange_block, "red_block": red_block, "purple_block": purple_block, "blue_block": blue_block, "green_block": green_block, "brown_block": brown_block, "brick_block": brick_block, "white_block": white_block}

screen_list = ["0", "1", "2", "3", "4", "5"]

class Paint2D:
  def first_image(self):
    screen_list[0] = [brick_block, brick_block, brick_block, "  ", green_block, green_block, green_block]
    screen_list[1] = [brick_block,blue_block, brick_block, "  ", green_block, green_block, green_block]
    screen_list[2] = [brick_block, brick_block, brick_block, "  ", "  ", brown_block, "  "]
    screen_list[3] = [green_block, green_block, green_block, green_block, green_block, green_block, green_block]
    screen_list[4] = ["  ", "  ", "  ", "  ", "  ", green_block, "  "]

  def do_the_tutorial(self):
    print("When your are done whith the tutorial you will be a pro on this so let's start!",end="")
    input()
    print("The first is the cordinates",end="")
    input()
    print("X is when you go to the rigth horizontal (-->)",end="")
    input()
    print("""The pattern or colors they exist are:
    yellow_block = 🟨
    orange_block = 🟧	
    red_block = 🟥
    purple_block = 🟪
    blue_block	= 🟦
    green_block =	🟩
    brown_block = 🟫
    brick_block = ?
    white_block = ⬜
   """)

  def start(self):
    self.s_clear()
    print("Hi and welcome to Paint 2D(BETA)")
    print("Tap enter to go to next text", end="")
    input()
    print("The program looks a littel bit diffrent on diffrent systems so you can test in orther and get diffrent reults.",end="")
    input()
    print("Have fun!")
    input()
    self.first_image()
    self.uppdate_screen()
    print('Tutorial yes or no?')
    tutorial_pick = str(input()).lower()

    #if tutorial_pick == 'yes':
    #  do_the_tutorial()

    #def do_the_tutorial():


    if tutorial_pick == 'yes': #INTE KLAR
      self.do_the_tutorial()
    else:
      self.start_game() 
    
  def start_game(self): #KLAR
    while True:
      self.input_move()
      self.uppdate_screen()

  def input_move(self): #INTE KLAR
    print('Write the X cordinate')
    X_cord = int(input())
    print('Write the Y cordinate')
    Y_cord = int(input())
    print('Write the color or pattern') 
    input_C_or_P = input()
    put_in = list_CP[input_C_or_P]
    screen_list[X_cord][Y_cord] = None
    screen_list[X_cord][Y_cord] = put_in

  def s_clear(self): #KLAR
    if os.name == 'posix':
        _ = os.system('clear')
    else:
        _ = os.system('cls')

  def uppdate_screen(self): #Ändra här om du lägger till fler rader
    self.s_clear()
    row_0 = screen_list[4][0] + screen_list[4][1] + screen_list[4][2] + screen_list[4][3] + screen_list[4][4] + screen_list[4][5] + screen_list[4][6]
    row_1 = screen_list[0][0] + screen_list[0][1] + screen_list[0][2] + screen_list[0][3] + screen_list[0][4] + screen_list[0][5] + screen_list[0][6]
    row_2 = screen_list[1][0] + screen_list[1][1] + screen_list[1][2] + screen_list[1][3] + screen_list[1][4] + screen_list[1][5] + screen_list[1][6]
    row_3 = screen_list[2][0] + screen_list[2][1] + screen_list[2][2] + screen_list[2][3] + screen_list[2][4] + screen_list[2][5] + screen_list[2][6]
    row_4 = screen_list[3][0] + screen_list[3][1] + screen_list[3][2] + screen_list[3][3] + screen_list[3][4] + screen_list[3][5] + screen_list[3][6]
    print(row_0)
    print(row_1)
    print(row_2)
    print(row_3)
    print(row_4)

app = Paint2D()
app.start()