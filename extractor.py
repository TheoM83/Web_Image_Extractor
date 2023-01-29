import argparse
import re
import requests
import os

parser = argparse.ArgumentParser()
parser.add_argument('url', help='The URL to scrape for image URLs')
parser.add_argument('-d', '--directory', help='The directory to save the images to')
parser.add_argument('-i', '--include', help='A string to include in the image URL', nargs='+')
parser.add_argument('-e', '--exclude', help='A string to exclude from the image URL', nargs='+')
parser.add_argument('-f', '--format', help='The image format to save (e.g. png, jpg, jpeg)', nargs='+', default=['png', 'jpg', 'jpeg'])
parser.add_argument('-r', '--replace', help='Replace existing files with the same name', action='store_true')
args = parser.parse_args()

url = args.url
directory = args.directory
include = args.include
exclude = args.exclude
formats = args.format
replace = args.replace

if directory and not os.path.exists(directory):
    os.makedirs(directory)

response = requests.get(url)
html_content = response.content

image_urls = list(set(re.findall('http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', str(html_content))))

print("Image URLs found:")
for url in image_urls:
    if any(url.endswith('.' + format) for format in formats):
        if include:
            include_found = False
            for inc in include:
                if inc in url:
                    include_found = True
                    break
            if not include_found:
                continue
        if exclude:
            exclude_found = False
            for exc in exclude:
                if exc in url:
                    exclude_found = True
                    break
            if exclude_found:
                continue
        print(url)
        if directory:
            response = requests.get(url)
            filename = os.path.join(directory, url.split('/')[-1])
            if not os.path.exists(filename) or replace:
                with open(filename, 'wb') as f:
                    f.write(response.content)
