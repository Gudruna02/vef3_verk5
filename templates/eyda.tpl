{% extends "base-karfa.html" %}

{% block title %}
    Vefverslun - körfu eytt
{% endblock %}

{% block refresh %}
    <meta http-equiv="refresh"content="2; url={{ url_for('index') }}">
{% endblock %}

{% block content%}
    <h1> Körfu hefur verið eytt..</h1>
{% endblock %}