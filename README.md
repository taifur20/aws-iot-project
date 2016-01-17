# aws-iot-project
Control your things by remote switch
Before working with the code you can follow the link: 
https://github.com/aws/aws-iot-device-sdk-js

Two program is used for the project. One is Node.js project used for publisher. aws-iot-device-sdk is used for the project.
You need to install Node.js and aws-iot-device-sdk to your Raspberry pi.

# Installing aws-iot-device-sdk

Installing with npm:
<pre>
npm install aws-iot-device-sdk
</pre>
<p strong>Installing from github:</p>
<pre>
git clone https://github.com/aws/aws-iot-device-sdk-js.git
cd aws-iot-device-sdk-js
npm install
</pre>

#Installing Node.js v4.0.0 on a Raspberry Pi (All Models)

Raspberry Pi Model A, B, B+ and Compute Module
<pre>
wget https://nodejs.org/dist/v4.0.0/node-v4.0.0-linux-armv6l.tar.gz
tar -xvf node-v4.0.0-linux-armv6l.tar.gz
cd node-v4.0.0-linux-armv6l
</pre>

Raspberry Pi 2 Model B
<pre>
wget https://nodejs.org/dist/v4.0.0/node-v4.0.0-linux-armv7l.tar.gz
tar -xvf node-v4.0.0-linux-armv7l.tar.gz
cd node-v4.0.0-linux-armv7l
</pre>

Copy to /usr/local
<pre>
sudo cp -R * /usr/local/
</pre>
