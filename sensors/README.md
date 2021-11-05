## A Simple Server with Python Flask

This is a simple skeleton Flask server project that works on any of the devices supported by [balena][balena-link].

This project simply serves up a description of the group members and the name of the tutorial in the on port `:80` of the balena device(RaspberryPi Zer0).
##Team Members: Thabang Sambo

##Practical 6
Sensor Node: I must configure the Pi to sample a temperature sensor and Light-dependent resistor (LDR) connected to the ADC every 10s. 

Using the code and circuit from WP4, I must configure the Pi to do the same as it was doing before but using a Balena container to deploy the code.  

Once I have my old code working and deployed again in the Balena container. I must modify the code using Python Sockets to send the values over TCP. This will allow me to send the data to the other Pi, Pi2, which is still hosting the webserver but with improvements. Then update with the latest IP for the Pi2 web server, so that I can be able to push a rebuilt image.  

• SEND: 
This will allow the server to be able to turn on or turn off Pi1’s sending of sensor data.

• CHECK: 
Check that the client is active. Client to Server Messages (P2 to P1) 

• SENDBACK:  
Returns an acknowledgment from receiving a SEND so that the server knows the request got    through. 

• STATUS: 
The client replies to the server indicating if it's a sampling of data is active, and the time (in HH:MM: SS) at which the last sample was sent. 

• SENSORS: 
This sends back sampled sensor data, the sensed temperature value, the sensed LDR value, and the time, i.e., a timestamp, in HH:MM: SS. Data stored on the server The Pi1 will read temperature and LDR sensed light level. Stored this in as an int variable. On start-up, the server Pi2 needs to create a sensor log file to save logged sensor readings. Where the date is the current date e.g., DDMMYY (day, month, year) and time is HHMM (hour and minute). When the server Pi2 receives the SENSOR messages, it needs to add an entry to the sensor log file. insert the sensor readings in an array and save that array to the CSV on exit or when the array gets full, i.e., using the array like a buffer. Web Interface the P2 server needs to provide a simple web interface. This can be an entirely text-based interface.

The web page provides facilities:
 
• Sensor On: Turn on the sensors 
• Sensor Off: Turn off the sensors 
• Status: use the CHECK message to see the status of the Pi1 
• Log Check: This function needs to print out the last 10 samples from the current run
    to the screen.
• Log download: This allows the user to download the current sensor log file.
• Exit: This just exits the server program. It could show a screen exited.