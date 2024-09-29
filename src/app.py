import argparse
import yaml
import flickrapi

parser = argparse.ArgumentParser(description='flickr_cli')
parser.add_argument('-v', '--verbose',action='store_true')
args = parser.parse_args()

with open('config/config.yml', 'r') as filehandle:
    config = yaml.safe_load(filehandle)
if args.verbose:
    print(config)

flickr = flickrapi.FlickrAPI(config['api_key'], config['api_secret'], format='parsed-json')

# 画像検索
result = flickr.photos.search(
    text = 'booty',
    per_page = 400,
    media = 'photos',
    sort = 'relevance',
    extras = 'url_q, licence'
)

photos = result['photos']
print(photos)
