import keyboard
import time
import vgamepad as vg

# intancia mando xbox (Xinput)
gamepad = vg.VX360Gamepad()

# acciones de mando
def Y_triangulo():
    gamepad.press_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_Y)
    gamepad.update()
    time.sleep(0.1)
    gamepad.release_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_Y)
    gamepad.update()

def B_circulo():
    gamepad.press_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_B)
    gamepad.update()
    time.sleep(0.1)
    gamepad.release_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_B)
    gamepad.update()

def A_equis():
    gamepad.press_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_A)
    gamepad.update()
    time.sleep(0.1)
    gamepad.release_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_A)
    gamepad.update()

def stick_izquierdo(x_value, y_value):
    gamepad.left_joystick(x_value=x_value, y_value=y_value)
    gamepad.update()

def stick_derecho(x_value, y_value):
    gamepad.right_joystick(x_value=x_value, y_value=y_value)
    gamepad.update()

# uso
def instrucciones():
    print("""
stick izquiedo:  | stick derecho:
w = arriba       | ⬆ = arriba
a = izquierda    | ⮕ = izquierda
s = abajo        | ⬇ = abajo
d = derecha      | ⬅ = derecha

botones:
t = y (triangulo)| u = a(equis)
y = b (circulo)  |
""")

def menu():
    while True:
        x = input("""
[0] reset
[x] fortnite afk
[p] uso manual
""").upper()
        if x == 'X':
            runAround()
        elif x == 'P':
            usarMando()
        elif x == '0':
            stick_izquierdo(0,0)
            stick_derecho(0,0)
        else:
            print('respuesta no valida')

def runAround():
    ix_value,iy_value = 0,-32768
    dx_value,dy_value = -32768,10000
    stick_izquierdo(ix_value, iy_value)
    stick_derecho(dx_value, dy_value)
    print("corriendo")
    while keyboard.is_pressed('q') == False:
        time.sleep(60)

def usarMando():
    señal = input("""
[h] ver controles
[x] volver
""").upper()
    if señal == 'H':
        instrucciones()
    elif señal == 'X':
        return
    else:
        pass
    print("en uso")
    while True:
        #sticks (-32768 a 32767)
        ix_value,iy_value = 0,0
        dx_value,dy_value = 0,0

        #stick izquiedo
        if keyboard.is_pressed('w'):
            iy_value = -32768
        elif keyboard.is_pressed('s'):
            iy_value = 32767
        if keyboard.is_pressed('a'):
            ix_value = -32768
        elif keyboard.is_pressed('d'):
            ix_value = 32767

        #stick derecho
        if keyboard.is_pressed('up'):
            dy_value = -32768
        elif keyboard.is_pressed('down'):
            dy_value = 32767
        if keyboard.is_pressed('left'):
            dx_value = -32768
        elif keyboard.is_pressed('right'):
            dx_value = 32767

        stick_izquierdo(ix_value, iy_value)
        stick_derecho(dx_value, dy_value)
        time.sleep(0.1)
        # botones
        if keyboard.is_pressed('t'):
            Y_triangulo()
            time.sleep(0.1)  # Evita múltiples pulsaciones seguidas
        if keyboard.is_pressed('y'):
            B_circulo()
            time.sleep(0.1)
        if keyboard.is_pressed('a'):
            A_equis()
            time.sleep(0.1)

        time.sleep(0.1)
#programa
def main():
    menu()

if __name__ == "__main__":
    main()
