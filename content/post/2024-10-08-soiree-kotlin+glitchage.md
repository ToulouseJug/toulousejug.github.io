---
title: Soirée High-Performance Kotlin + Glitchage de microcontroleur
date: 2024-10-08
host: epitech
sponsors: [monkeypatch, lyra]
partners: [jetbrains]
authors: [abos]
flyer: images/2024-10-08-soiree-kotlin+glitchage/promo.png
event: https://www.meetup.com/toulouse-java-user-group/events/303600904
---

Nouvelle soirée chez Epitech avec un retex par Arnaud Giuliani sur la gestion des choix
techniques sous contrainte de perf et de volumétrie, en Kotlin. Suivi d'une épopée électronique
par Fabien Tregan.


### From Zero to Billions : Building a High-Performance Kotlin App in Two Months - par Arnaud Giuliani

Join us as we unravel the journey of building a Kotlin app capable of handling billions of events in just two months. Within weeks of our first client using the SDK, we found ourselves analyzing approximately 5 terabytes of data.

The challenge was immense: how to store this vast amount of data without skyrocketing cloud consumption? Which data to retain and which to discard? How to ensure the frontend performance remains unaffected while loading pages?

Thanks to the flexibility of the Google Cloud Platform, we were able to design an infrastructure that is as reliable as it is scalable. But the work didn't stop there. We had to simultaneously develop new features.

In this presentation, we'll share the technology choices we made that enabled us to deliver quickly. We'll delve into our use of Ktor, Exposed, and Koin for our Kotlin web application development.

Join us to learn how we navigated these (crazy) challenges and successfully delivered a high-performing, data-intensive application.

### Mon premier test de glitchage de microcontroleur - par Fabien Trégan

Un peu dans l'idee de la pesentation que j'avais donnee au JUG sur de l'escalade et exploitation de bug dans Pokemon [non enregistrée, mais disponible en replay sur la chaîne de nos amis du DevFest Touluse ! ; ndlr], cette presentation n'a rien a voir avec Java.

Elle parle de glitchage de microcontroleur (ne pas respecter ses conditions d'utilisation pour qu'il n'ait pas son comportement nominal et par la contourner des protections), et plus specifiquement de comment j'ai procede, de ce que j'ai appris, de ce qui m'a surpris, lors de ma premiere tentative, moi qui fait beaucoup de dev java et de coaching et tres peu de securite et de l'electronique.