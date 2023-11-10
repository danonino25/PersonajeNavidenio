# PersonajeAngel
Integrantes : 
Noah Noel Arredondo Torres 
Ana María Barrientos Guerrero

# Nombre del Personaje
Angel con Coro Celestial

# Materiales a utilizar

| Nombre del componente| Descripción| Cantidad| Precio|
|--|--|--|--|
| ESP32 | Microcontrolador con 30 pines con comunicación WiFi y bluetooth|1 |$ 140.00|
|Cables Dupont| Cables para conexión de prototipos de pruebas | 50 |$50.00|
|Motor a pasos | Motor a pasos unipolar con driver ULN2003 | 1 |$200.00|
|Pantalla Oled| Pantalla OLED, 1pc 1.3 pulgadas Módulo de pantalla OLED IIC | 1 |$131.00|
|Zumbador| Hilitand Zumbador piezoeléctrico de la Alarma de 3-24V DC|1|$82.00|


# Circuito en wokwi de los componentes electronicos conectados
Circuito de los leds que seran colocados en la parte de la nube mandando pequeños relampagos de luz blanca:
![image](https://github.com/danonino25/PersonajeNavidenio/assets/116208398/3896cf5d-e03a-46a2-9dc1-40ca80c3e63d)
Circuito del motor servo que controlará el movimiento de las alas del angel:
![image](https://github.com/danonino25/PersonajeNavidenio/assets/116208398/0f3e7187-bd71-481d-ac5f-33e8dd06880a)
Circuito de la microbocina que reproducirá los villancicos:
![image](https://github.com/danonino25/PersonajeNavidenio/assets/116208398/1972b424-c15d-432c-90a9-aab5b3313cee)
Circuito de la pantalla oled mediante la cual se enviaran mensajes navideños dedicado a un usuario:
![image](https://github.com/danonino25/PersonajeNavidenio/assets/116208398/9e5fb99e-f8e2-4a8b-97ef-63234ee9a77b)




# Software a utilizar 

|Nombre| Versión|Tipo de Software|
|--|--|--|
| Thonny | 4.2.1 | Software libre|
SSD1602| 1.8.1 |Software libre|

# Protitipo en dibujo
![image](https://github.com/danonino25/PersonajeNavidenio/assets/116208398/68ab59dc-b2ba-465e-91b5-eedde4628fdd)

# Comunicación
Control de Luces y Sonido a través de una Aplicación Móvil: Desarrollo de una aplicación móvil (iOS o Android) que se conecte de forma inalámbrica a la placa ESP32 a través de Bluetooth o Wi-Fi. La aplicación podría permitir a los usuarios controlar las luces y el sonido del ángel, cambiando colores, patrones de iluminación y canciones del coro celestial en tiempo real.

Control Remoto a Través de Internet: Utilizando una conexión a Internet para controlar el ángel desde cualquier lugar. Los usuarios pueden acceder a una aplicación móvil para controlar el ángel, incluso si no están físicamente cerca de él.

Sensores de Ambientales: Integrar sensores de temperatura, humedad o luz ambiental en el ángel. Los datos recopilados por estos sensores podrían ser accesibles a través de una aplicación móvil, lo que permitiría a los usuarios supervisar las condiciones ambientales en tiempo real.

Interacción Social: Implementar una función que permita a los usuarios compartir fotos o videos del ángel en las redes sociales directamente desde la aplicación móvil.

Personalización y Configuración: Ofrecer a los usuarios la posibilidad de personalizar la apariencia y el comportamiento del ángel a través de la aplicación, como seleccionar diferentes canciones para el coro, cargar imágenes personalizadas en una pantalla LED del ángel, etc.

# Arquitectura
![image](https://github.com/danonino25/PersonajeNavidenio/assets/116208398/8535edaf-f474-4d8b-a905-5107202d5360)


# Base de datos 

*Tabla 1 - "Dispositivos"*
  
  | Id_Dispositivo | Nombre_Dispositivo | Ubicacíon |
  |--|--|--|
  |1 | Noah Torres | Edificio TI|

 *Tabla 2 - "Datos Ambientales"*

   | Id_Registro | Id_Dispositivo | Fecha_Hora | Temperatura (°C) |Humedad (%)| Luminocidad(lux) | Estado |
   |--|--|--|--|--|--|--|
   | 1 | 1 | 2023-09-30 03:00:00 | 25.5 | 60 | 100 | Normal|

*Tabla 3 - "Villancicos"*
  
   | Id_Villancico | Nombre | Letra/ubi |
   |--|--|--|
   |1 | Campanas de Belén | Audio/telefono/noah/|
    
    
  
