---
layout: fullpage
title: Research
active: research
---

<!-- see _data/content/research.yaml for content -->
{% for cont in site.data.content.research %}
<div class="row">
<div class="col-sm-3">
<img src="{{cont.image}}" class="img-fluid" />
</div>
<div class="col-sm-9">
<h2>{{cont.title}}</h2>
{{cont.content | markdownify}}
</div>
</div>
{% endfor %}

<div class="row"><div class="col-lg-9 col-xs-12">
<h2>Papers</h2>
{% include_relative citations.html %}
</div></div>

