{% extends 'core/base.tpl' %}
{% block title %} Home page {% endblock %}
{% block body %}
    <h1> Wellcome to blog! </h1>
    <h2> Categories: </h2>
    <hr />
    {% for category in categories %}
        <h3>{{ category.title }}</h3>
        <ol>
            {% for article in category.articles.all() %}
                <li><a href="/articles/{{article.id}}">{{ article.title }}</a></li>
            {% endfor %}
        </ol>
    {% endfor %}
{% endblock %}
