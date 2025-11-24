# NSANTOS-RASP-PI

The purpose of the following design, is to have a system that can indicate to us how far or close an object is to a sensor. Although we get a numerical output from the sensor onto our Pi (as to how far or close an object is), how would we be able to tell the difference if we had no way to display said output? Well with lights of course! The following system is a very simplified design, but it sets a good presidence for how distance-reading devices work.

**ATTENTION:** Do not connect/disconnect wires to the raspberry Pi while it is on. I strongly suggest you setup everything first before connecting the Pi to a power source.

<ins>You will need</ins>  
-1 Raspberry Pi  
-1 Breadboard  
8 male to female jumper wires  
-1 HC-SR04 Sensor  
-1 470Ohm resistor  
-1 330Ohm resistor  
-2 220Ohm resistor(s)  
-2 LED (preferably two different colors)  

<ins>Stage 1</ins> (Setting up the sensor)

Connect your components as displayed by the screenshot below. Your grounding and GPIO connections should be the same as mine - if you choose to use different pins,
you will then need to modify your code (covered in stage 3) to address the GPIO differences. 
  
**WARNING:** Please ensure you are using the correct resistors, otherwise the sensor will overheat (disconnect the power from the Pi if anything feels unreasonably warm or smells off).
<img width="1267" height="466" alt="Screenshot 2025-11-24 112909" src="https://github.com/user-attachments/assets/5682e6b3-d9d1-4379-a57e-cc64b66051bb" />


<ins>Stage 2</ins> (Setting up the LEDs)  
Connect your LEDs according to the screenshot below.

<img width="945" height="590" alt="Screenshot 2025-11-24 114838" src="https://github.com/user-attachments/assets/096eea67-2262-41c4-9e63-a4ad2c0576ab" />  

  
<ins>Stage 3</ins> (Inputting your code needed to run the program)
1. Now that you have everything connected to your Pi and Breadboard, go ahead and connect your Pi to the power.
2. Login to the Pi and open the Thotty application.
3. Navigate to the main.py file found in the NSANTOS-RASP-PI repository.
4. Copy the code found in the main.py file into the Thotty application.
5. Run the program.
6. Now take something, like a sticky note, and move it towards the sensor. If everything was set up properly the green LED should blink if the object is less than 10cm away - if the object is sensed to be further than 10cm away the red LED will blink.
