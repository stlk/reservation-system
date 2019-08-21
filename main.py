#!/usr/bin/env python
from livereload import Server, shell
server = Server()

build = shell('pipenv run python build.py', cwd='.')
build()
build_css = shell('npx tailwind build site/static/styles.css -o site/static/output.css', cwd='.')
build_css()

server.watch('site/**/*', build)
server.watch('site/*', build)
server.watch('build.py', build)
server.watch('site/static/styles.css', build_css)
server.watch('tailwind.config.js', build_css)
server.serve(root='public')