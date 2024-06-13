# auth-iitk

This is a new updated code for auto login to IITK network

Run the following commands by opening the terminal in your folder.

### Prerequisites:
 - make sure you have pip3 installed. If not, install it using the command: ```sudo apt install python3-pip``` in terminal
 - Now, using pip3, you need to install *bs4* for installation (You can skip it if you have it). To install run: ```pip install bs4``` in terminal
 - Note: In some newer ubuntu systems, you need to ```sudo pip install bs4``` to make it work.

### Adding your login credentials
You need to put your iitk username and password in auth-iitk.py (probably line no. 9 or 10)

### Running the code

For Windows:
Just run ```python3 auth-iitk.py``` it will automatically login you and keep refreshing your connection.

For linux users:
Run ```python3 auth-iitk.py``` in the terminal, which will log you in and keep your connection active

### Running the code in windows in background: 

You can run ```pythonw auth-iitk.py```

### Alternate Once for all (for linux only)- 

You can setup a python Daemon

#### 1) install supervisor by typing
```sudo apt-get install supervisor```

#### 2) copy auth-iitk.py to 
``` sudo cp auth-iitk.py /opt ```

#### 3) copy auth-iitk.conf to /etc/supervisor/conf.d/
``` sudo cp auth-iitk.conf /etc/supervisor/conf.d/ ```

#### 4) update supervisor list -- 
```sudo supervisorctl update```

Now it will login automatically when you start your laptop

#### Restart code in case of suspend or hibernation (recommended for linux)
In case of suspending and hibernation if you want it to restart

``` sudo cp IITK-resume.service /etc/systemd/system/```

``` sudo systemctl enable IITK-resume.service```
