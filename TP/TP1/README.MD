# Compte rendu TP1

## Réponse aux questions du TP1 (Voir code pour le reste)
<br/>

### 1.6 Préparation des variables pour le template JINJA

<br/>

1. Quels sont les éléments de configuration à réaliser pour que les
équipements du vlan 10 et du vlan 20 du bâtiment C puissent
communiquer ?
   * **Il faut configurer le router et le switch en configurant les interfaces (acces et trunk) et les deux VLAN 10 et 20 (sous interfaces pour le router)**

<br/>


2. Parmi les éléments de configuration identifiés à la question 1, quelles
sont les variables Jinja que vous avez pu identifier ?
   * **Les interfaces (interface.nom  ; interface.vlan_id ; interface.mode et interface.ip pour le router R2)**
  
<br/>


### 1.7 -Développer la fonction python permettant de lire les données définis dans les fichiers R2.json et ESW2.json

<br/>

5. Essayez d'exécuter votre script avec un chemin d’un fichier inexistant .
Que se passe-t-il ? Quel est le type d’erreur qui est levé ?
   * **Le script crash car "file not exist" car le chemin n'est pas bon**

<br/>


6. Améliorez votre code pour gérer les exceptions (erreurs) dans le cas ou
le chemin du fichier n’est pas correct par exemple
   * **On peut utiliser la clause try except pour gérer ce cas là et ainsi raise l'erreur plutot que de faire crash le script**

<br/>

 ### 1.10 - Ajout d’un nouveau bâtiment D à l’architecture

<br/>

17. Dans quel format sont les données de sortie de la fonction à la
question 16 ?
    * **Sous forme de dictionnaire**
  
<br/>


18.  D’après-vous est-il utile de modifier les templates Jinja2 pour que
votre configuration depuis yaml soit prise en compte ? Pourquoi?
     * **Inutile de modifier les templates Jinja2 car les variables sont les mêmes (noms, vlan_id, etc...) et la méthode render_config() prend aussi bien du json que du yaml en format de donnée d'entrée.**

---




