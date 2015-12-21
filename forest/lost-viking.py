SLIDE = 10
SWITCH = 6
SKIP = 9
TURN = 1
sideSteps = 1
steps = 1
X_PACE_LENGTH = 4
Y_PACE_LENGTH = 6
while steps <= 35:
    self.moveXY(steps * X_PACE_LENGTH, sideSteps * Y_PACE_LENGTH) 
    if steps % SWITCH == 0:
        TURN = -TURN
    sideSteps += TURN
    if steps % SKIP == 0:
        sideSteps += TURN
    if sideSteps < 1:
        sideSteps += SLIDE
    if sideSteps > SLIDE:
        sideSteps -= SLIDE
    steps += 1


        

        
    
