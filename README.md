# AUTH-IITK

This is a new updated code for auto login to IITK network

## Adding your login credentials
You need to put your iitk username and password in auth-iitk.py (probably line no. 9 or 10)

### Running the code (temporary)

For Windows:
Just run ```python3 auth-iitk.py``` it will automatically login you and keep refreshing your connection.

For linux users:
Run ```python3 auth-iitk.py``` in the terminal, which will log you in and keep your connection active

## Running the code in windows in background: 

You can run ```pythonw auth-iitk.py```

# Alternate Once for all/Permanent (for linux only)- 

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
