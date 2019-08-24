# Yoga class list

I fell in love with http://dashdance.com website [long ago](https://twitter.com/tvrdek/status/819822694053150720) and now, thanks to Tailwind CSS I finally got to reimplement events listing and detail.

You can see it live on https://yoga-studio.netlify.com/

## How to build it

The app uses Tailwind to build it's CSS.

```
npx tailwind build site/static/styles.css -o site/static/output.css
```

To build the HTML I used jinja2 and livereload.

```
# Build the output
pipenv run python build.py

# Start dev server
pipenv run python main.py
```