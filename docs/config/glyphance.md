# Config Schema

```txt
https://github.com/cupcakearmy/glyphance
```



| Abstract            | Extensible | Status         | Identifiable | Custom Properties | Additional Properties | Access Restrictions | Defined In                                                                      |
| :------------------ | :--------- | :------------- | :----------- | :---------------- | :-------------------- | :------------------ | :------------------------------------------------------------------------------ |
| Can be instantiated | No         | Unknown status | No           | Forbidden         | Forbidden             | none                | [glyphance.schema.json](../../out/glyphance.schema.json "open original schema") |

## Config Type

`object` ([Config](glyphance.md))

# Config Properties

| Property            | Type     | Required | Nullable       | Defined by                                                                                               |
| :------------------ | :------- | :------- | :------------- | :------------------------------------------------------------------------------------------------------- |
| [fonts](#fonts)     | `object` | Optional | cannot be null | [Config](glyphance-defs-fonts.md "https://github.com/cupcakearmy/glyphance#/properties/fonts")           |
| [output](#output)   | `object` | Optional | cannot be null | [Config](glyphance-defs-output.md "https://github.com/cupcakearmy/glyphance#/properties/output")         |
| [context](#context) | `string` | Optional | cannot be null | [Config](glyphance-properties-context.md "https://github.com/cupcakearmy/glyphance#/properties/context") |

## fonts



`fonts`

* is optional

* Type: `object` ([Details](glyphance-defs-fonts.md))

* cannot be null

* defined in: [Config](glyphance-defs-fonts.md "https://github.com/cupcakearmy/glyphance#/properties/fonts")

### fonts Type

`object` ([Details](glyphance-defs-fonts.md))

## output



`output`

* is optional

* Type: `object` ([Details](glyphance-defs-output.md))

* cannot be null

* defined in: [Config](glyphance-defs-output.md "https://github.com/cupcakearmy/glyphance#/properties/output")

### output Type

`object` ([Details](glyphance-defs-output.md))

## context



`context`

* is optional

* Type: `string`

* cannot be null

* defined in: [Config](glyphance-properties-context.md "https://github.com/cupcakearmy/glyphance#/properties/context")

### context Type

`string`

# Config Definitions

## Definitions group fonts

Reference this group by using

```json
{"$ref":"https://github.com/cupcakearmy/glyphance#/$defs/fonts"}
```

| Property          | Type    | Required | Nullable       | Defined by                                                                                                                   |
| :---------------- | :------ | :------- | :------------- | :--------------------------------------------------------------------------------------------------------------------------- |
| `^[a-zA-z \-_]+$` | `array` | Optional | cannot be null | [Config](glyphance-defs-font.md "https://github.com/cupcakearmy/glyphance#/$defs/fonts/patternProperties/^\[a-zA-z \\-_]+$") |

### Pattern: `^[a-zA-z \-_]+$`



`^[a-zA-z \-_]+$`

* is optional

* Type: `object[]` ([Details](glyphance-defs-font-variation.md))

* cannot be null

* defined in: [Config](glyphance-defs-font.md "https://github.com/cupcakearmy/glyphance#/$defs/fonts/patternProperties/^\[a-zA-z \\-_]+$")

#### ^\[a-zA-z \\-\_]+$ Type

`object[]` ([Details](glyphance-defs-font-variation.md))

## Definitions group font

Reference this group by using

```json
{"$ref":"https://github.com/cupcakearmy/glyphance#/$defs/font"}
```

| Property | Type | Required | Nullable | Defined by |
| :------- | :--- | :------- | :------- | :--------- |

## Definitions group css

Reference this group by using

```json
{"$ref":"https://github.com/cupcakearmy/glyphance#/$defs/css"}
```

| Property                                                                                                                                                                                                    | Type     | Required | Nullable       | Defined by                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| :---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | :------- | :------- | :------------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `^ascent-override\|descent-override\|font-display\|font-family\|font-stretch\|font-style\|font-weight\|font-feature-settings\|font-variation-settings\|line-gap-override\|size-adjust\|src\|unicode-range$` | `string` | Optional | cannot be null | [Config](glyphance-defs-css-patternproperties-ascent-overridedescent-overridefont-displayfont-familyfont-stretchfont-stylefont-weightfont-feature-settingsfont-variation-settingsline-gap-overridesize-adjustsrcunicode-range.md "https://github.com/cupcakearmy/glyphance#/$defs/css/patternProperties/^ascent-override\|descent-override\|font-display\|font-family\|font-stretch\|font-style\|font-weight\|font-feature-settings\|font-variation-settings\|line-gap-override\|size-adjust\|src\|unicode-range$") |

### Pattern: `^ascent-override|descent-override|font-display|font-family|font-stretch|font-style|font-weight|font-feature-settings|font-variation-settings|line-gap-override|size-adjust|src|unicode-range$`



`^ascent-override|descent-override|font-display|font-family|font-stretch|font-style|font-weight|font-feature-settings|font-variation-settings|line-gap-override|size-adjust|src|unicode-range$`

* is optional

* Type: `string`

* cannot be null

* defined in: [Config](glyphance-defs-css-patternproperties-ascent-overridedescent-overridefont-displayfont-familyfont-stretchfont-stylefont-weightfont-feature-settingsfont-variation-settingsline-gap-overridesize-adjustsrcunicode-range.md "https://github.com/cupcakearmy/glyphance#/$defs/css/patternProperties/^ascent-override|descent-override|font-display|font-family|font-stretch|font-style|font-weight|font-feature-settings|font-variation-settings|line-gap-override|size-adjust|src|unicode-range$")

#### ^ascent-override|descent-override|font-display|font-family|font-stretch|font-style|font-weight|font-feature-settings|font-variation-settings|line-gap-override|size-adjust|src|unicode-range$ Type

`string`

## Definitions group font-variation

Reference this group by using

```json
{"$ref":"https://github.com/cupcakearmy/glyphance#/$defs/font-variation"}
```

| Property              | Type      | Required | Nullable       | Defined by                                                                                                                                          |
| :-------------------- | :-------- | :------- | :------------- | :-------------------------------------------------------------------------------------------------------------------------------------------------- |
| [file](#file)         | `string`  | Optional | cannot be null | [Config](glyphance-defs-font-variation-properties-file.md "https://github.com/cupcakearmy/glyphance#/$defs/font-variation/properties/file")         |
| [variable](#variable) | `boolean` | Optional | cannot be null | [Config](glyphance-defs-font-variation-properties-variable.md "https://github.com/cupcakearmy/glyphance#/$defs/font-variation/properties/variable") |
| [css](#css)           | `object`  | Optional | cannot be null | [Config](glyphance-defs-css.md "https://github.com/cupcakearmy/glyphance#/$defs/font-variation/properties/css")                                     |

### file



`file`

* is optional

* Type: `string`

* cannot be null

* defined in: [Config](glyphance-defs-font-variation-properties-file.md "https://github.com/cupcakearmy/glyphance#/$defs/font-variation/properties/file")

#### file Type

`string`

### variable



`variable`

* is optional

* Type: `boolean`

* cannot be null

* defined in: [Config](glyphance-defs-font-variation-properties-variable.md "https://github.com/cupcakearmy/glyphance#/$defs/font-variation/properties/variable")

#### variable Type

`boolean`

### css



`css`

* is optional

* Type: `object` ([Details](glyphance-defs-css.md))

* cannot be null

* defined in: [Config](glyphance-defs-css.md "https://github.com/cupcakearmy/glyphance#/$defs/font-variation/properties/css")

#### css Type

`object` ([Details](glyphance-defs-css.md))

## Definitions group range

Reference this group by using

```json
{"$ref":"https://github.com/cupcakearmy/glyphance#/$defs/range"}
```

| Property | Type | Required | Nullable | Defined by |
| :------- | :--- | :------- | :------- | :--------- |

## Definitions group output

Reference this group by using

```json
{"$ref":"https://github.com/cupcakearmy/glyphance#/$defs/output"}
```

| Property            | Type      | Required | Nullable       | Defined by                                                                                                                        |
| :------------------ | :-------- | :------- | :------------- | :-------------------------------------------------------------------------------------------------------------------------------- |
| [dir](#dir)         | `string`  | Optional | cannot be null | [Config](glyphance-defs-output-properties-dir.md "https://github.com/cupcakearmy/glyphance#/$defs/output/properties/dir")         |
| [prefix](#prefix)   | `string`  | Optional | cannot be null | [Config](glyphance-defs-output-properties-prefix.md "https://github.com/cupcakearmy/glyphance#/$defs/output/properties/prefix")   |
| [css](#css-1)       | `object`  | Optional | cannot be null | [Config](glyphance-defs-css.md "https://github.com/cupcakearmy/glyphance#/$defs/output/properties/css")                           |
| [clean](#clean)     | `boolean` | Optional | cannot be null | [Config](glyphance-defs-output-properties-clean.md "https://github.com/cupcakearmy/glyphance#/$defs/output/properties/clean")     |
| [formats](#formats) | `array`   | Optional | cannot be null | [Config](glyphance-defs-output-properties-formats.md "https://github.com/cupcakearmy/glyphance#/$defs/output/properties/formats") |
| [ranges](#ranges)   | `object`  | Optional | cannot be null | [Config](glyphance-defs-output-properties-ranges.md "https://github.com/cupcakearmy/glyphance#/$defs/output/properties/ranges")   |

### dir



`dir`

* is optional

* Type: `string`

* cannot be null

* defined in: [Config](glyphance-defs-output-properties-dir.md "https://github.com/cupcakearmy/glyphance#/$defs/output/properties/dir")

#### dir Type

`string`

### prefix



`prefix`

* is optional

* Type: `string`

* cannot be null

* defined in: [Config](glyphance-defs-output-properties-prefix.md "https://github.com/cupcakearmy/glyphance#/$defs/output/properties/prefix")

#### prefix Type

`string`

### css



`css`

* is optional

* Type: `object` ([Details](glyphance-defs-css.md))

* cannot be null

* defined in: [Config](glyphance-defs-css.md "https://github.com/cupcakearmy/glyphance#/$defs/output/properties/css")

#### css Type

`object` ([Details](glyphance-defs-css.md))

### clean



`clean`

* is optional

* Type: `boolean`

* cannot be null

* defined in: [Config](glyphance-defs-output-properties-clean.md "https://github.com/cupcakearmy/glyphance#/$defs/output/properties/clean")

#### clean Type

`boolean`

### formats



`formats`

* is optional

* Type: `string[]`

* cannot be null

* defined in: [Config](glyphance-defs-output-properties-formats.md "https://github.com/cupcakearmy/glyphance#/$defs/output/properties/formats")

#### formats Type

`string[]`

### ranges



`ranges`

* is optional

* Type: `object` ([Details](glyphance-defs-output-properties-ranges.md))

* cannot be null

* defined in: [Config](glyphance-defs-output-properties-ranges.md "https://github.com/cupcakearmy/glyphance#/$defs/output/properties/ranges")

#### ranges Type

`object` ([Details](glyphance-defs-output-properties-ranges.md))
