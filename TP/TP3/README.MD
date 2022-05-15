# Compte rendu TP3

## Réponse aux questions du TP3 (Voir code pour le reste) => le fichier oldnetmiko.txt contient des bouts de codes permettant de répondre à différentes questions de ce TP
## Tout le code est organisé pour ne lancer que le main depuis la racine du tp => python3 script/main.py
<br/>

### 1.9 -Automatisation réseau avec Nornir

</br>

13. Quels sont les attributs de l’objet nr ? Pour connaître les attributs de
l’objet nr utilisez la méthode __dict__ (utilisable sur tout objet python).
Quel est le format de données de sortie ? Quelles sont les attributs de
l’objet nr ? A votre avis lequel nous permettrait d’aller lire l’inventaire
que nous avons précédemment défini (question 9) ?

    * **Les attributs sont : {'data': <nornir.core.state.GlobalState object at 0x7f6021d7cf40>, 'inventory': <nornir.core.inventory.Inventory object at 0x7f6021c78780>, 'config': <nornir.core.configuration.Config object at 0x7f60228481d0>, 'processors': [], 'runner': <nornir.vlugins.runners.ThreadedRunner object at 0x7f6021cb9c40>}**
    * **L'attribut inventory devrait nous permettre d'aller lire l'inventaire.**
  
</br>



14.  Affichez l’attribut hosts de l’attribut que vous avez trouvé à la
question 13. Quelles sont les données retournées ? Quel est le format
de données retourné ?

     * **Un print de nr.inventory.hosts nous retourne un dictionnaire contenant les hosts de notre fichier hosts.yaml**

</br>


15.  Affichez la valeur du premier élément de l’objet à la question 14.
Quelle est la valeur retournée ? Quel est le type de cette valeur
(fonction type() )?
     * **La valeur retournée contient l'host R1 et c'est une liste**

</br>

16. Utilisez la méthode dir() sur l’objet de la question 15. Parmi les
attributs affichés, lequel permet d’afficher l’adresse ip et le username /
password du host en question? Depuis quel fichier ces données ont été
récupérées ? Dans quelle section de ce fichier plus précisément?

    * **print(dir(nr.inventory.hosts.get("R1-CPE-BAT-A")))** nous donne différents attributs (username, password etc. Ces données ont été récupérées depuis les fichiers .yaml de notre dossier inventory (fichier hosts + defaults))

</br>

17. Utilisez la méthode keys() sur l’objet de la question 15. Que
voyez-vous ? Depuis quel fichier ces données ont été récupérées ?
Dans quelle section de ce fichier plus précisément ? Ajoutez une
nouvelle entrée à ce fichier, par exemple: room: 001 et exécuter de
nouveau le script.
    * **print(nr.inventory.hosts.get("R1-CPE-BAT-A").keys()) nous renvoie : dict_keys(['device_name', 'device_type', 'device_model', 'locality', 'building', 'vendor']) qui sont toutes les clés récupérées sous la clé data: de notre fichier hosts.yaml ainsi que du fichier groups.yaml (pour la clé vendor)**
    * **print(nr.inventory.hosts.get("R1-CPE-BAT-A")["room"]) nous renvoie 1.**

<br/>

22. Affichez le vendor du host R1-CPE-BAT-A en partant du code de la
question 21
    * **print(nr.inventory.hosts.get("R1-CPE-BAT-A").groups[0]["vendor"])**

</br>

23. Affichez le hostname (adresse ip) de chaque host définis dans le
fichier hosts.yaml en utilisant l’objet nr définis à la question 12.
Aidez-vous des questions précédentes.
    * **lst_host = [nr.inventory.hosts.get(item).hostname for item in nr.inventory.hosts]**

</br>

24.   Nornir nous donne la possibilité d’appliquer des filtres sur notre
inventory pour récupérer par exemple un host à partir de son hostname
par exemple. A l’aide du code suivant affichez la liste des hosts de type
router.

      * **print(nr.filter(device_type="router").inventory.hosts.keys())**

<br/>

25. Affichez à présent la liste des hosts de type router_switch
    * **print(nr.filter(device_type="router_switch").inventory.hosts.keys())**

<br/>

27.  Que retourne la variable result à la question 27 ? Aidez-vous de la
méthode type()
     * **Le type est <class 'nornir.core.task.AggregatedResult'>**


29.  Après avoir affiché result à l’aide de la fonction print_result,
qu’avez-vous remarqué ? Sur quel équipement la task s’est exécutée
par défaut ?
    * **La fonction print_result permet un affichage plus propre et plus explicite des résultats des tasks** 
    * **La task s'est exécutée sur tous les hosts**

<br/>

30.  Faites en sorte que la task hello_world s’exécute uniquement sur les
équipements de type routeur_switch.
    * **result = nr.filter(device_type="router").run(task=hello_world)**