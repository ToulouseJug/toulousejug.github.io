---
title: Soirée Rust
date: 2019-11-07
host: epitech
sponsors: [ippon, monkeypatch]
partners: [jetbrains]
authors: [abos]
---

Je vous entends déjà :

> "- Rust au JUG ?! Non mais t'es pas maboule ?!"

Et bin non ! Il y a plusieurs mois est arrivé sur le CFP (https://github.com/ToulouseJug/call-for-paper/) un sujet sur
Rust orienté pour les développeurs Java.

Une occasion parfaite de mettre à l'honneur un concept cher à mon coeur : la pollinisation croisée.

### Rust pour les développeurs Java - par Simon Chemouil ({{< twitter simach >}})

Rust, tout comme Java, est né de l'objectif de proposer une alternative sûre à C++ (à l'exécution et pour la santé mentale des développeurs), mais avec une approche radicalement différente: du côté de Java, la sûreté résulte de la VM et de son Garbage Collector, alors que Rust est le premier langage mainstream à proposer un mécanisme sûr de gestion automatique de la mémoire "compile-time", tout en générant des binaires natifs. Le Rust atteint ainsi la performance de C/C++ sans les risques associés.

Dans cette présentation, il sera question de présenter Rust en partant de Java, en comparant le modèle mémoire, les primitives de design, la gestion des erreurs et le multi-threading.

Après une brève présentation "Rust par rapport à Java", où principalement seront comparés le GC de Java et le borrow checker de Rust (10 slides, ~20 mins), on ira tout droit dans le code en portant du code écrit en Java vers Rust, en comparant les points forts des deux langages.

Il s'agit d'un talk d'introduction, modérément technique, le code Java qui sera porté sera trivial (aucun framework, mais multi-threadé), et promis à la fin Duke et Ferris vont pas se taper dessus.

Référence CfP : https://github.com/ToulouseJug/call-for-paper/issues/29

Vidéo : {{< youtube BT_9NL0Ian8 >}}
