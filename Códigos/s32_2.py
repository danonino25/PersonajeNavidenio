from machine import Pin, PWM, I2C
from time import sleep, sleep_ms
import _thread
import ssd1306
from servo import Servo

# Configuración del zumbador
buzzer = PWM(Pin(17), freq=440, duty=512)  # Utiliza un rango más amplio (0-1023)

# Función para manejar el sonido
def tono(frecuencia, tiempo):
    buzzer.freq(frecuencia)
    buzzer.duty(512)  # Ajusta según sea necesario
    sleep(tiempo)
    # Pausa adicional al final de cada nota para evitar mezcla
    sleep(0.1)

# Melodía
melodia_jingle_bells = [
    (659, 0.5), (659, 0.5), (659, 1), (659, 0.5), (659, 0.5), (659, 1),
    (659, 0.5), (698, 0.5), (784, 1), (587, 0.5), (659, 0.5), (698, 0.5),
    (784, 0.5), (784, 0.5), (784, 1), (784, 0.5), (784, 0.5), (784, 1),
    (784, 0.5), (698, 0.5), (659, 0.5), (587, 0.5), (523, 0.5), (523, 0.5), (523, 1),
]

# Variables de control
reproduciendo = False

# Función para reproducir melodía en un hilo
def reproducir_melodia():
    global reproduciendo
    while True:
        if reproduciendo:
            for nota in melodia_jingle_bells:
                tono(nota[0], nota[1])

# Función para la animación en la pantalla OLED
def animacion_oled():
    i2c = I2C(scl=Pin(22), sda=Pin(21))
    oled_width = 128
    oled_height = 64
    oled = ssd1306.SSD1306_I2C(oled_width, oled_height, i2c)

    mensaje1 = "  Feliz Navidad"
    mensaje3 = "     JoJoJo"

    while True:
        for i in range(oled_height):
            oled.fill(0)
            oled.text(mensaje1, 0, i)
            oled.text(mensaje3, 0, oled_height // 2 + i)
            oled.show()
            sleep_ms(50)

# Función para el movimiento del servo
def movimiento_servo():
    motor = Servo(pin=18)
    while True:
        motor.move(180)
        print("Posición del servo: 180")
        sleep(0.3)
        motor.move(0)
        print("Posición del servo: 0")
        sleep(0.3)

# Iniciar los hilos
_thread.start_new_thread(reproducir_melodia, ())
_thread.start_new_thread(animacion_oled, ())
_thread.start_new_thread(movimiento_servo, ())

# Mantener el programa principal a la espera
while True:
    # Añade una pausa para permitir que el intérprete MicroPython gestione los hilos
    sleep(1)
    # Reiniciar la melodía y el servo
    reproduciendo = True
    sleep(10)  # Ajusta la duración según sea necesario
    reproduciendo = False
    sleep(1)  # Pausa adicional para permitir que los hilos se detengan completamente
