# Glyphance

<kbd>/ɡlɪfhɑːns/</kdb>

This is a CLI utility that help reduce load times and bytes by splitting typography files into smaller chunks for different unicode ranges automatically _without the tears_.

## 🌈 Features

- Configurable.
- Config driven.
- Docker image, no local install required.
- Outputs `woff2`.
- Provides a generated CSS file to simply include.

## 🚀 Quickstart

Lets assume we want to use 2 variable fonts, one of which has an italic version still as a separate file. Also on our webserver we serve our static fonts from `/fonts/`.

1. Get the font files
2. Write a little config file `glyphance.yaml` and define the font-families (`Mulish` and `FireCode` e.g.) and their files or variations.
3. Run it.
4. Use the generate font files and CSS.

```
example/
├── FiraCode-VariableFont_wght.ttf
├── Mulish-Italic-VariableFont_wght.ttf
├── Mulish-VariableFont_wght.ttf
└── glyphance.yaml
```

```yaml
# glyphance.yaml
fonts:
  'Mulish':
    - file: Mulish-VariableFont_wght.ttf
      variable: true
      css:
        font-weight: 200 1000
    - file: Mulish-Italic-VariableFont_wght.ttf
      variable: true
      css:
        font-weight: 200 1000
        font-style: italic
  'FireCode':
    - file: FiraCode-VariableFont_wght.ttf
      variable: true
      css:
        font-weight: 300 700

output:
  prefix: /fonts/
```

### Run

```bash
docker run -v $(pwd)/example:/data cupcakearmy/glyphance
```

### Enjoy

Now you can use the generated font files and import the `generated/fonts.css` into your code.

> Remember you can modify the `prefix` to match the folder structure of your static files.

```
example/
├── FiraCode-VariableFont_wght.ttf
├── Mulish-Italic-VariableFont_wght.ttf
├── Mulish-VariableFont_wght.ttf
├── generated
│   ├── 08284d4f696ab68dc7aa21c9c061c534939a3a0c.woff2
│   ├── ...
│   ├── ...
│   ├── f8d95e7f048e130c09015a20689693461cc0dedb.woff2
│   └── fonts.css
└── glyphance.yaml
```

## 💡 Inspiration

The idea came mostly at how google fonts subsets their typefaces on [Google Fonts](https://fonts.google.com).
They split the fonts into multiple blocks of unicode chars, and leverage the [`unicode-range`](https://developer.mozilla.org/en-US/docs/Web/CSS/@font-face/unicode-range) property of `@font-face` to only deliver the parts of a font that are needed for a website, drastically reducing bytes sent over the wire.
Under the hood it uses the amazing [fonttools](https://github.com/fonttools/fonttools) to do the heavy lifting.

## 📖 API & Documentation

> Config file reference can be found under [docs/config](./docs/config/).

### Example

```yaml
fonts:
  'My Font Familiy':
    - file: ./path/relative/to/config/file.ttf|otf|...
      variable: true # Whether ist's a variable font or not, defaults to false
      css:
        font-style: italic # Custom css properties to be added to the css

output:
  dir: foo # Directory of the output
  prefix: /static/fonts # Prefix to be added to the src URL in the CSS
  clean: true # Whether to clean to output directory first
  css:
    font-weight: 400 # CSS to added to each @font-face. By defaults includes swap, normal weight and style
```

### Provide custom unicode ranges

By default Glyphance uses the same ranges as Google Fonts. However you can customize and specify your own ranges. See the [list of possible values](https://en.wikipedia.org/wiki/List_of_Unicode_characters).

```yaml
fonts:
  'Mulish':
    - file: Mulish-VariableFont_wght.ttf
      variable: true
      css:
        font-weight: 200 1000
    - file: Mulish-Italic-VariableFont_wght.ttf
      variable: true
      css:
        font-weight: 200 1000
        font-style: italic
  'FireCode':
    - file: FiraCode-VariableFont_wght.ttf
      variable: true
      css:
        font-weight: 300 700

output:
  ranges:
    abc: U+0061-0063
    numbers: U+0030-0039
    dot: U+002E
  ""
```
