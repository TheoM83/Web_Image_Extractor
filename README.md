# Web_Image_Extractor
A tool that permits to extract every image of a webpage.

## Setup

### Download the repo
 ```git clone https://github.com/TheoM83/Web_Image_Extractor/new/main?readme=1```

### Install the requirements
```pip install -r requirements.txt```

## Usage : 

### Options
```
usage: extractor.py [-h] [-d DIRECTORY] [-i INCLUDE [INCLUDE ...]] [-e EXCLUDE [EXCLUDE ...]] [-f FORMAT [FORMAT ...]] [-r] url

positional arguments:
  url                   The URL to scrape for image URLs

options:
  -h, --help            show this help message and exit
  -d DIRECTORY, --directory DIRECTORY
                        The directory to save the images to
  -i INCLUDE [INCLUDE ...], --include INCLUDE [INCLUDE ...]
                        A string to include in the image URL
  -e EXCLUDE [EXCLUDE ...], --exclude EXCLUDE [EXCLUDE ...]
                        A string to exclude from the image URL
  -f FORMAT [FORMAT ...], --format FORMAT [FORMAT ...]
                        The image format to save (e.g. png, jpg, jpeg)
  -r, --replace         Replace existing files with the same name
  ```

### Example
```python script.py http://www.example.com -d images -i image1 image2 -e private```

