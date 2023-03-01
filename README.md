# 30DaysOf Blog Scafolding

The #30DaysOf Python app will scofold out the blog structure for a #30Days blog campaign.

## Installation

```bash
pip install -r requirements.txt
```

## Content Configuration

A blog.yaml file is used to configure the structure and the metadata of the blog posts. You'll find the blog.yaml file in the root of the project.

### Example blog.yaml

```yaml
campaign: 
  name: 30DaysOfAzureAI
  slug: 2023
  blog_url: https://microsoft.github.io/Low-Code/blog

  days:
      - folder: 2023-03-29-openia-intro
        title: Hello, Azure OpenAI Service!
        description: "Welcome to #AiApril! Join us for #30DaysOfAzureAI learning, skilling and discussions at https://aka.ms/ai-april"
        authors: [dglover, nitya]
        keywords: [ai-april, azure open ai]
        tags: [Azure AI, developer tools, onboarding, power platform fundamentals, 30DaysOfLowCode, recap]
        canonical:
        twitter:
          creator: dglover
          site: AzureAdvocates
          
      - folder: 2023-03-29-openia-api
        title: Hello, Azure OpenAI Service!
        description: "Welcome to #AiApril! Join us for #30DaysOfAzureAI learning, skilling and discussions at https://aka.ms/ai-april"
        authors: [dglover, nitya]
        keywords: [ai-april, azure open ai]
        tags: [Azure AI, developer tools, onboarding, power platform fundamentals, 30DaysOfLowCode, recap]
        canonical:
        twitter:
          creator: dglover
          site: AzureAdvocates
```yaml

## Usage

Run the generator.py script to generate the blog posts. It will create a folder for each day in the output directory.

```bash
python generator.py <output directory>
```
