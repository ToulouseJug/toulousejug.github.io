---
title: Soirée De l'OOP à la FP
date: 2019-06-11
sponsors: ippon, monkeypatch
authors: [abos]
---

Pour la dernière soirée de la saison 2018-2019 le thème était "de la programmation orientée object
à la programmation fonctionnelle", vaste programme.  
Pour ce faire, une première vidéo où l'on revient aux sources et où l'on présente les grands concepts, suivi
d'une présentation d'un cas concret pour lequel des concepts de programmation fonctionnelle peuvent nous aider.

### La programmation fonctionnelle sans céder à la mode - par Frédéric Cabestre ({{< twitter fcabestre >}})

Aujourd'hui, pour être à la mode, il faut parler de programmation fonctionnelle. Et de suite on convoque les mots en vogue: « Immutabilité », « Monade » ou « Catamorphisme ». Au mieux le message est brouillé, mal reçu. Au pire la salle se vide !

Ce que je vous propose c'est de repartir des principes de base, avec des idées bien arrêtées et peut-être parfois provocatrices. Comprendre, comme le disait John Hugues, « Why functionnal programming matters ». Cerner les quelques idées directrices de la programmation fonctionnelle et ce qu'elles apportent concrètement au quotidien. Voir comment et pourquoi d'autres concepts en découlent nécessairement...

Il sera peut-être finalement question de « Théorie des catégories » ! Mais il sera surtout question, en vrac, d'histoire et de mise en œuvre des langages, de typage, de performance, d'artisanat du logiciel, de « Design patterns », d'abstraction et, soyons fou, de réification.

En somme, je vais vous parler de programmation fonctionnelle en essayant de ne pas être à la mode !

Référence CfP : https://github.com/ToulouseJug/call-for-paper/issues/20

Vidéo : {{< youtube pBHCHF2JMfg >}}

### De l'OOP à la FP : l'affaire de la validation - par Emmanuel Nhan ({{< twitter nhanmanu >}})

On est tous tombé au moins une fois dans cette boucle en remplissant un formulaire web :

* Remplir et cliquer sur envoyer,
* Avoir en retour un champ en erreur,
* Corriger la saisie et soumettre,
* Avoir un autre champ en erreur,
* Corriger la saisie et soumettre,
* ...

Même chose pour l'envoi d'une requête HTTP avec un body JSON qui peut être invalide à plusieurs endroits. Doit-on corriger chaque champ un à un à mesure que l'on découvre les erreurs ou existe-t-il un moyen d'avoir l'ensemble des erreurs dès la première requête ?

Dans ce talk, nous examinerons les moyens pour remonter toutes les erreurs dès la première validation en commençant par la solution la plus Java possible en utilisant la JSR 303 Bean Validation. Après avoir vu les avantages et inconvénients de cette approche, nous essayerons de construire un programme plus fonctionnel. Petit à petit nous ferons émerger des abstractions et nous déboucherons sur une version purement fonctionnelle de la résolution de ce problème.

Ce talk est fait pour les développeurs Java ou Kotlin qui veulent rendre leur code plus fonctionnel. Par conséquent, il nécessite une connaissance de Java et des bases de Kotlin ou Scala. Si vous connaissez déjà Scala et Cats, ne vous attendez pas à apprendre beaucoup.

Référence CfP : https://github.com/ToulouseJug/call-for-paper/issues/27

Vidéo : {{< youtube tkq-TjcYM3Q >}}
