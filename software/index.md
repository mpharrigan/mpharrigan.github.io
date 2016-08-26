---
layout: fullpage
title: Software
active: software
---

<!-- see _data/content/software.yaml for content -->
{% for cont in site.data.content.software %}
<div class="row">
  <div class="col-lg-2 col-sm-3">
    <img src="{{cont.image}}" class="img-fluid" />
  </div>
  <div class="col-lg-7 col-sm-9">
    <h2>{{cont.title}}</h2>
    <ul class="nav nav-inline">
      {%for link in cont.links%}
      <li class="nav-item">
      <a class="nav-link" href="{{link.href}}">{{link.text}}</a>
      </li>
      {%endfor%}
    </ul>

    {{cont.content | markdownify}}
  </div>
</div>
{% endfor %}
