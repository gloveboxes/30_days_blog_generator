"""
Python app to read a blog.yaml and generate a blog file structure
and index.md markdown file from a template
"""

import datetime
import os
import sys
import pathlib
import jinja2   # https://pypi.org/project/Jinja2/
import oyaml as yaml

TEMPLATE_FILE = "template.md"
DAYS_FILE = "blog.yaml"


def validate_data(data):
    """Validate the yaml file."""

    previous_date = None

    if 'campaign' not in data:
        print("Missing campaign in yaml file")
        return False
    if 'slug' not in data['campaign']:
        print("Missing slug in yaml file")
        return False
    if 'name' not in data['campaign']:
        print("Missing name in yaml file")
        return False
    if 'blog_url' not in data['campaign']:
        print("Missing blog_url in yaml file")
        return False

    for item in data['campaign']['days']:
        if 'folder' not in item:
            print("Missing folder in yaml file")
            print(item)
            return False
        if 'title' not in item:
            print("Missing title in yaml file")
            print(item)
            return False
        if 'description' not in item:
            print("Missing description in yaml file")
            print(item)
            return False
        if 'authors' not in item:
            print("Missing authors in yaml file")
            print(item)
            return False

        try:

            item_date = datetime.datetime.strptime(
                item['folder'][:10], '%Y-%m-%d').date()

            # compare the date with the previous date
            if previous_date is not None and item_date < previous_date:
                print("Dates are not in order")
                print(item)
                return False

            previous_date = item_date

        except ValueError:
            print(
                "Invalid date in yaml file - the folder name must be in the format YYYY-MM-DD and optionally, followed with a dash and short description.")
            print(item)
            return False

    return True


def main(args):
    """RGenerate blog items from yaml file."""

    output_folder = args[1] if len(args) > 1 else 'blog'
    day = 0

    # Read the yaml file
    with open(DAYS_FILE, encoding='utf8') as f:
        data = yaml.load(f, Loader=yaml.Loader)

    if not validate_data(data):
        print("Error in yaml file")
        return

    # Read the template file
    template_loader = jinja2.FileSystemLoader(searchpath="./")
    template_env = jinja2.Environment(loader=template_loader)

    template = template_env.get_template(TEMPLATE_FILE)

    for item in data['campaign']['days']:
        day += 1
        item['day'] = day
        item['campaign'] = data['campaign']['name']
        item['slug'] = data['campaign']['slug']
        item['blog_url'] = data['campaign']['blog_url']

        output_text = template.render(item)

        pathlib.Path(os.path.join(output_folder, item['folder'])).mkdir(
            parents=True, exist_ok=True)
        filename = os.path.join(output_folder, item['folder'], 'index.md')

        with open(filename, 'w', encoding='utf8') as f:
            f.write(output_text)

    print("Done")


if __name__ == '__main__':
    main(sys.argv)
