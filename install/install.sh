#!/usr/bin/bash

echo -n "Enter the username to start the installation: "
 read user

echo "Installation is starting"

apt update 

apt install python3-gi python3-gi-cairo gir1.2-gtk-3.0 -y

apt update

apt install libgirepository1.0-dev gcc libcairo2-dev pkg-config python3-dev gir1.2-gtk-3.0 -y

mkdir /home/$user/.local/share/grupy_db/
cp /home/$user/grupy/data/imc.db /home/$user/.local/share/grupy_db/
cp -r /home/$user/grupy /usr/local/bin/
cd  /usr/local/bin/grupy/compiled/
rm -rf UtilGtk
ln -s /usr/local/bin/grupy/util/compiled/ UtilGtk
chmod +x /usr/local/bin/grupy/compiled/imc.pyc
cp /usr/local/bin/grupy/install/imc.desktop /usr/share/applications/
chmod +x /usr/share/applications/imc.desktop
echo "Installation completed"
