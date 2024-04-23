# auth-iitk

New updated code for auto login to IITK network

you need to install *bs4*, for installation just open your command prompt/ terminal, type -
 
```pip install bs4```

Note: make sure you have pip3 installed. If not, install it using the command: ```sudo apt install python3-pip```

Note: In some newer ubuntu systems, you need to ```sudo pip install bs4``` to make it work.

You need to put your iitk username and password at given place in auth-iitk.py

For Windows
Just run auth-iitk.py it will automatically login you and keep refreshing your connection.

For linux
you can run auth-iitk.py which will login you and keep your connection active

Alternate Once for all -
You can setup a python Daemon

### 1) install supervisor by typing
```sudo apt-get install supervisor```

### 2) copy auth-iitk.py to 
``` sudo cp auth-iitk.py /opt ```

### 3) copy auth-iitk.conf to /etc/supervisor/conf.d/
``` sudo cp auth-iitk.conf /etc/supervisor/conf.d/ ```

### 4) update supervisor list -- 
```sudo supervisorctl update```

Now it will login automatically when you start your laptop

In case of suspending and hibernation if you want it to restart

``` sudo cp IITK-resume.service /etc/systemd/system/```

``` sudo systemctl enable IITK-resume.service```
