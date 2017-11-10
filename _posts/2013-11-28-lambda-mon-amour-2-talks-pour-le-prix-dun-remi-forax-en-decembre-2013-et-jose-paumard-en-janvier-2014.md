---
layout: post
title: Lambda mon amour - 2 talks pour le prix d'un ! Rémi Forax en décembre 2013 et José Paumard en janvier 2014
date: 2013-11-28 21:21
author: baptiste
comments: true
---
Comme vous le savez sûrement, <a href="http://openjdk.java.net/projects/jdk8/">Java 8 arrive d'ici quelques semaines, normalement fin mars 2014</a>.

Comme le dit Mark Reinhold, le "<em>Chief Architect of the Java Platform"</em>, <a href="https://blogs.oracle.com/java/entry/the_javaone_2013_technical_keynote">les lambdas sont la plus grosse mise à jour du modèle de programmation depuis toujours -- plus encore que les generics</a>.

Nous avons donc trouvé important de planifier plusieurs sessions pour découvrir sereinement toutes ces nouveautés.
<ol>
	<li>Octobre 2013 : La première de la série a déjà eu lieu il y a quelques semaines, avec <a href="{{site.baseurl}}/2013/10/03/soiree-generics-et-lambda.html">Henri Tremblay qui nous a sensibilisé au cocktail spécial qu'allait être le mélange lambda/generics</a>.</li>
	<li>Mardi 10 décembre 2013 : Rémi Forax nous expliquera "pourquoi les lambdas dans Java 8 sont ce qu'elles sont et pourquoi Java ne sera plus jamais le même".</li>
	<li>Mercredi 15 janvier 2014 : José Paumard nous présentera le nouveau visage de l'API Collection</li>
</ol>
<h3 id="lambdaHistory">Lambdas, from the great closure war to Java 8, an unexpected journey, <em>par Rémi Forax</em></h3>
Rémi est professeur et travaille dans l'équipe qui implémente les lambdas dans le JDK. Il fait partie des deux Expert Groups de la <a href="http://jcp.org/en/jsr/detail?id=292">JSR 292, sur invokedynamic</a>, et de la <a href="http://jcp.org/en/jsr/detail?id=335">JSR 335 (sur les lambdas, donc)</a>.

Abstract :
<p style="padding-left: 30px;">Une bonne façon de comprendre les lambdas est de repartir
de l'historique puis d'expliquer le cheminement pas toujours en ligne droite
qui a été suivi pour arriver à la syntaxe et la sémantique actuelle.
Puis je montrerai quelques exemples d'utilisation des lambdas
pour illustrer la façon dont les lambdas impactent le design d'APIs.</p>
<p style="padding-left: 30px;">Pour l'instant j'ai pas prévu de montrer de code assembleur, mais qui sait ?</p>
<a href="http://www.jugevents.org/jugevents/event/show.html?id=52745">Inscrivez-vous rapidement sur JugEvents</a>, les places seront chères :-) !
<h3 id="Collection">Java 8 : lambdas, Streams et Collectors, le nouveau visage de l'API Collection, <em>par José Paumard</em></h3>
José est professeur, membre du Paris JUG et rompu aux plus grosses conférences. <a href="http://www.devoxx.be/dv13-jos-paumard.html?presId=3540">Son talk sur le sujet à Devoxx 2013</a>, il y a quelques semaines, a été parmi les mieux notés par l'assistance.

Abstract :
<p style="padding-left: 30px;">L'API la plus utilisée du JDK est sans aucun doute l'API Collection. Brillamment conçue il y a un peu plus de 15 ans, elle est encore aujourd'hui au coeur de toutes les applications Java. En 2004, elle a subi son premier lifting, avec l'introduction des génériques. Cette mise à jour, bien qu'importante, n'a cependant pas modifié ses patterns d'utilisation. Avec l'introduction des lambdas en Java 8, l'API Collection est à nouveau réécrite, mais cette fois la situation est différente : ses patterns d'utilisation sont complètement changés.</p>
<p style="padding-left: 30px;">La première partie de cette conférence introduit les lambda expressions, comment les écrire, et ce qu'elle nous apportent en tant que développeurs. La deuxième partir présente en détail les nouveaux patterns introduits par les API Stream et Collector. Ces nouvelles API vont changer la façon dont nous allons pouvoir traiter les collections de grande taille, y compris en parallèle, avec un modèle de programmation très simple, et des patterns très puissants. Cette puissance sera montrée dans des exemples réels, qui monteront comment Java 8 va pouvoir nous aider à écrire simplement du code efficace et performant.</p>
Les inscriptions ne sont pas encore ouvertes, mais surveillez bien le compte Twitter <a href="https://twitter.com/toulousejug">@toulousejug</a> ou <a href="https://groups.google.com/forum/#!forum/toulouse-jug">la liste du JUG</a>, nous allons l'ouvrir probablement d'ici mi-décembre.
