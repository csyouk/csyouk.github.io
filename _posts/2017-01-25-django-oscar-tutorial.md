---
title: django-oscar
layout: post
date: '2017-01-25 03:00:51'
tags:
- django
- oscar
---

# Deep dive into django-oscar

## What is Django-Oscar?

- e-commerce framework
- open source
- django 1.8, python2 and 3 support
- FE : Bootstrap 3, less, jQuery

Before I start into django-oscar, I had to know the structure of django-oscar.

If stucked, give question to [here](https://groups.google.com/forum/?fromgroups#!forum/django-oscar).

*Oscar is a just a set of DJago apps*  
*Oscar is an e-commerce framework for Django desgined for building domain-driven sites*

~~~
oscar/
  apps/
  core/
  forms/
  locale/
  management/
  models/
  profiling/
  static/
  templates/
  templatetags/
  test/
  views/
  __init__.py
  app.py
  defaults.py
~~~

- **apps/** 디렉토리에는 **app** 들이 포함되어 있다.
