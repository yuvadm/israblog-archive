from os import environ

BOT_NAME = 'israblog'

SPIDER_MODULES = ['israblog.spiders']
NEWSPIDER_MODULE = 'israblog.spiders'

# Crawl responsibly by identifying yourself (and your website) on the user-agent
USER_AGENT = 'Israblog Archive Spider (+https://github.com/yuvadm/israblog-archive)'

AWS_ACCESS_KEY_ID = environ.get('AWS_ACCESS_KEY_ID')
AWS_SECRET_ACCESS_KEY = environ.get('AWS_SECRET_ACCESS_KEY')
