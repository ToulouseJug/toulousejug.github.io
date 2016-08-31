toulousejug.github.io
=====================

Toulouse JUG website

Intallation sous Ubuntu/Debian (sans Docker)
---

Installer Ruby (avec des extensions dev)

        sudo apt-get install ruby-dev
        
Puis suivre le guide MacOS

Installation sous MacOS
---

MacOS inclut une version de Ruby et de son gestionnaire de package *gem*. L'installation necessite la Commande Line de XCode, ce qui n'est pas un cas isolé.
L'idéal est donc de suivre gentiment les [conseils d'installation](http://jekyllrb.com/docs/installation/) en commancant par le CLI Xcode, verifier avec `gem -v` que gem est installé puis :

        # ne pas oublier le sudo...
        sudo gem install jekyll

        # cloner le site
        cd ~/mes-super-projets
        git clone https://github.com/ToulouseJug/toulousejug.github.io.git

        # se déplacer sur le site
        cd toulousejug.github.io/
        # create a server, and regenerate _site for each modifications
        jekyll serve --watch

        #et voila : http://localhost:4000/
        # classic Git pour modificer le site

Utilisation avec Docker
-----

        docker run -it --rm --volume=$(pwd):/srv/jekyll -p 4000:4000 jekyll/jekyll jekyll s

Voir [utilisation de l'image Docker](https://github.com/jekyll/docker).

Fonctionnement basic
-----

Jekyll génère un répertoire nommé `_source` à partir des autres fichiers. Il ne faut donc pas chercher à modifier directement ce répertoire.

_config.yml
----

C'est le fichier de configuration principal


                name: Toulouse JUG
                description: Toulousains et passionnés des technos de la plateforme Java
                # dialect markdown
                markdown: redcarpet
                # seems deprecated
                pygments: true
                safe: true
                lsi: false
                paginate: 5
                encoding: UTF-8

                # needed for DNS redirection
                baseurl: /
                url: http://toulousejug.github.io
                linkGoogleGroup: http://groups.google.com/group/toulouse-jug
                linkTwitter: https://twitter.com/toulousejug
                linkGithub: https://github.com/toulousejug
                linkRSSFeeds: /feed
