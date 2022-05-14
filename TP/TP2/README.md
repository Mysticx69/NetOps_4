# Compte rendu TP2

## Réponse aux questions du TP2 (Voir code pour le reste) => le fichier oldnetmiko.txt contient des bouts de codes permettant de répondre à différentes questions de ce TP
<br/>

### 1.9 -Automatisation réseau avec Paramiko
---

</br>

13. Commentez la ligne suivante de votre script : time.sleep(.5) et
exécutez le script. Que se passe-t-il ? Pourquoi ?
    * **On ne voit pas le résultat de la commande car on demande l'output trop tôt; le time sleep permet de laisser le temps au switch de lancer et d'afficher le résultat de la commande**
</br>

14) Modifiez la valeur de la variable nbytes à 500 et exécutez le script.
Que se passe-t-il ? Pourquoi ?
    * **On ne reçoit maintenant plus que 500 octets donc l'output est tronqué et on obtient que les premieres lignes.**
  
</br>

---

### 1.10 - Automatisation réseau avec netmiko
---

</br>


24. Affichez la variable net_connect. Que contient la variable ? Quels
sont les attributs de la variable ?
    * **Un objet netmiko <netmiko.cisco.cisco_ios.CiscoIosSSH object at 0x7fec169d3310>**

</br>

25. Quelle méthode de l’objet net_connect permet d'exécuter des
commandes “show” ? Affichez l’état des interfaces du routeur R1 depuis
le script run_netmiko.
    * **La méthode send_command(commands) de l'objet net_connect permet cela**
  

</br>


26.  Utilisez le paramètre use_textfsm=True à la commande de la
question 25. Affichez le résultat, qu’observez-vous ?
     * **Cela permet de transformer l'output en un dictionnaire**

</br>


27.  Affichez la table de routage du routeur R1 en utilisant le paramètre
textfsm. Quel est le format de données retourné ?
     * **Format de donnée : Dictionnaire**

</br>


29. Quelle méthode de l’objet net_connect permet d'exécuter des
commandes en mode config ?
    * **La méthode  send_config_set(commmands) permet d'éxécuter des commandes en mode config**

</br>

31.  b) Quelle est l’autre option possible pour déployer ce fichier de
configuration depuis netmiko?
     * **La méthode send_config_from_file(file) permet de déployer un fichier de conf**

</br>

---

### 1.11- Automatisation réseau avec Napalm
---

</br>

41. Quel est la méthode de l’objet device permettant d’envoyer une
commande show ? Exécutez la commande permettant de récupérer
l’état des interfaces du routeur R1.
    * **La méthode cli de l'objet device permet d'envoyer une commande.**

</br>


42. Quel est le format de sortie de la commande à la question 42 ?
Quelle est la clé utilisée ?
    * **Le format est un dictionnaire avec comme clé la commande envoyé en argument de la méthode cli()**

</br>


43. Quelle est la seconde méthode permettant de lire les données de
configuration du routeur ?
    * **La méthode get_config()**

</br>

44. Quel est le format de sortie de la commande à la question 43 ?
    * **L'objet retourné est un dictionnaire avec une clé pour chaque configuration stockée (running ; candidate ; startup) Ces dernières sont en format string**

</br>

45. b) Exécutez la commande show ip int brief sur le routeur R1 , que
remarquez-vous sur la ligne des interfaces loopback 1 et
loopback 2? Comment expliquer cette différence ?
    * **On constate que l'onglet METHOD utilisé est TFTP et non NVRAM comme les autres, parce que nous avons envoyé une commane via napalm (et donc en TFTP)**