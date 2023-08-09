# Glossaire anglais-français D&D

## Introduction

Ce glossaire est une tentative de concentrer des traductions glanées ici et là. Il se peut qu'il serve un jour à quelque chose (notamment dans l'initiative de passer D&D en données structurées comme [Open5e](https://github.com/open5e), le jour où le multilingue sera possible.

## JSON data

La structure des données est la suivante :

```
{
    "glossary-a" :
    [
        {
            "en" : "animal telepathy",
            "fr" : "télépathie avec les animaux",
            "descr-fr" : "pouvoir psionique",
            "source" : "Eldritch Wizardry",
            "dd-version" : 0
        },
    ]
}
```

Cela pour chaque lettre.

Un programme python simple de conversion convertit tout cela en .md.

