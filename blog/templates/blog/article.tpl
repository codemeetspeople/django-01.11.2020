{% extends 'core/base.tpl' %}
{% block title %} {{ article.title }} {% endblock %}
{% block body %}
    <h1> {{ article.title }} </h1>
    <hr />
    {{ article.content }}
{% endblock %}