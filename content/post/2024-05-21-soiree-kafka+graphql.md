---
title: Soirée Kafka + GraphQL
date: 2024-05-21
host: epitech
sponsors: [monkeypatch, lyra]
partners: [jetbrains]
authors: [abos]
---

Nouvelle soirée chez Epitech Toulouse.

### Retex : Kafka et les traitements longs? Yes we (kaf)can - par Guillaume Andrieu

Kafka est notoirement mal adapté aux traitements longs... ou pas!
Certes la configuration par défaut est plus adaptée à traiter des tas de messages par microseconde, pourtant dans nos chaînes de traitement parfois, il y a un CPU qui donne de sa personne et qui a besoin de plus de quelques secondes pour terminer.

Dans ce cas, on modifie à la va vite `max.poll.timeout` et pis vala? Ca peut poser de sérieux soucis, surtout si on a des traitements parallélisés et de l'autoscaling.

Dans cette présentation, on verra comment on peut s'en sortir en paramétrant le client Kafka proprement, à coups de `rebalance listener` et de `partition assignor`.

Vidéo : {{< youtube id="BGbTDEl5bss" >}}

### GraphQL, une API de base de données, ou pas, ou quand même un peu - par Nicolas Lalevée

Mettre en place une API grâce à GraphQL : limites et avantages sur le dev d’un backend avec Spring GraphQL.

S'agit-il d'une API au dessus d'une connexion à une BDD ? Telle est la question posée par @hibnico.

Vidéo : {{< youtube id="zzkJu-LlJy4" >}}