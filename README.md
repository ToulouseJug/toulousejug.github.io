Built with [Hugo].

---

## Preview locally

Build the site and serve it locally with:

    docker run -it --rm --volume=$(pwd):/src -p 1313:1313 registry.gitlab.com/pages/hugo@sha256:017b3e0d3620cf4a7d782656237b7aa8793909339d927c15dcd5bdd26180a849 hugo serve --bind 0.0.0.0

Then go to `localhost:1313/`.

Once happy with your changes, commit to the `source` branch.

## Deploying

Run:

    docker run -it --rm --volume=$(pwd):/srv registry.gitlab.com/pages/hugo@sha256:017b3e0d3620cf4a7d782656237b7aa8793909339d927c15dcd5bdd26180a849 hugo -d public/

Then go to the `public` folder, commit onto the `master` branch and push to Github to deploy. 

[hugo]: https://gohugo.io
