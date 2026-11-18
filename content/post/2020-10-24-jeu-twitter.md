---
title: Jeu Twitter licences JetBrains
date: 2020-10-24
partners: [jetbrains]
authors: [abos]
---

Chose promise, chose due !

Comme nous l'avions annoncé via Twitter, nous avions pas moins de 6 licences
pour des produits JetBrains à offrir en raison de notre partenariat
(JetBrains User Group Support Program).

{{< tweet 1319590091724128256 >}}

Sans plus attendre, les gagnants sont :

* {{< x JBaptiste_31 >}}
* {{< x 19emtuck >}}
* {{< x Olivier_M_31 >}}
* {{< x ClergueCh34 >}}
* {{< x lidodo >}}
* {{< x jpbolatre >}}

Félicitations ! 🥳 Vos coupons vous ont déjà été envoyés via Direct Message sur Twitter.

### Et ce tirage au sort, il est honnête ?!

Alors voilà, ce n'est pas la première fois qu'on voulait mettre en place un petit
tirage au sort avec Julien [Zanon, co-organisateur du JUG, NDLR] mais comme il
n'y a que 24 heures par jour, et 7 jours par semaine, ça ne s'était pas produit
jusqu'ici.

Seulement, après les deux sujets de la dernière soirée (Randomness & Property-Based
Testing) et voyant notre petit stock de coupons qui commençait à s'accumuler, on
s'est dit qu'il était temps.

J'avais gardé dans un coin quelque part un lien vers une méthode de sélection
d'un gagnant de concours via un petit algo en ligne de commande, alors cette nuit
je me suis chauffé et je l'ai ré-implémenté pour obtenir nos 6 gagnants.

### Show me the code!

Premièrement : récupérer la liste des participants au concour.

Pour aller vite, je n'ai pas intégré cette partie là dans le script (flemme
de créer un identifiant d'App Twitter, authentification, oauth, toussa...) et j'ai
directement récupéré le contenu JSON de la réponse faite par le navigateur.

{{< centeredimage local="true" alt="Testcontainers" src="firefox.png" width="800" >}}

Le dernier Twittos à avoir "liké" le Tweet (le premier sur la capture d'écran)
l'a fait après l'heure limite, il n'est donc pas pris en compte pour le tirage
au sort.  
Le contenu est disponible [ici](/misc/2020-10-24-jeu-twitter/twitter.json).

Ensuite l'algorithme. Je n'ai pas réinventé la roue, j'ai simplement adapté
le script détaillé dans cet article : [How To Do a Fair Online Raffle?](http://www.guido-flohr.net/how-to-do-a-fair-online-raffle/)
Je l'ai simplement modifié pour pouvoir faire plusieurs tours en excluant le
vainqueur du tour précédent, afin de faire gagner plus d'une personne.

Ce que j'ai trouvé d'amusant avec cet article, c'est que sa "source d'entropie"
est le compte Twitter de Donald Trump 🤣  
C'est tellement un excité de Twitter que comme source de
valeurs aléatoires, c'est effectivement bien choisi.

Je me suis donc basé sur le premier Tweet du 45° président des États-Unis à partir
de la fin du jeu, c'est-à-dire [celui-ci](https://x.com/realDonaldTrump/status/1319761576996573186)
(qui n'a rien d'amusant malheureusement, j'aurais bien aimé un petit Covfefe).

Et pour le reste, j'ai utilisé Clojure, et plus particulièrement [Babashka](https://github.com/borkdude/babashka).  
Parce que, quand même, on est un JUG, on va pas faire du bash ! On reste sur la JVM scrogneugneu !
(enfin GraalVM là en fait, mais ça passe !)

```clojure
#!/usr/bin/env bb
(require '[clojure.java.shell :refer [sh]])
(require '[cheshire.core :as json])


(defn get-entries []
  (->
    (slurp "twitter.json")
    json/parse-string
    (get-in ["data" "favoriters_timeline" "timeline" "instructions"])
    first
    (get "entries")
    ; ici j'inverse la liste des participants parce que Twittere
    ; me la donne par ordre antichronologique de "like"
    reverse
    vec))

(defn get-random-number-script-str [s mod]
  (format
    "echo '%s' | openssl sha512 -whirlpool | sed -e 's/.*= //' | tr '[:lower:]' '[:upper:]' | perl -lne 'print \"ibase=16;n=$_;ibase=A;n%%%s\"' | bc | tr -d '\n'"
    s mod))

(defn get-random-number [tweet participants]
  (->>
    (get-random-number-script-str tweet participants)
    (sh "bash" "-c")
    :out
    Integer/parseInt))

(defn vec-remove
  "remove elem in coll"
  [nth coll]
  (vec (concat (subvec coll 0 nth) (subvec coll (inc nth)))))

(defn get-winners [entries participants tweet max-coupons]
  (loop [entries entries participants participants winners #{} coupons 0]
    (if (< coupons max-coupons)
      (let [winnerIdx (get-random-number tweet participants)
            entry (nth entries winnerIdx)
            winner (get-in entry ["content" "itemContent" "user" "legacy" "screen_name"])
            ]
          (recur (vec-remove winnerIdx entries) (dec participants) (conj winners winner) (inc coupons)))
      winners)))

(let [entries (get-entries)
      participants (count entries)
      tweet "THANK YOU to all of the Great American Patriots in The Villages, Florida! #MAGA"
      max-coupons 6
      ]
  (get-winners entries participants tweet max-coupons))
```

Le résultat est le suivant :

```bash
$ raffle.clj
#{"JBaptiste_31" "19emtuck" "Olivier_M_31" "ClergueCh34" "lidodo" "jpbolatre"}
```

Voilà ! En attendant les vidéos de la soirée, qui ne devraient pas tarder,
vous avez tout sous la main pour vérifier les résultats.  
J'espère ne pas avoir fait de bêtise 😇