---
title: Soirée Test-Safe & Oauth2
date: 2020-01-16
host: epitech
sponsors: [ippon, monkeypatch]
partners: [jetbrains]
authors: [abos]
---

Bonne année 2020 à tous les Juggers (c'est comme ça qu'on dit ?) !

Pour débuter l'année on va se faire un peu peur 👻 avec un sujet expérimental "Test-Safe",
suivi d'un tour d'oauth2.

### Programmation Test-Safe - par Adrien Piquerez ({{< x adrien_piquerez >}})

La programmation test-safe est une méthode de programmation centrée sur les tests.  
C'est du TDD, mais natif, du TDD par design !

Plus concrètement c'est l'idée que les tests sont la source du programme, et que l'implémentation est le produit des
tests. L'idée est belle, mais comment ça marche ?

Ce talk est un début d'aventure, en live coding, vers une librairie de programmation test-safe. En scala, mais pas de
panique, aucune notion de scala n'est requise pour comprendre.

Référence CFP : https://github.com/ToulouseJug/call-for-paper/issues/37

Vidéo : {{< youtube P_M49IQpcgc >}}

### Oauth2 est effrayant ? Non ! Voyons comment bien s'en servir - par Mathieu Passenaud ({{< x mathieupassenau >}})

`client_id` et `client_secret`, tout le monde connait.  
Par contre, on met quoi dans `redirect_uri`, `x-frame-options`, `Content-Security-Policy` ou `Web origins` ?  
C'est quoi un client "confidentiel" ?

Faisons un tour de oauth2, des méthodes d'authentification (les "flows"), de ce qu'il est possible de faire et ce
qu'il ne faut surtout pas faire.

Basé avant tout sur des cas d'utilisation courants et pas juste un récit d'un énième bouquin sur oauth
avant de voir comment faire, on va surtout voir ce qu'il ne faut pas faire.

Exemple et manipulations avec keycloak.

Référence CFP : https://github.com/ToulouseJug/call-for-paper/issues/42

Vidéo : {{< youtube RcTwgvJQr8s >}}
