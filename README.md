toulousejug.github.io
=====================

Toulouse JUG website


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
        jekyll serve 
        
        #et voila : http://localhost:4000/
        # classic Git pour modificer le site
