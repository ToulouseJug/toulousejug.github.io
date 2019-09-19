---
title: Soirée Loom & Spring Cloud
date: 2019-09-05
host: epitech
sponsors: [ippon, monkeypatch]
partners: [digitalocean, jetbrains]
promotions: []
authors: [abos]
---

Pour attaquer cette nouvelle saison, un aperçu du Projet Loom par moi-même, et une présentation de Spring Cloud par un
speaker bien connu du JUG.

Malheureusement, étant speaker lors de cette soirée, il m'a été impossible d'enregistrer ma présentation sur Loom, et
la présentation sur Spring Cloud a été enregistrée sans micro-cravate sur la caméra n°2, d'où une qualité d'image et de son
inférieures à d'habitude.

### La concurrence sans s’emmêler les ficelles avec Project Loom - par Arnaud Bos ({{< twitter abos >}})

Le domaine de la programmation concurrente utilise le champ lexical de la filature et nous met les nerfs en pelote avec des concepts qui s'entrelacent : fibers, threads, lightweight-threads, green threads, loom...
Peut-être avez vous également entendu parler de coroutines ? Rassurez-vous, tout est lié.

Au fil de cette présentation (em)mêlée d'exemples de code, vous découvrirez le projet Loom qui a pour vocation d'apporter à la JVM des "mécanismes léger de concurrence", ainsi que des API plus haut niveau pour broder dessus.

Nous aborderons ensemble l'origine de Loom et ses récents prototypes. Vous vous apercevrez que son maillage va au delà de "simples" primitives et peut nous amener jusqu'à révolutionner la concurrence sur la JVM.

Et en attendant la révolution, sans tirer trop sur la corde, vous verrez comment on peut juste utiliser Quasar.

Référence CfP : https://github.com/ToulouseJug/call-for-paper/issues/39

### Microservices avec Spring Cloud - par Florian Beaufumé ({{< twitter fbeaufume >}})

Une architecture en microservices apporte de nombreux bénéfices mais pose plusieurs difficultés à cause de la nature distribuée de l'application.

Pour nos applications Java ou Kotlin basées sur Spring Framework et Spring Boot, il existe des solutions apportées par les projets Spring Cloud. Elles ont l'avantage d'être neutres par rapport à l'orchestrateur ou au cloud utilisé.

A travers une majorité de slides, mais aussi quelques démonstrations, nous allons expliquer ces difficultés et montrer la mise en oeuvre étape par étape des solutions de Spring Cloud :

* Centralisation de la configuration avec Spring Cloud Config
* Automatisation et fiabilisation des communications entre services avec Spring Cloud Netflix
* Exposition des services aux clients avec Spring Cloud Gateway
* Corrélation des logs avec Spring Cloud Sleuth

Référence CfP : https://github.com/ToulouseJug/call-for-paper/issues/30

Vidéo : {{< youtube wf80O7TJ12k >}}
