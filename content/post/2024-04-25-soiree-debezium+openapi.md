---
title: Soirée Change Data Capture + OpenAPI
date: 2024-04-25
host: lyra
sponsors: [monkeypatch, lyra]
partners: [jetbrains]
authors: [abos]
---

Pour cette occasion nous serons accueillis par notre sponsor, Lyra, à Labège.

### Change Data Capture : comment garantir l'intégrité des données relationnelles ? - par Manfred Martin

Le Change Data capture (CDC) permet de capter tous les changements de données qui se produisent sur la base de données et de les traiter comme on le souhaite.

Cette solution technique (ex : Debezium) adresse de nombreux cas d'utilisation : alimentation d'un data-lake, migration vers une architecture event-driven...

Un cas d'usage commun est la captation des changements sur une base de données relationnelle (SQL) afin de les envoyer au fil de l'eau sur une solution de streaming (ex. Kafka).

La promesse est belle mais... si vos données relationnelles sont bien structurées (et c'est le cas, bien sûr), elles ne tiennent pas dans une unique table mais plutôt sur un ensemble de tables liées entre elles par des relations.

Alors la réalité vous rattrape et c'est le début des problèmes !

Car malgré les différents modes de fonctionnement des outils de CDC, mettre à disposition des données éclatées sur plusieurs tables tout en assurant leur intégrité à chaque instant reste un challenge !

Même si les données seront "cohérentes à terme", les données immédiates, elles, pourront être incohérents et décrire une réalité qui n'aura même jamais existée dans la base de données !

Pour y remédier, nous vous présenterons différentes solutions que nous avons expérimentées : celles qui marchent... et les autres !

Vidéo : {{< youtube id="Rrptq845zB0" >}}

### OpenAPI (dev tool) - par Damien Guerin

Les contrats OpenAPI (anciennement Swagger) permettent de formaliser le fonctionnement d'une API REST. Dans un environnement de plus en plus tourné vers les API et les micro-services, ce formalisme présente de nombreux avantages, comme la génération automatique du code client et serveur, la garantie de stabilité de l'écosystème, la validation à la volée des requêtes entrantes, la génération de documentation, etc.

Durant ce talk, nous vous présenterons la stratégie mise en place à Lyra pour centraliser et partager les contrats OpenAPI entre les différents produits, et simplifier les interdépendances entre services.

Pour cela, nous avons publié en Open-Source l' "OpenAPI Dev Tool", un outil tout-en-un permettant de simplifier le développement et l'utilisation des contrats de nos API. Utilisé par tous nos projets en interne, il peut être utilisé dans n'importe quel contexte.

Enfin, nous conclurons par un retour d'expérience sur l'utilisation de l'écosystème OpenAPI, ses avantages et les pièges que nos 5 ans d'expérimentations nous ont permis de déceler.

Vidéo : {{< youtube id="I-QuS0EBA08" >}}
