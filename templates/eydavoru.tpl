{% extends "base-karfa.html" %}

{% block title %}
    Vefverslun - vöru eytt
{% endblock %}

{% block refresh %}
    <meta http-equiv="refresh" content="1; url={{ url_for('karfa') }}">
{% endblock %}

{% block content %}
    <h1> Vöru út körfu hefur verið eytt...</h1>
{% endblock %}