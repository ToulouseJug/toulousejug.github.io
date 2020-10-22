---
title: Workshop Testcontainers
date: 2020-03-12
host: epitech
sponsors: [ippon, monkeypatch]
partners: [jetbrains]
authors: [abos]
---

En raison de l'épidémie de COVID (EDIT Post COVID: et juste avant d'être confinés !!!)
nous avions prévu une baisse du nombre d'inscrits à cette soirée. C'est pourquoi nous
avons choisi de vous proposer un workshop !

Les auteurs du Workshop n'étant pas dispo pour des raisons de planning, ils nous ont
proposé d'organiser le Workshop sans eux de notre côté, les sources étant disponible
en ligne (licence MIT) !

Plutôt que chacun sur son PC, et parce que l'ambiance s'y prêtait bien, nous avons réalisé
ce workshop en "mob programming". C'est-à-dire moi-même au "pupitre" avec mon laptop,
lisant les instructions du workshop, les tips et les correctifs, et les autres participants
qui me donnent leurs réponses/idées pour réaliser les exercices.

Voici la description du workshop et un lien vers le contenu à la fin 😉

{{< centeredimage local="true" alt="Testcontainers" src="testcontainers.jpeg" width="650" >}}

### Testcontainers - par Victor GALLET ({{< twitter GalletVictor >}}) et Antoine ROUX ({{< twitter _wziko_ >}})

Avec de plus en plus d'applications "dockerisées", Testcontainers est une librairie qui mérite que l'on s'y intéresse et va révolutionner la manière dont sont écrits les tests d'intégration.

En partant d'une application SpringBoot classique, en l'occurrence Spring PetClinic, nous vous proposons d'utiliser la puissance de Docker au sein de votre pipeline de tests d'intégration grâce à la librairie Testcontainers. Cette dernière est une bibliothèque Java permettant de simplifier la gestion du cycle de vie des conteneurs durant la phase de test.

Les applications que nous produisons sont de plus en plus connectées et de plus en plus dépendantes de ressources externes telles qu'une base de données, un broker de messages, un service de messagerie, etc. Afin de réaliser des tests qui communiquent avec ces ressources externes, nous avons habituellement recours à des librairies de mock, des services embarqués en mémoire, ou des installations en local.

Mettre en place des tests s'intégrant avec toutes ces briques est fastidieux et coûteux en terme de mise en place et de développement. De plus, ces derniers ne sont pas toujours représentatifs de la production.

Aujourd'hui, grâce à Docker et Testcontainers nous pouvons rapidement préparer un environnement de test fiable.

Workshop : https://zenika.github.io/handson-testcontainers/

Enjoy !