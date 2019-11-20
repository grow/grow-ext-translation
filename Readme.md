# Grow Translation Extension

Note: **Experimental**

Extension for working with translations inline in the document using custom
jinja functions in the templates.

## Usage

### Initial setup

1. Create an `extensions.txt` file within your pod.
1. Add to the file: `git+git://github.com/grow/grow-ext-translation`
1. Run `grow install`.
1. Add the following section to `podspec.yaml`:

```
ext:
- extensions.translation.TranslationExtension
```

When the extension is enabled (on by default) the translation UI JS and CSS will be added to the build output.

### Environment specific configuration.

The extension can be disabled by using environment tagging:

For example:

```
ext:
- extensions.translation.TranslationExtension
    enabled@env.prod: False

deployments:
  prod:
    destination: local
    out_dir: build/
    env:
      name: prod
```

## Templating

In order to use the translation extension the following are needed in the templates.

In the `<head>` add the following:

```
{{translation_styles()}}
```

At the end of the `<body>` add the following:

```
{{translation_scripts()}}
```

When outputting translations in the templates instead of using `_()`
use the following depending on the context.

For normal text blocks use the following:

```
<p>{{ _tag('Original String') }}</p>
```

When using in attributes (ex: `title=""`) use the following:

```
<img {{ _attr('alt', 'original string') }}>
```
