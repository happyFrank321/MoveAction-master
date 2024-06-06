# Pre-install
Installing packages using the Debian-based distros example:
```
apt install python3.10-dev libssl-dev libmysqlclient-dev build-essential
```
Installing packages using the Red Hat-based distributions example:
```
sudo dnf install python3.10-devel openssl-devel
sudo dnf groupinstall "Development Tools" "Development Libraries"
sudo dnf install make automake gcc gcc-c++ kernel-devel
```

# Install
```
python3.10 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
cp config_example.py config.py
```


