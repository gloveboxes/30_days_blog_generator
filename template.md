---
slug: {{slug}}-day{{day}}
title: {{ day }}. {{ title }}s
authors: [ authors ]
draft: true
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
  <meta name="twitter:image" content="{{ blog_url }}/{{ slug }}-day{{ day }}/twitter.png" />
  <meta name="twitter:card" content="summary_large_image" />
  {% if twitter['creator'] %}<meta name="twitter:creator" content="{{ twitter['creator'] }}" />{% endif %}
  {% if twitter['site'] %}<meta name="twitter:site" content="@{{ twitter['site'] }}" /> {% endif %}
  {% endif %}
  <link rel="canonical" {% if canonical %}href="{{ canonical }}" {% else %} href="{{ blog_url }}/{{ slug }}-day{{ day }}" {% endif %} />

</head>

Welcome to `Day {{ day }}` of {{ campaign }}!

## What We'll Cover

<!--
- Azure OpenAI Service
- Azure OpenAI Python SDK
 -->

## Introduction

{{ description }}