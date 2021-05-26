import sys,pygame
from pygame.locals import *
fps=30
pygame.font.init
pygame.init()
window=pygame.display.set_mode((500,500))
pygame.display.set_caption('Lunar Lander')


BLACK=pygame.Color(0,0,0)
pygame.display.set_caption('Lunar lander')
font=pygame.font.Font("rainyhearts.ttf",20)
death=False

small_explosion=pygame.image.load('explosion small.png')
large_explosion=pygame.image.load('explosion large.png')

moon_surface=pygame.image.load('moon surface.jpg')
text_surface=font.render('out of fuel!',False,(255,0,0))
crash_text=font.render('Game over',False,(255,255,0))
crash_text2=font.render('Press R to retry or Q to quit',False,(255,255,0))
win_text=font.render('You WIN',False,(255,255,0))

red=pygame.Color(255,0,0)
gray=pygame.Color(189,189,189)
pygame.mixer.pre_init()
pygame.mixer.init()


class Lander(pygame.sprite.Sprite):
    def __init__(self):
        pass
    def engineBoost(self):
        global velocity
        global y
        acceleration=1
        
        velocity+=acceleration
        

clock = pygame.time.Clock()
play_again=False
while True:
    
    window.fill(BLACK)
    window.blit(moon_surface,(0,410))
    window.blit(moon_surface,(250,410))
    fuel_counter=0
    x=250
    y=0
    Counter=0
    velocity=0
    play_again=False
    death_counter=0
    collide=False
    pygame.display.update
    for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
    fuel=125
    #placeholder replace iwth y for the height
    #also add something like the draw y height vs the amount of fuel so use % or something
    fuelx=400
    pygame.draw.rect(window,red,(fuelx,200,20,100))
    fuelLeft=1
    
    lander_image=pygame.image.load('lander 16x16 sprite.png')
    lander_engine=pygame.image.load('lander 16x16 sprite engine on.png')
    
    lander=Lander()
    surface=pygame.Rect(0,400,500,500)
    while True:
        if play_again==1:
            break
        pygame.display.update()
        pygame.draw.rect(window,BLACK,(250,0,50,409))
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
        
        
        keys=pygame.key.get_pressed()
        if keys[pygame.K_w] and fuel>0:
            lander.engineBoost()
            
            window.blit(lander_engine,(x,y))
            '''engine=pygame.mixer.Sound('engine sound effect.mp3')'''
            fuel-=1
            if fuel_counter==5:
                fuel_counter=0
                fuelLeft+=4.2
            fuel_counter+=1
            #pygame.mixer.Sound.set_volume(engine,1.0)
            #pygame.mixer.Sound.play(engine,-1)
         
        else:
            window.blit(lander_image,(x,y))
            velocity-=0.81
        
        pygame.draw.rect(window,BLACK,(fuelx,200,20,fuelLeft))       
        if fuel<=0:
            window.blit(text_surface,(370,309))
        y-=velocity
        
        
        


        lander_leg=y-5
        collide=surface.collidepoint(x,lander_leg)
        if collide and abs(velocity)>3:
            death_texty=100
            #ADD THE EXPLOSINO DRAWING
            '''pygame.mixer.load("Explosion sound effect.mp3")
            pygame.mixer.set_voume(0.7)
            pygame.mixer.play()'''
        
            while True:
                if play_again==1:
                    break
                if death_counter<40 and play_again==False:
                    pygame.draw.rect(window,BLACK,(250,0,50,409))
                    window.blit(moon_surface,(250,410))
                    window.blit(small_explosion,(x,y))
                    pygame.display.update()
                   
                elif death_counter>40 and death_counter<100 and play_again==False:
                    pygame.draw.rect(window,BLACK,(250,0,50,409))
                    window.blit(moon_surface,(250,410))
                    window.blit(large_explosion,(x,y))
                    pygame.display.update()
                    
                elif death_counter>200 and play_again==False:
                   
                    pygame.draw.rect(window,BLACK,(250,0,50,410))
                    window.blit(moon_surface,(250,410))
                    pygame.display.update()
                   
                    
                    while True:
                        window.blit(crash_text,(200,100))
                        window.blit(crash_text2,(150,120))
                        pygame.display.update()
                         
                        for event in pygame.event.get():
                            if event.type == pygame.QUIT:
                                pygame.quit()
                                exit()
                        
                        quitkey=pygame.key.get_pressed()
                        
                        if quitkey[pygame.K_r]:
                            play_again=1
                            break
                        elif quitkey[pygame.K_q]:
                            sys.exit()
                death_counter+=1
                
        elif collide and abs(velocity)<=3:
            window.blit(win_text,(250,200))
            pygame.display.update()
            
            while True:
                
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        exit()
                
            
            '''pygame.mixer.Sound('Small step for man audio.mp3')
            pygame.mixer.Sound.set_voume(0.7)
            pygame.mixer.Sound.play()
            #figure out how to do audio and insert thats one small step form an qoute or whawtever
            #ADD SOMETHING HERE FOR WIN!!
        pygame.mixer.stop()'''
        
        
        clock.tick(fps)
