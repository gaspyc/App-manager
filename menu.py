import keyboard, pyautogui, os, time, threading
from windowsfunc import *
from browsersfunc import *

run = True
browsers = {
'edge': (1,1),
'chrome': (2,2),
'Navegador Opera': (3,3),
'Opera g':(4,4),
'brave':(5,5),
'vivaldi':(6,7),
'avast':(7,7),
'Firefox':(8,8),
'Firefox Dev':(9,9),
'Waterfox':(10,10),
'Duck':(11,11)
}

sesiones = list(browsers.keys())
switch = {1:'si',0:'no'}
a,b,c,d,e,f,g,h = 0,0,0,0,0,2,'',0

def recarga(switch,b):
    while switch[b]:
        print('haciendo algo...')
        time.sleep(2)

def user(browsers):
    global run,a,b,c,d,e,f,g,h
    aperturas = ['todo','solo incognito']
    aplicaciones = ['xbox.com/es-AR/play/games/fortnite/BT5P2X999VH2','kick.com/cautt']
    while run:
        while True:
            print(f"""
            |- - - - M E N U - - - -| {g}
            |[1] abrir navegadores  | {a} / {len(browsers)}
            |[2] iniciar sesion     | {b} / {len(sesiones)*f} sesiones iniciadas
            |[3] fortnite afk       | {switch[c]}
            |[4] cambiar apertura   | modo : {aperturas[d]}
            |[5] cambiar app        | app  : {aplicaciones[e][:4]}
            |[6] mando fisico       | {switch[h]}
            """)
            x = input('seleccionar o pulse [0] para salir :')
            if x in ['1','2','3','4','5','6','0']:
                g = ''
                break
            else:
                g = f'{x} no es una opcion valida'
                os.system('cls')

        match x:
            case '1':
                for browser in browsers:
                    openbrowser(browser,aplicaciones[e])
                    a+=1
            case '2':
                pass
            case '3':
                hilo_recarga.start()
            case '4':
                d = (d + 1)%len(aperturas)
                f=2 if d==0 else 1
            case '5':
                e = (e + 1)%len(aplicaciones)
            case '6':
                h = (h + 1)%len(aplicaciones)
            case '0':
                run = False
        os.system('cls')

if __name__ == '__main__':
    time.sleep(1)
    click(770,1200)
    hilo_user = threading.Thread(target=user, args=(browsers,))
    hilo_recarga = threading.Thread(target=recarga, args=(switch,b))
    hilo_user.start()