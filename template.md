---
slug: {{slug}}-day{{day}}
title: "{{ day }}. {{ emoji }}{{ title }}"
authors: {{ authors }}
draft: false
hide_table_of_contents: false
toc_min_heading_level: 2
toc_max_heading_level: 3
{% if keywords %}keywords: {{ keywords }}{% endif %}
{% if tags %}tags: {{ tags }}{% endif %}

image: https://microsoft.github.io/Low-Code/img/og/30-01.png
description: "{{ description }}"
---

<head>
{% if twitter %}
  <meta name="twitter:url" content="{{ blog_url }}/{{ slug }}-day{{ day }}" />
  <meta name="twitter:title" content="{{ title }}" />
  <meta name="twitter:description" content="{{ description }}" />
  <meta name="twitter:image" content="{{ blog_url }}/{{ slug }}-day{{ day }}/banner.png" />
  <meta name="twitter:card" content="summary_large_image" />
  {% if twitter['creator'] %}<meta name="twitter:creator" content="{{ twitter['creator'] }}" />{% endif %}
  {% if twitter['site'] %}<meta name="twitter:site" content="@{{ twitter['site'] }}" /> {% endif %}
  {% endif %}
  <link rel="canonical" {% if canonical %}href="{{ canonical }}" {% else %} href="{{ blog_url }}/{{ slug }}-day{{ day }}" {% endif %} />

</head>

- 📧 [Subscribe to the Azure AI Developer Newsletter](https://microsoft.github.io/Low-Code/subscribe)
- 📌 [Ask a question about this post on GitHub Discussions](https://github.com/AzureAiDevs/Discussions/discussions/categories/{{ day }}-{{ title|lower|replace(":", "")|replace(" ", "-") }})

<!-- 

PLEASE READ THIS BEFORE EDITING THIS FILE

- This file is a template for the daily posts of the #30DaysOf series.

- TWITTER IMAGE: 
  - Create a image suitable for twitter and place it in the same folder as this file. 
  - The image must be named twitter.png
  - The ideal image size is 1600x900 pixels.

 -->

## Day _{{ day }}_ of #{{ campaign }}

**{{ description }}**

{% include 'content/' + folder + '/intro.md' ignore missing %}

## What We'll Cover

{% set template = "## What We'll Cover" %}
{% include 'content/' + folder + '/covered.md' ignore missing %}

<!--
- Covered 1
- Covered 2
- Covered 3
 -->

![Empty Banner Placeholder](banner.png)

{% set template = '## Introduction' %}
{% include 'content/' + folder + '/body.md' ignore missing %}

<!-- Content for the day goes here. -->

## Learn More

{% if canonical -%}
To learn more, check out this [article]({{ canonical }}).
{% endif %}
