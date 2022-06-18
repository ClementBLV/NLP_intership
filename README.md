# NLP_intership


**Introduction :**

Dans le cadre du contrôle financier l’AMF est amenée à examiner les rapports publiés par des centaines d’entreprises pour en tirer les informations et les indicateurs nécessaires. Or ces rapports font plusieurs centaines de pages. Il est donc impossible pour les agents de l’AMF de parcourir l’ensemble de ces rapports. Jusqu’à présent ils se contentaient d’examiner de petits échantillons. Pour parvenir à examiner l’ensemble de ces rapports il est donc primordial de réduire le spectre de recherche et d’extraire les informations clés des rapports. Pour ce faire des algorithmes de « question answering » ou de « summarization » peuvent d’être envisagés. Néanmoins ces algorithmes ne peuvent qu’extraire les données présentes sous forme textuelle. Les données présentes dans les tableaux leur sont quant à elle innascibles. Malheureusement ces données possèdent généralement de nombreuses informations très importantes, il est donc crucial de pouvoir les extraire et les interpréter.

Ce programme permet de dire si oui ou non une page (PDF, JPG, PNG) possède un tableau. Il retourne True si la page possède un tableau et False sinon. Il peut ainsi être utilisé dans un document pour identifier les pages possédant un tableau, localiser ce tableau. Puis il suffit d’appliquer un algorithme OCR pour récupérer le texte contenu dans le tableau, ou directement extraire ce tableau.

**Programme :**

Un premier collab https://colab.research.google.com/drive/1-VlA04t33pdPXv3IJJ9IfAgEhDAUIUJo?usp=sharing , est un collab de démonstration étape par étape des méthodes utilisées. Tous les modules utilisés ainsi que les méthodes qui en découlent y sont implémenté et détaillées clairement. Des exemples visuels sont aussi présents pour un rendu plus concret. Le dataset utilisé est un dataset « maison » constitué de pdf avec des tableaux, des images de tables (Cat8.pdf), des scans jpg et png de pdf avec et sans tableaux. Le dataset est directement importé par le collab depuis GitHub.

Un deuxième collab (https://colab.research.google.com/drive/1TRVzwZcqeBc1eQ5jAkwi-ER-HY7qrW-T?usp=sharing) est beaucoup moins détaillé et importe directement les méthodes réalisées sous forme d’un module python. Son but est de traiter directement les documents sans explication. Le dataset utilisé est un ensemble de documents pdf et jpg (sample).

**Utilisation :**

**_ATTENTION :_** pour importer les modules il faut lancer la première cellule contenant les !pip install. Il faut le faire DEUX fois. Une première fois (qui peut prendre 5 à 10 min selon les appareils et ce qui y est installer). Une fois la première exécution terminer il faut RELANCER LE RUNTIME, cela se fait en cliquant sur le bouton qui s’affiche en bas des logs d’importation ou en allant dans le menu en haut à droite et en cliquant sur « Exécution » puis « Redémarrer l’environnement d’exécution ». Une fois cela fait il faut relancer la même cellule pour finaliser l’installation.

Une fois cette installation fait, l’evironment peut être exécuter librement. Des cellules se chargent d’importer directement ce qu’elles ont besoin depuis GitHub.

Les bibliothèques utilisées ne fonctionnent qu’avec des GPU (d’où l’utilisation de google collab). Il convient donc de se connecter à un GPU (Exécution – Modifier le type d’exécution – GPU). 

