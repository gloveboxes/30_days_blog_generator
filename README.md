# 30DaysOf Blog Scafolding

The #30DaysOf Python app will scofold out the blog structure for a #30Days blog campaign.

1. The index.md file will be created for each day from the template.md file.
1. The blog.yaml file will be used to configure the metadata for each day.

## Installation

```bash
pip3 install -r requirements.txt
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
        title: kick starting AI April!
        description: "Welcome to #AiApril! Join us for #30DaysOfAzureAI learning, skilling and discussions at https://aka.ms/ai-april"
        authors: [dglover, nitya]
        keywords: [ai-april, azure open ai]
        tags: [Azure AI, developer tools, onboarding, azure ai fundamentals, 30DaysOfAzureAI, recap]
        canonical:
        twitter:
          creator: dglover
          site: AzureAdvocates

      - folder: 2023-04-03-openia-sdk
        title: Dive into Azure OpenAI Service sdk
        description: "Let's dive into Azure OpenAI Service SDK"
        authors: [nitya]
        keywords: [ai-april, azure open ai service]
        tags: [Azure AI, developer tools, onboarding, power platform fundamentals, 30DaysOfLowCode, recap]
        canonical:
        twitter:
          creator: dglover
          site: AzureAdvocates
```

## Usage

Run the generator.py script to generate the blog posts. It will create a folder for each day in the output directory.

The generator will validate the blog.yaml file and will fail if the file is not valid.

```bash
python3 generator.py <optionally, specify the output directory. The default output folder is blog>
```
