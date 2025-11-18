#Here we go
from gpiozero import DistanceSensor, LED
from time import sleep

# Set up the sensor, LEDs, and button
sensor = DistanceSensor(echo=23, trigger=24, max_distance=2.0)
led_read = LED(18)
led_far = LED(16)

THRESHOLD_CM = 10.0
BLINK_INTERVAL = 0.5  # For normal blinking

while True:
    # Normal blinking behavior
    distance = sensor.distance * 100
    print(f"Distance: {distance:.2f} cm")

    if  distance > THRESHOLD_CM:
        led_far.on()
        sleep(BLINK_INTERVAL)
        led_far.off()
        sleep(BLINK_INTERVAL)
    else:
        led_read.on()
        sleep(BLINK_INTERVAL)
        led_read.off()
        sleep(BLINK_INTERVAL)
