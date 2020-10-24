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