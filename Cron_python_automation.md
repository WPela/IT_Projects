**Cron**

I want to shedule python code to run every hour and download data from API and save it as CSV file.

First I checked if I have Cron installed using *sudo apt-get install cron*.

![image](https://github.com/WPela/IT_Projects/assets/62253932/ebc081d6-c03d-4779-b54f-a1733ea74362)

Because I have it installed, next step is to verify if python is installed. *python3 --version*

![image](https://github.com/WPela/IT_Projects/assets/62253932/ba1ae5bd-0927-49be-b851-d8a136901acb)

Now I will open crontab editor *crontab -e* and add necessary information on the bottom to schedule python script.

![image](https://github.com/WPela/IT_Projects/assets/62253932/ed410604-5aba-47f1-a2b2-d6b24365d281)

In cronetab, type in line where you specify date (asterisk "*" means every), environment and location of python script, which you want to schedule.

![image](https://github.com/WPela/IT_Projects/assets/62253932/c0b6cb56-e23c-49e8-90ad-ecff83f8c162)


Now, scheduled script should run every hour 10min before full hour.
