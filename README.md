# ConferenceBadge
Pi Zero ScrollPHat Conference Name Badge Python Script
##Installation
1. Run command curl -sS https://get.pimoroni.com/scrollphat | bash and install all examples and modules
2. Place boot file of choice in Pi's home user Desktop (/home/pi/Desktop/boot_(name).py)
3. Install Webmin by using the commands found here: https://gist.github.com/SammyHerring/7e2efefa94cd966b329c 
4. Setup Scheduled Cron Job on boot from Webmin (as installed in step 3) that uses the following command: sudo python "/home/pi/Desktop/boot_(name).py"
