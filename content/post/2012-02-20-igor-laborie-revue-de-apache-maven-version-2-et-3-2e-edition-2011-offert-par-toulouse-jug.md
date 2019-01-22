---
title: Igor Laborie - revue de "Apache Maven, Version 2 et 3, 2e édition 2011" offert par Toulouse JUG
date: 2012-02-20
---

Apache Maven, Version 2 et 3, 2e édition

<!-- more -->

[{{< centeredimage local="true" alt="Apache Maven, Version 2 et 3, 2e édition" src="9782744024948.jpeg" >}}](https://www.pearson.ch/Informatik/PearsonFrance/EAN/9782744024948/Apache-Maven)

### Présentation rapide

Ce livre est écrit par Nicolas de Loof (CloudBees) et Arnaud Héritier
(eXo Platform), avec de nombreuses participations de la communauté francophone.

Pour rappel Arnaud était venu nous présenter [Maven 3 lors de la session du 16 Mars 2011](http://www.slideshare.net/aheritier/toulouse-jug-apache-maven-3x).
J'espère que l'on verra Nicolas bientôt sur Toulouse, par exemple pour nous
présenter Cloudbees ?

**UPDATE : Nicolas viendra justement nous présenter CloudBees jeudi 15 mars
2012, pratiquement un an jour pour jour après la venue d'Arnaud.  
Réservez votre soirée !**

Ce livre présente l'ensemble des concepts de Maven 2 et 3. Il fait le tour des
possibilités de cet outil via un cas concret que l'on suit de bout en bout en
utilisant les plugins principaux.

Ce livre ne fait pas une revue détaillée de tous les plugins de Maven, ni de
leurs options.

### Revue

Bien que je fréquente depuis longtemps Maven je n'ai jamais eu l'occasion
d'approfondir le sujet. J'attendais donc de compléter mes connaissances et
d'apprendre les bonnes pratiques de Maven.

Contrairement aux livres informatiques que je lis traditionnellement ce livre
utilise une approche récréative en faisant intervenir de nombreux acteurs de la
communauté de Maven. Ceci rend la lecture plus agréable.

En partant d'un cas concret, il met en évidence la puissance de Maven en
expliquant et démontrant les bonnes pratiques, j'avais déjà rencontré beaucoup
de ces situations, l'apprentissage en est donc bien meilleur.

Cet ouvrage a globalement comblé mes attentes sur Maven. Il me parait important
de mettre en pratique les notions abordées sur un projet concret en parallèle
de la lecture.

J'ai trouvé particulièrement intéressant les chapitres qui prennent du recul, en
particulier le chapitre 15 qui dresse qui bilan, ainsi que le chapitre 16 qui
essai de voir plus loin (OSGi, Modules Java).

Un problème courant lorsqu'on parle des outils comme Maven, ANT, Gradle, ... et
qu'il est difficile d'isoler l'outil par rapport aux autres outils de la forge
logiciel (SCM, Intégration Continue, Procès de livraison, ...). Dans ce livre
on retrouve une présentation rapide de l'intégration continue (Continuum, Hudson
et Jenkins) et des outils de qualité (PMD, Findbugs, Sonar).

De mon point de vu, les outils d'intégration continue prennent le pas sur Maven
pour ce qui concerne le contrôle qualité voir du processus de livraison
(Continuous Delivery). Cela aurait été peut être hors sujet, mais j'aurai
préférer un chapitre complet sur Jenkins mettant en oeuvre tout ceci.

Du coté test JavaEE, j'aurai aimer avoir plus de détail sur Arquillian qui
aujourd'hui me semble être la meilleur solution de test dans ce contexte.

Dans le chapitre 14: "Un nouveau projet démarre", il manque peut être une petite
note sur les outils comme Springs Roo ou JBoss Forge, et d'expliquer le
positionnement des archétypes Maven vis à vis de ces outils.

### Conclusion

Les plus :

* Livre en français, avec un ton récréatif
* Complet pour les bonnes pratiques
* Les situations sont réelles
* Prise de recul sur Maven

Les moins :

* Il y a beaucoup d'exemples, j'aurai bien aimé pouvoir télécharger les sources.
* Plus j'utilise Maven, plus j'ai l'impression que c'est l'outil des années
  2000's, et pas celui des 2010's.

De mon point de vue s'il faut lire un seul bouquin sur Maven, c'est celui la.