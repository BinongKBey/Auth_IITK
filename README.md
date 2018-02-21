# auth-iitk
you need to install bs4, for installation just type pip install bs4 in your command prompt/ terminal

You need to put your iitk username and password at given place in auth-iitk.py

For Windows
Just run auth-iitk.py it will automatically login you and keep refreshing your connection

For linux
you can run auth-iitk.py which will login you and keep your connection active
Alternate -
You can setup a python Daemon
1) install supervisor by typing    sudo apt-get install supervisor
2) copy auth-iitk.py to /opt
3) copy auth-iitk.conf to /etc/supervisor/conf.d/
4) update supervisor list by -- sudo supervisorctl update

Now it will login automatically when you start your laptop

In case of suspending and hibernation

sudo cp IITK-resume.service /etc/systemd/system/

sudo systemctl enable IITK-resume.service
