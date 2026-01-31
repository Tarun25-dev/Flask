"""
Jinja2: 
>> Jinja2 is a template engine, it help flask to insert python data into HTML.
>> flask uses jinja2 by default

1. Variables:{{ }}

<p>Name: {{ name }}</p>
<p>Branch: {{ branch }}</p>

2. Conditions:{% if %}

{% if user %}
  <h2>Welcome {{ user }}</h2>
{% else %}
  <h2>Welcome Guest</h2>
{% endif %}

3. Loops:{% for %}

<ul>
{% for skill in skills %}
  <li>{{ skill }}</li>
{% endfor %}
</ul>

"""
