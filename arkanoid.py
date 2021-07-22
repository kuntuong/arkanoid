# Import the play version of PYTHON
import play  
import pygame

# The background's color is blue
play.set_backdrop("dark blue")

score_txt = play.new_text(words='Score:', x=play.screen.right-100, y=play.screen.bottom+30, color='white', size=70)
score = play.new_text(words='0', x=play.screen.right-30, y=play.screen.bottom+30, color='white', size=70)

# Create the base platform as what we will control
base_platform = play.new_box(
        color="black",
        x=0, y=-230,
        width=105,
        height=25,
        border_color='grey',
        border_width=2,
        transparency=98,
)

lost = play.new_text(
        words="¥øü dïdñ't ©ātc©h thé băłł, ¥øũ łøsT!",
        x = 0, y = 30,
        font=None,
        font_size=50,
        color="white"
)
lost.hide()
win = play.new_text(
        words="¥øü gøt ®ïd øƒ āłł brïçkś, ¥øũ ẇøñ!",
        x = 0, y = 30,
        font=None,
        font_size=50,
        color="white"
)
win.hide()
# Create the ball to play with
arkanoid_ball = play.new_circle(
        color="light blue",
        x=0, y=-180,
        radius=15,
        border_color="white",
        border_width=2,
        transparency=85
)

#Create the blocks the ball will hit
boxes = []

for l in range(4):
        for i in range(8):
                box = play.new_box(
                        color="grey",
                        border_color="dark blue",
                        border_width = 1,
                        x = -340 + (98 * i), y = 280 - (30 * l),
                        width = 98,
                        height = 30    
                )
                boxes.append(box)
                
@play.when_program_starts
def start():
        base_platform.start_physics(
                stable=True, 
                obeys_gravity=False, 
                bounciness=1, 
                mass=1
        )
        
        arkanoid_ball.start_physics(
                stable=False, 
                x_speed=18, y_speed=18, 
                obeys_gravity=False, 
                bounciness=1, 
                mass=9
        )

        
# Repeats it forever
@play.repeat_forever                    
def repeat():
        # if base_platform.x > 290:
        #         base_platform.physics.x_speed = 0
        # elif base_platform.x < -290:
        #         base_platform.physics.x_speed = 0
        # else:
        if play.key_is_pressed('left'):
                base_platform.physics.x_speed = -40
        elif play.key_is_pressed('right'):
                base_platform.physics.x_speed = 40
        
        else:
                base_platform.physics.x_speed = 0    
       
        for i in boxes:
                if arkanoid_ball.is_touching(i): 
                        i.hide()
                        boxes.remove(i)
                        arkanoid_ball.physics.x_speed = arkanoid_ball.physics.x_speed + 0.5
                        arkanoid_ball.physics.y_speed = arkanoid_ball.physics.y_speed + 0.5
                        arkanoid_ball.physics.x_speed = arkanoid_ball.physics.x_speed * -1
                        arkanoid_ball.physics.y_speed = arkanoid_ball.physics.y_speed * -1
                        score.words = str(int(score.words) + 10)

        if arkanoid_ball.y < base_platform.y:
                lost.show()
                arkanoid_ball.hide()
                base_platform.hide()
        if len(boxes) == 0:
                win.show()
                arkanoid_ball.hide()
                base_platform.hide()


       
        


# Start the program
play.start_program()