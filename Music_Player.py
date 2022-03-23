import pygame,time,random,os,easygui
c=[]
pygame.init()
pygame.mixer.init()
def z():
    x=0
    o=easygui.diropenbox()
    f=o
    while x<30:
        o=f
        while os.path.isdir(o):
            if os.listdir(o)==[]:
                break
            o+='/'+random.choice(os.listdir(o))
            #print(o)
            if o.endswith('.mp3'):
                c.append(o)
                x+=1
                #print('Appended %s!'% o)
            else:
                continue
def g():
    global x
    if not pygame.mixer.music.get_busy():
        x+=1
        pygame.mixer.music.load(c[x])
        pygame.mixer.music.play()
    if x>28:
        z()
    pygame.time.delay(2100)
    g()
z()
x=0
g()
