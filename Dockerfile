# Image simpliste pour builder et tester plus facilement en local.
# docker build -t toulousejug .
# docker run -p 4000:4000 toulousejug
FROM jekyll/jekyll:3

ADD . /srv/jekyll/
