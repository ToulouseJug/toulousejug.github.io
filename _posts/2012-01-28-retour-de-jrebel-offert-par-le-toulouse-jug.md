---
layout: post
title: Jonathan Pineau - Retour de JRebel, offert par le Toulouse JUG 
date: 2012-01-28 18:05
author: nicorama
comments: true
---
<p>Ce retour fait suite au gain d’une licence JRebel lors de la <a href="{{site.baseurl}}/2011/11/22/retour-sur-la-soiree-play.html">soirée du Toulouse JUG autour du Framework Play</a>.</p>
<h3>Présentation rapide</h3>
<p><a href="http://zeroturnaround.com/jrebel/">JRebel </a>est un outil proposé par la société ZeroTurnaround à destination des développeurs ayant pour but d’améliorer leur productivité. Pour cela, il fournit un système de prises en compte à chaud des modifications sans nécessiter le redéploiement de l’application ou le redémarrage du serveur.</p>
<p>Il se présente sous la forme d’un plugin « java agent » à déclarer au niveau de la JVM du serveur d’application et d’un fichier de configuration « rebel.xml » à placer à la racine du répertoire contenant les fichiers « .class » pour chaque application et module du projet. A l’exécution, cet agent surveille les classpath indiqués dans le fichier « rebel.xml » puis agit sur le Class Loader en chargeant les nouvelles versions des classes (d’après ce que j’ai pu comprendre, il s’agit d’un monitoring des classpath en se basant sur les timestamp des fichiers .class pour détecter les modifications).</p>
<p>Pour plus de détails, la <a href="http://zeroturnaround.com/jrebel/documentation/">documentation </a>et les forums permettent une prise en main rapide pour les cas d’utilisation standards.</p>
<h3>Prise en Main</h3>
<p>Pour prendre en main l’outil, j’ai effectué les premiers tests sur un projet personnel basé sur Spring MVC avec utilisation de Spring Web Flow, le tout s’exécutant dans le conteneur Tomcat.</p>
<p>Pour les technologies Spring, ZeroTurnaround fournit de nombreux exemples (documentation, FAQ, screencast). La mise en place de JRebel a donc été rapide. Pour les quelques problèmes survenus au démarrage, une recherche sur les forums permet de rapidement cerner les erreurs de paramétrage.</p>
<p>Pour les personnes ayant assisté aux soirées sur Play ou Grails, les présentateurs ont mis en avant la prise en compte des modifications sans redémarrage du serveur parmi les avantages par rapport aux autres frameworks JEE dits « standards ». Avec JRebel, un projet Spring « classique » profite d‘un fonctionnement très proche.</p>
<p>L’apport de JRebel est un plus indéniable pour le développement. Il permet d’améliorer la productivité du développeur aussi bien dans la phase de création que leur de la validation ou du support d’une application. Malgré quelques ratés ayant nécessité de redémarrer Tomcat, ce premier test m’a convaincu de pousser l’expérimentation en condition réelle sur un projet professionnel.</p>
<h3>Utilisation en condition réelle</h3>
<p>Afin de faire un retour plus pertinent, j’ai configuré JRebel sur mon environnement de développement professionnel. Point important, la société pour laquelle je travaille utilise un framework interne, donc non listé comme pris en charge par JRebel.</p>
<p>Alors que la mise en place fut plutôt rapide pour le projet Spring, la tâche a été beaucoup plus compliquée sur ce second environnement. Après plusieurs échecs, j’ai fini par trouver un paramétrage assurant la prise en compte des modifications pour les projets web principaux, les modules externes étant plus ou moins bien pris en charge.</p>
<p>Après environ trois semaines d’utilisation en condition réelle, JRebel affiche une estimation de 3 heures économisées (pour 14 jours de développement). Toutefois, malgré la prise en compte des modifications, notre framework interne nécessite un redéploiement de l’application web dans la plupart des cas.</p>
<p>La problématique rencontrée n’est pas à mettre sur le compte de JRebel mais sur le fonctionnement particulier de notre framework. Pour que certaines modifications soient prises en compte, la chaîne de démarrage de l’application web est impérative. Pour utiliser JRebel de manière optimale avec ce framework, le développement d’un plugin JRebel prenant en compte ses particularités semble inévitable et met fin à mes tests.</p>
<h3>Conclusion</h3>
<p>Les Plus :</p>
<ul>
<li>JRebel améliore la productivité de développement. Il peut être également intéressant lors de la phase de support où le nombre de redémarrages peut être élevé</li>
<li>Bonne intégration aux différents IDE et gestion de la majorité des conteneurs de servlet et serveurs JEE</li>
<li>Gestion d’un<a href="http://zeroturnaround.com/jrebel/features/frameworks/"> grand nombre de frameworks</a></li>
<li>Documentation et support</li>
</ul>
<p>Les Moins :</p>
<ul>
<li>Solution payante. Il peut être difficile de justifier l’achat sachant que la solution se limite aux développeurs et ne profite pas aux clients finaux en environnement de production</li>
<li>Solution complexe à mettre en œuvre avec certaines architectures (problème sur la gestion des modifications sur plusieurs modules externes) ou des frameworks « exotiques »</li>
</ul>
<p>Jonathan Pineau</p>

