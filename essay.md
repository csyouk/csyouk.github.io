---
title: Essay
layout: page
permalink: "/essay/"
---

{% for post in site.categories.essay %}
<ul>
  <li><a href="{{ post.url }}">{{ post.title }}</a></li>
</ul>
{% endfor %}
