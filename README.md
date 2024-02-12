# Introduction to Python With Trinket

This repo is a mirror of the Trinket Course[Introduction to Python Programming]
(https://trinket.io/eric-busboom/courses/introduction-to-python-programming), 
which is a copy of a course provided by Trinket. We've modified the course
to include some recipes. The original source of the course is available
[at Trinket.io](https://trinket.io/eric-busboom/courses/introduction-to-python-programming)
or in the ``orig-source`` directory


The original source has been converted, using the ``convert.py`` script, 
to the [lesson-builder](https://github.com/league-infrastructure/lesson-builder.git) format. The
conversion can be views with the vuepress configuration in the `docs` doreictory, or
to the Github Pages deployment at:

    


## Setup for Development



Install the lesson-builder programs

```bash 
python -mvenv .venv
source .venv/bin/activate
pip install git+https://github.com/league-infrastructure/lesson-builder.git#egg=lesson-builder
```

Install vuepress, [see these instructions for details](https://vuepress.vuejs.org/guide/getting-started.html). In this example, we will be using `yarn` rather than `npm` to install vuepress.

Install the requirements the vuepress

```bash
( cd docs && yarn install) )
```

Run the vuepress devel server:

```bash
jtl serve 
```


After you make changes to the lessons, you should re-run the build: 

```bash
jtl -vv build --lesson assignments/lesson-plan.yaml -a assignments -d docs
```


If you want to have the build and serve watch the assignments directory for changes and automatically
rebuild: 

```bash
jtl serve & ;  jtl -vv build --lesson assignments/lesson-plan.yaml -a assignments -d docs -w
```
