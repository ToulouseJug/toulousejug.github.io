---
title: Soirée Java async/await
date: 2025-12-11
host: epitech
sponsors: [monkeypatch, openairlines]
partners: [jetbrains]
authors: [abos]
flyer: images/2025-12-11-soiree-java-async-await/promo.jpg
event: https://www.meetup.com/toulouse-java-user-group/events/304384746
---

Nouvelle soirée du Java User Group Toulousain le jeudi 11 décembre à 19h, chez Epitech Toulouse.

Retour d'un speaker local habitué des talks pointus autour de la concurrence, de la programmation fonctionnelle et des langages de programmation et de leurs particularités : **Didier Plaindoux** !

### Async/Await et Java - par Didier Plaindoux

Les langages populaires tels que JavaScript, Rust, Swift, Kotlin ou Dart fournissent une construction spécifique pour le style de programmation asynchrone basée sur une extension du language ce qui n'est pas la cas pour Java. Cependant, dans la dernière version de Java (21 et plus), le concept de thread virtuel a été introduit afin d'opérer une séparation nette avec le thread de la plateforme. Avec de tels threads, les I/O sont gérées différemment, les threads virtuels étant mis en attente afin de libérer ceux de la plateforme. Malheureusement, le style de programmation asynchrone n'est pas explicite lors de l'écriture de code.

Au cours de cette présentation, nous concevrons le concept de **Promesse** pour introduire le style de programmation asynchrone. Cependant, cette approche soulève un nouveau problème dans le code conçu : le *callback hell*.

La dernière pièce du puzzle sera la conception d'un **await** compatible avec les threads grâce aux threads virtuels. Nous serons alors en mesure d'écrire du code en utilisant une approche de type async/await sans introduire de nouveau mot-clé dans le langage alliant le meilleur des deux mondes à savoir un language sans méthodes "colorées" et une expressivité accrue lors de l'élaboration de code asynchrone.

Reference: [Projet HiPeAS](https://github.com/Smallibs/hpas)
