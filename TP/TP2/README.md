# Compte rendu TP2

## Réponse aux questions du TP2 (Voir code pour le reste)
<br/>

### 1.9 -Automatisation réseau avec Paramiko

</br>

13. Commentez la ligne suivante de votre script : time.sleep(.5) et
exécutez le script. Que se passe-t-il ? Pourquoi ?
    * **On ne voit pas le résultat de la commande car on demande l'output trop tôt; le time sleep permet de laisser le temps au switch de lancer et d'afficher le résultat de la commande**
</br>

14) Modifiez la valeur de la variable nbytes à 500 et exécutez le script.
Que se passe-t-il ? Pourquoi ?
    * **On ne reçoit maintenant plus que 500 octets donc l'output est tronqué et on obtient que les premieres lignes.**
  
</br>


### 1.10 - Automatisation réseau avec netmiko

</br>


24. Affichez la variable net_connect. Que contient la variable ? Quels
sont les attributs de la variable ?