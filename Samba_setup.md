**Samba setup**

We will set Samba tool now to share disk which is connected to raspberry. Because I want to reach terminal via my laptop, I will use PuTTY to connect to my raspberry.

Before I connect, I need to know ip of the device. In raspberry terminal ![image](https://github.com/WPela/IT_Projects/assets/62253932/d92868f5-c729-4227-8297-e8e70789f81c), type in *ifconfig* and write down the ip. Till this moment, we do not need to use GUI of the raspberry.

![image](https://github.com/WPela/IT_Projects/assets/62253932/10714025-9e4a-4f68-83a4-616f593be239)

In PuTTY type in ip of the device and press "Open". 

![image](https://github.com/WPela/IT_Projects/assets/62253932/61f39f30-c7f5-4156-8ff8-610af3eac9ce)

Raspberry will ask for user's name and password. *Important* While typing password, you will not see characters appearing - just type in password and press enter.

Update software using *sudo apt update* command. In case of packages which can be upgraded, additionally use *sudo apt full-upgrade*.

Now we will move to samba. Type in *sudo apt install samba*. In case of questions to install additional elements, pres *y*. Also you will see progress bar on the bottom.

Once done, check status with *sudo systemctl status smbd* command.

Use command *df -h* to check location of the connected disk.
![image](https://github.com/WPela/IT_Projects/assets/62253932/9e4f12f4-dd68-4b16-b131-fc1087c17f5b)

In this case it is /dev/sda1 and I will create new directory using *sudo mkdir /media/shared_disk* command. 

Verify id -u and id -g 
![image](https://github.com/WPela/IT_Projects/assets/62253932/20918f1e-f856-4d43-85a6-d618ddcf2bab)


Now map the disk to the directory using *sudo nano /etc/fstab* command and type locations and settings similar to the line on the screenshot.
![image](https://github.com/WPela/IT_Projects/assets/62253932/fb43bb9d-f6b4-4f6b-ab37-8a664809fbf8)

Reboot Raspberry after that.


Open samba config now *sudo nano /etc/samba/smb.conf* and add shared directory as below:
![image](https://github.com/WPela/IT_Projects/assets/62253932/c55be9da-d5a1-4abe-99d1-5ff72c95d12e)

Restart password with *sudo passwd -a username*.

At the end restart samba *service smbd restart*.
