---
title: Soirée jOOQ & Change-Data-Capture
date: 2020-11-17
host: jakartaee
sponsors: [ippon, monkeypatch]
partners: [jetbrains]
authors: [abos]
---

Encore une soirée en remote.

Un énorme merci à la fondation Eclipse de nous permettre d'utiliser leur compte
"Jakarta EE for JUGs" sur la plateforme [crowdcast.io](https://www.crowdcast.io/jakarta4jugs).

### JOOQ, joy of SQL - par Kevin Davin ({{< twitter davinkevin >}})

Et si l'on reprenait le contrôle de nos interactions avec notre base de données préférée? Car en vrai, nos BDD sont des monstres de puissance qui sont souvent sous exploités sweat. Nous verrons, avec JOOQ, comment écrire des requêtes SQL simples ou évolués, le tout facilement et de manière type-safe !

Venez découvrir cette superbe librairie OpenSource, compatible Java, Kotlin & Scala, qui va vous permettre de vous simplifier la vie et d'améliorer votre code… et même de découvrir de super fonctionnalités SQL que vous n'imaginiez même pas.

Lien des slides : https://docs.google.com/presentation/d/1YKk47FWeQqEIUVRHBKHSx7cigFGfeMV5QBYqe-dnHjE

Référence CFP : https://github.com/ToulouseJug/call-for-paper/issues/49

Vidéo : {{< youtube id="iXup-CqXdvc?start=484" >}}

### A Change-Data-Capture use-case: designing an evergreen cache - par Nicolas Frankel ({{< twitter nicolas_frankel >}})

When one’s app is challenged with poor performances, it’s easy to set up a cache in front of one’s SQL database. It doesn’t fix the root cause (e.g. bad schema design, bad SQL query, etc.) but it gets the job done. If the app is the only component that writes to the underlying database, it’s a no-brainer to update the cache accordingly, so the cache is always up-to-date with the data in the database.

Things start to go sour when the app is not the only component writing to the DB. Among other sources of writes, there are batches, other apps (shared databases exist unfortunately), etc. One might think about a couple of ways to keep data in sync i.e. polling the DB every now and then, DB triggers, etc. Unfortunately, they all have issues that make them unreliable and/or fragile.

You might have read about Change-Data-Capture before. It’s been described by Martin Kleppmann as turning the database inside out: it means the DB can send change events (SELECT, DELETE and UPDATE) that one can register to. Just opposite to Event Sourcing that aggregates events to produce state, CDC is about getting events out of states. Once CDC is implemented, one can subscribe to its events and update the cache accordingly. However, CDC is quite in its early stage, and implementations are quite specific.

In this talk, I’ll describe an easy-to-setup architecture that leverages CDC to have an evergreen cache.

Vidéo : {{< youtube id="iXup-CqXdvc?start=4090" >}}
