import network
from machine import Pin
from time import sleep
from umqtt.simple import MQTTClient
import _thread

# Definimos las propiedades de conexión con el servidor
MQTT_BROKER = "broker.hivemq.com"
MQTT_CLIENT_ID = ""
MQTT_USER = ""
MQTT_PASSWORD = ""
MQTT_TOPIC = "NNAT/led"
MQTT_PORT = 1883

# Declaración del motor
IN1 = Pin(26, Pin.OUT)
IN2 = Pin(25, Pin.OUT)
IN3 = Pin(33, Pin.OUT)
IN4 = Pin(32, Pin.OUT)

pins = [IN1, IN2, IN3, IN4]

sequence_1 = [[0, 0, 0, 1], [0, 0, 1, 0], [0, 1, 0, 0], [1, 0, 0, 0]]
sequence_2 = [[1, 0, 0, 0], [0, 1, 0, 0], [0, 0, 1, 0], [0, 0, 0, 1]]

# Declaro mis variables para los leds
led_1 = Pin(12, Pin.OUT)
led_1.value(0)
led_2 = Pin(13, Pin.OUT)
led_2.value(0)

# Función para conexión WiFi
def conectar_wifi():
    print("Conectando", end="")
    sta_if = network.WLAN(network.STA_IF)
    sta_if.active(True)
    sta_if.connect("NoahT", "Noah9999")  # Modifica el nombre y la contraseña de tu red
    while not sta_if.isconnected():
        print(".", end="")
        sleep(0.3)
    print("WiFi conectada!")

# Variable global para controlar el estado de los LEDs
parpadeando = False

# Función que controla el comportamiento de los LEDs
def controlar_leds():
    while parpadeando:
        led_1.value(1)
        led_2.value(0)
        sleep(0.5)
        led_1.value(0)
        led_2.value(1)
        sleep(0.5)

# Función que enciende y apaga un led de acuerdo al mensaje recibido del servidor
def llegada_mensaje(topic, msg):
    global parpadeando  # Hacer referencia a la variable global
    print("Mensaje: ", msg)
    if msg == b'1':
        parpadeando = True
        _thread.start_new_thread(controlar_leds, ())  # Iniciar hilo para el parpadeo
    elif msg == b'0':
        parpadeando = False  # Detener el parpadeo
        led_1.value(0)
        led_2.value(0)  # Apagar ambos LEDs
    else:
        print("Mensaje no válido")

# Función de suscripción
def suscribir():
    client = MQTTClient(
        MQTT_CLIENT_ID,
        MQTT_BROKER,
        port=MQTT_PORT,
        user=MQTT_USER,
        password=MQTT_PASSWORD,
        keepalive=0
    )
    client.set_callback(llegada_mensaje)
    client.connect()
    client.subscribe(MQTT_TOPIC)
    print("Conectado a: ", MQTT_BROKER, " y en el tópico: ", MQTT_TOPIC)
    return client

# Función para el movimiento del motor en un hilo separado
def mover_motor():
    while True:
        for step in sequence_2:
            for i in range(len(pins)):
                pins[i].value(step[i])
                sleep(0.001)

# Conexión WiFi
conectar_wifi()

# Creamos el MQTT y nos suscribimos a un tópico
client = suscribir()

# Iniciar el hilo para el motor
_thread.start_new_thread(mover_motor, ())

# Ciclo principal donde el cliente MQTT espera mensajes
while True:
    client.wait_msg()
