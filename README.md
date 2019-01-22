Built with [Hugo].

---

## Preview locally

Build the site and serve it locally with:

    docker run -it --rm --volume=$(pwd):/srv -p 1313:1313 registry.gitlab.com/pages/hugo:latest hugo -s srv serve --bind 0.0.0.0

Then go to `localhost:1313/`.

Once happy with your changes, commit to the `source` branch.

## Deploying

Run:

    docker run -it --rm --volume=$(pwd):/srv registry.gitlab.com/pages/hugo:latest hugo -s srv -d public/

Then go to the `public` folder, commit onto the `master` branch and push to Github to deploy. 

[hugo]: https://gohugo.io
