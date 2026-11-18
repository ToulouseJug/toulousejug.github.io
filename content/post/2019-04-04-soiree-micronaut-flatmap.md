---
title: Soirée Micronaut & flatMap
date: 2019-04-04
host: epitech
sponsors: [ippon, monkeypatch]
partners: [digitalocean, jetbrains]
promotions: []
authors: [abos]
---

Et voici les vidéos de la soirée d'avril où il a été question de [Micronaut](https://micronaut.io/)
et des boucles `for` et autres patterns d'itération/récursion.

> **Je tiens à vous prévenir :** la qualité des vidéos de cette soirée laisse à désirer...  

Mea culpa :

* le son n'est pas aussi clair que ce que nous avons pu obtenir par le passé, c'est
  parce que j'avais oublié un cable crucial pour l'installation : mon cable TRRS.
* de plus, la soirée s'étant déroulée dans une salle différente de celle qui nous est habituellement mise à disposition,
  j'ai eu quelques problèmes de mise en place de la caméra (angle) ainsi que des problèmes **d'éclairage**.
  
La deuxième présentation en particulier a subi plusieurs retouches en post-production, notamment au niveau de
l'exposition et de la saturation, pour un résultat assez décevant. Rassurez vous, la qualité du contenu est au
rendez-vous 😃

Le point positif, c'est que si la qualité de ces vidéos est en dessous de celle de nos productions habituelles,
**ces deux présentations étaient des répétition** avant qu'elles ne soient données par leurs auteurs à de plus grands
événements :

* Olivier présentera Micronaut dans un Tools in Action à [Devoxx France](https://cfp.devoxx.fr/2019/talk/WPM-6585/Micronaut,_le_framework_JVM_ultra-light_du_futur)
* Igor reparlera des boucles `for` et de `flatMap` [à SunnyTech](https://sunny-tech.io/schedule/2019-06-27?sessionId=45)

### Micronaut, le framework JVM ultra-light du futur - par Olivier Revial ({{< x pommeDouze >}})

Temps de démarrage proche de la seconde, empreinte mémoire de 10MB, pas de réflection, approche "cloud native" : autant de caractéristiques qui font du framework Micronaut le compagnon idéal de développement de vos microservices Java/Kotlin.

Si des frameworks comme Spring Boot ont grandement facilité l'écriture d'applications en permettant de générer des applications standalone et auto-configurées, ils souffrent néanmoins de l'historique Spring et de sa "lourdeur". En effet, l'injection de dépendances au runtime et la réflection rendent plus longs les temps de démarrage et font grossir l'empreinte mémoire de nos applis.

En partant de 0, Micronaut prend le contre-pied de ses prédécesseurs en se passant de la réflection et en utilisant la "Ahead-Of-Time compilation" pour des temps de démarrage en dessous de la seconde !

Pensé de base pour supporter et faciliter le développement de microservices et d'applications serverless, Micronaut offre par défaut le support de nombreux providers et outils cloud, il permet l'écriture d'applications réactives, il rend les applications facilement testables... bref, il apporte tout ce dont on a besoin pour développer des applications modernes !

Cette présentation sera un live-coding pour montrer les principales fonctionnalités et les principaux points forts du framework Micronaut.

Vidéo : {{< youtube wzGD7ThQ64o >}}

Référence CfP : https://github.com/ToulouseJug/call-for-paper/issues/32

### 🏋️‍️ Refactoring sans les `for` - par Igor Laborie ({{< x ilaborie >}})

Peut-on se passer de la bonne vieille boucle for ?
Il est toujours intéressant de creuser les alternatives comme les Stream, ou d'autres options.
Mais le plus important c'est de savoir quand il fuir cette instruction. Ou pas !

Au quotidien, les boucles sont les briques de base de notre code.
Mais on oublie souvent les alternatives comme l'API Stream, la récursivité...
C'est toujours bénéfique de prendre du recul sur le code que l'on écrit, pour analyser ce qui peut être amélioré.
Les alternatives sont elles plus lisibles ? Plus maintenables ? Plus performantes ?

Ici on se contentera de regarder ce qui se passe en Java, avec quelques incursion coté Kotlin et Scala.
Mais le propos s'adapte aux autres langages de programmation.

Vidéo : {{< youtube KjzA91jvjq4 >}}

Référence CfP : https://github.com/ToulouseJug/call-for-paper/issues/24
