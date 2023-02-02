---
title: Soirée GC concurrents
date: 2020-05-14
host: jakartaee
sponsors: [ippon, monkeypatch]
partners: [jetbrains]
authors: [abos]
---

Première soirée remote pour le Toulouse JUG !

Un énorme merci à la fondation Eclipse de nous permettre d'utiliser leur compte
"Jakarta EE for JUGs" sur la plateforme [crowdcast.io](https://www.crowdcast.io/jakarta4jugs).

Suite à l'épidémie de COVID-19 de nombreuses conférences ont été annulée. C'est le
cas de Devoxx France où Jean-Philippe Bempel devait, cette année, parler de Java
Flight Recorder après avoir donné, l'an dernier, une présentation sur les GC
concurrents.

Avec Julien on a pensé que cette présentation sur les GC concurrents, même si déjà
vue à d'autres conférences, était très intéressante et vallait la peine d'être
rejouée. Nous remercions chaleureusement Jean-Philippe d'avoir partagé ses
connaissances avec nous !

### Comprendre les GC sur la JVM : Mode Avancé ! - par Jean-Philippe Bempel ({{< twitter jpbempel >}})

Depuis quelques années, le monde du GC sur la JVM évolue : G1 est par défaut sur le JDK9, Shenandoah est mis à disposition par Red Hat, un nouveau GC entre dans l'OpenJDK depuis le JDK 11: ZGC et Azul C4 est toujours là.

Comme les GC "classiques" sont plutôt bien compris maintenant, cette présentation s'attardera sur les arcanes des plus récents. Nous allons expliquer le concurrent marking (tri-color marking), les specificités de G1, la Load Value Barrier de C4, les Brooks pointers de Shenandoah et le multi-mapping de ZGC.

== À propos du speaker

Développeur passionné par les performances, les runtim es (JVM, CLR) et adepte de Mechanical Sympathy, Jean-Philippe Bempel a plus de 8 ans d'expérience dans les systèmes de trading low latency. Maintenant il apporte son expertise sur la JVM chez Criteo afin d'optimiser les jobs Map/Reduce & Spark.

Vidéo : {{< youtube 52oD58ll9GY >}}
