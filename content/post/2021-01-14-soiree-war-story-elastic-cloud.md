---
title: Soirée War Story Elastic Cloud
date: 2021-01-14
host: jakartaee
sponsors: [ippon, monkeypatch]
partners: [jetbrains]
authors: [abos]
---

Encore une soirée en remote.

Un énorme merci à la fondation Eclipse de nous permettre d'utiliser leur compte
"Jakarta EE for JUGs" sur la plateforme [crowdcast.io](https://www.crowdcast.io/jakarta4jugs).

### War story : comment les pauses du GC ont pété la prod - par Sylvain Wallez ({{< twitter bluxte >}})

Nous avons eu un [incident récent sur Elastic Cloud](https://www.elastic.co/blog/elastic-cloud-january-18-2019-incident-report) dont une des causes est des pauses longues du garbage collector de ZooKeeper.

Le talk présentera les grands principes de ZooKeeper et comment il est utilisé sur Elastic Cloud. On verra comment du code apparemment juste sous-optimal dans la librairie Apache Curator a en fait contribué à une réaction en chaîne qui a mis par terre une partie des services, et comment nous y avons remédié pour que ce type d'incident ne se produise plus.

Référence Cfp : https://github.com/ToulouseJug/call-for-paper/issues/28

Vidéo : {{< youtube id="hY3AmG3HYqE?start=365" >}}
