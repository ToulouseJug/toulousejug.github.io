---
title: Soirée GraalVM
date: 2019-12-12
host: onepoint
sponsors: [ippon, monkeypatch]
partners: [jetbrains]
authors: [abos]
---

Il faudrait vivre dans une grotte pour ne pas avoir entendu parler de GraalVM.  
Si c'est votre cas, il va falloir songer à venir plus souvent au JUG !

Pour la dernière soirée de l'année 2019 nous vous avions proposé deux présentations sur ce thème.

### GraalVM : les applications natives en Java - par Sylvain Wallez ({{< x bluxte >}})

GraalVM est une JVM nouvelle génération qui a plusieurs aspects intéressants :

* elle est "polyglotte" et permet de faire tourner du Java/Kotlin/Scala (classique) mais aussi du R, JavaScript, Ruby ou Python (moins classique)
* elle permet de faire de la compilation "ahead of time" et produire un exécutable natif minimaliste qui peut être déployé facilement.

La présentation montrera les différentes capacités de GraalVM et comment la compilation native permet de répondre aux contraintes des applications "cloud-native", catégorie qui regroupe les micro-services, le serverless, les containers (et side-cars), etc.

Référence CfP : https://github.com/ToulouseJug/call-for-paper/issues/22

Vidéo : {{< youtube qyx21kTon9Q >}}

### GraalVM: la JVM polyglotte - par Pascal Gillet ({{< x psclgllt >}})

“Cette librairie n'est pas disponible dans mon langage de programmation. Je dois la réécrire."

"Ce langage conviendrait parfaitement à mon problème, mais nous ne pouvons pas l'exécuter dans notre environnement."

"Ce problème est déjà résolu dans tel ou tel langage, mais ce langage est trop lent."

Oui, GraalVM améliore les performances des langages JVM tels que Groovy, Scala ou Kotlin pour égaler les performances des langages natifs. Oui, GraalVM permet de produire des exécutables Java standalone - des images natives - grâce à la compilation Ahead-of-time. Oui, le startup de ces applications est grandement réduit. Oui, GraalVM est bien intégrée dans des frameworks tels que Micronaut et Quarkus. Et donc oui, GraalVM rend ses lettres de noblesse au langage Java, qui devient très pertinent dans le monde des micro-services. 😛

Dans ce talk, nous nous intéresserons à l'autre grand objectif de GraalVM, qui est de mélanger librement plusieurs langages dans des applications multi-langages ou polyglottes: imaginez une application dont le code source mêle le Java, le JavaScript, le Python, et le Rust! 🤯 GraalVM permet donc aux développeurs de choisir librement le bon langage pour la tâche à résoudre, sans faire de compromis sur les performances.

Nous allons étudier les mécanismes de GraalVM permettant des applications polyglottes. Nous présenterons également Truffle, un outil associé à GraalVM pour écrire son propre langage.

Et bien sûr nous écrirons, en live, une application multi-langages !

Référence CfP : https://github.com/ToulouseJug/call-for-paper/issues/22

Vidéo : {{< youtube PypmeSh1WlQ >}}
