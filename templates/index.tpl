{% extends "base.html" %}

{% block title %}
    <title>Vefverslun</title>
{% endblock %}

{% block content %}
    <h1 class="litur">Vörur</h1>
    <section class="rapper">
        {% for i in v %}
            <div id="item{{ i[0] }}">
                <h2> {{ i[1] }} </h2>
                <img src="/static/{{ i[2] }}">

                <h2>Verð: <a href="/add/{{i[0]}}">{{ i[3] }}kr</a><h2>
            </div>
        {% endfor %}
    </section>
{% endblock %}