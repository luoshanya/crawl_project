#导入
from scrapy import cmdline

# cmdline.execute(['scrapy','crawl','spider_csbk'])
#或者
cmdline.execute('scrapy crawl spider_csbk'.split())