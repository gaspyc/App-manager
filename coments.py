import keyboard, random,time,win32api,win32con
# bloque1[0] + bloque1? + frase? + emote? | bloque[1] + frase? + emote?
bloque1 = [('hola','ola','holaa','q onda','que ondaaa','que onda el directo'),('na','naaaa','nah','buenaaa','god','GOOOOD','anashe','gil','parguelita','pediloo')]
bloque2 = ['maquina','fiera','idolo','amigazo','amigo','genio','titan','bestia','rey','capitan de navio','capitan de corbeta','facha','superheroe','locura','toro','pantera','streamer del año']
frases = ['como vas en ranked?','como va la cosa ?','como va todo ?','todo bien?','subis contenido en alguna plataforma?','te re banco','aguante talleres','vaya partido tio, ndeah','q comiste?','q jugas animal','algun consejo para mejorar ?','unas ganas de un mac','añadimeeee','arrancas a hacer coaching y me avisas','tirate unos factos','que juegos jugas?','que rango sos?','jugas lol?','jugas valorant?','Haces deporte?','cuantas veces por dia te pegan en tu casa?','mostrate la base de clash of clans','hace cuanto jugas fn','mcdonald o burger','a q edad arrancaste a jugar al fulbo ?','para cuando un irl ?','bancas a mrbeast?','color favorito ?','cual es tu artista favorito?', 'te gusta myke towers ?']
emotes = ['beeBobble','RareCharm','EZ','ratJAM','DanceDance','Flowie']
coinflip = random.randint(0,1)

x = len(bloque1)-1
Tercio = random.randint(0,2)
"""
parte1 = variacion al azar [ seleccion al azar ] + emote * numero 0-5
"""

def click(x=None,y=None):
    if x and y:
        win32api.SetCursorPos((x,y))
    time.sleep(.5)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)

def wintab():
    keyboard.press_and_release('win+tab')
    time.sleep(2)

def firstapp():
    wintab()
    keyboard.press_and_release('end')
    keyboard.press_and_release('enter')

def randomMsg():
    #click(1695,892)
    emote = (' '+emotes[random.randint(0,len(emotes)-1)])*random.randint(0,5)
    parte1 = bloque1[coinflip][random.randint(0,len(bloque1[coinflip])-1)]*random.randint(0,1)
    parte2 = bloque2[random.randint(0,len(bloque2)-1)]*random.randint(0,1)
    frase = frases[random.randint(0,len(frases)-1)]*random.randint(0,1)
    #correcciones
    if parte2 and frase:
        parte2 = parte2 + ', '
    if parte1 and parte2:
        parte2 = ' ' + parte2
    elif parte1 and frase:
        frase = ', ' + frase
    #logica
    if parte1 and coinflip == 0:              #| saludo + alias? + frase? + emote?
        print(parte1 + parte2 + frase + emote)#|
    elif parte1 and coinflip == 1:            #| exclamacion + emote?
        print(parte1 + emote)                 #|
    elif parte2:                              #|
        print(parte2+frase+emote)             #| alias + frase? + emote?
    elif frase:                               #|
        print(frase+emote)                    #| frase + emote?
    else:                                     #|
        print(emote*2)                        #| mucho emote

    #keyboard.press_and_release('enter')
"""
while not keyboard.is_pressed('q'):
    cont = 0
    firstapp()
    time.sleep(1)
    randomMsg(parte1)
    time.sleep(random.randint(2,30))
    cont +=1
    if cont == 15:
        cont = 0
        firstapp()
"""
randomMsg()

