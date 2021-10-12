# original code here https://domopi.eu/reconnecter-automatiquement-votre-raspberry-pi-au-wifi/

#!/bin/bash

# sudo vi /usr/local/bin/WifiRebooter.sh

# L'adresse IP du serveur que vous voulez pinger
SERVER=8.8.8.8

# Envoyer seulement 2 pings, et envoyer la sortie vers /dev/null
ping -c2 ${SERVER} > /dev/null

# Si le code retour du ping ($?) est différent de 0 (qui correspond à une erreur)
if [ $? != 0 ]
then
    # Relancer l'interface wifi
    ifdown --force wlan0
    ifup wlan0
fi

# sudo chmod +x /usr/local/bin/WifiRebooter.sh
# */5 *   * * *   root    /usr/local/bin/WifiRebooter.sh
