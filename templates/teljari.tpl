<a href="/karfa"><img class="karfa" src="/static/offer-kart.png"></a> < smelltu á korfuna

{% if 'karfa' in session: %}
    <span>( {{ fjoldi }} )</span>
{% else %}
    <span>( 0 )</span>
{% endif %}