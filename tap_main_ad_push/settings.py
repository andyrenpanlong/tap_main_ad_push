# -*- coding: utf-8 -*-

# Scrapy settings for tap_main_ad_push project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#     http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html
#     http://scrapy.readthedocs.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'tap_main_ad_push'

SPIDER_MODULES = ['tap_main_ad_push.spiders']
NEWSPIDER_MODULE = 'tap_main_ad_push.spiders'


# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'tap_main_ad_push (+http://www.yourdomain.com)'

# Obey robots.txt rules
ROBOTSTXT_OBEY = True

# Configure maximum concurrent requests performed by Scrapy (default: 16)
#CONCURRENT_REQUESTS = 32

# Configure a delay for requests for the same website (default: 0)
# See http://scrapy.readthedocs.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
#DOWNLOAD_DELAY = 3
# The download delay setting will honor only one of:
#CONCURRENT_REQUESTS_PER_DOMAIN = 16
#CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
#COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
#TELNETCONSOLE_ENABLED = False

# Override the default request headers:
DEFAULT_REQUEST_HEADERS = {
  # 'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
  # 'Accept-Language': 'en',
    'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
    'Accept-Encoding':'gzip, deflate, br',
    'Accept-Language':'zh-CN,zh;q=0.8',
    'Cache-Control':'max-age=0',
    'Connection':'keep-alive',
    'Cookie':'locale=eyJpdiI6IlwvM2RhZkNcL2p4K2dMQWwzaGZuOVRRZz09IiwidmFsdWUiOiJqSXBEZEJMUCtuUjZMRE9JM3NOTk5BPT0iLCJtYWMiOiI5YTFhMDE4Yjk4ZGY5Y2YzM2M4MDJjZjYxNDkwNGRmMDU5ZmQwNWU4YmU1Y2NkMjExOTczOThlNWVmMmIwYzNkIn0%3D; tapadid=098d2c7b-9332-f092-41ea-9df55318d3ce; bottom_banner_hidden=1; remember_web_59ba36addc2b2f9401580f014c7f58ea4e30989d=eyJpdiI6IkJrUWVOZEZWdUM3Tk5Pa0RiWnRxXC93PT0iLCJ2YWx1ZSI6IkgrWGxUbUZtN0xwMDF3VEZES2dmSmRCRXAzak40bklKR3BOR3g1a2E5RSt5RWJ6OXVQZXBOdjE0NThDNXVHclMwUVprY09NOU1OTUdSQ3kwUENaaGRFWFRGalFlRk03bGlUTkVrSXBCUmZnPSIsIm1hYyI6ImY2YzY3NTczMjA3MzNkY2VjOTNkNDUyZmE0M2RiNDZlZjY5MzJmZGMyYzUwYzcxOTQ5MGE4ZDJjMzBjYjM3YzMifQ%3D%3D; acw_tc=AQAAAK0j2GTV7AoARM4T2vDtnpiCdhRt; _ga=GA1.2.1193393775.1504229158; _gid=GA1.2.530713293.1504707506; XSRF-TOKEN=eyJpdiI6IlwvVlZ4c2R2WVlrXC9Ub01QamZPQjhjUT09IiwidmFsdWUiOiJaV1FHdHdVc0JwTElTQWd4SkxVb0xlZGt3d0lnZTF2WGYyVUNPTU1yeTJxUDJFVjJyTDF5MnYxaFA2dHZGQUtua3lCQnNXemo4NWtkbEJyTEpJXC9SK0E9PSIsIm1hYyI6ImUyNThlZDg5NDZhNmJiODZhMjY2MDYwMDFlMmQyYWEzODBhOGNjN2E3Njc0NzgxOWJlZDAzNWNjY2E5MWUzM2YifQ%3D%3D; tap_sess=eyJpdiI6ImFGY0hxT1pEQ05NRmJPZnpaRUxEOWc9PSIsInZhbHVlIjoiR0R5KzJNVjY5S3Y2bXB4QUxyQzJsUXZjMzMrdFR1YU95OEVJeFJEekRaRGE0NHFMTVlEdks1MlNydEJhVEtCajNLOWNsQllSbUhHRHV5TmhQNkpvSXc9PSIsIm1hYyI6Ijc2NzM3Y2FhOWE1MzhiY2ZiYWRhZTc5NzFjOGQyYmVjZmEzNDFjMTNlYTZkMzJjOWY4Mzc4MzczZDUxZDE0NjIifQ%3D%3D',
    'Host':'www.taptap.com',
    'Upgrade-Insecure-Requests':'1',
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.90 Safari/537.36',
    'TEST-CSRF-TOKEN':'Iv9ZxWbozPGvsm1VLlgt7u3hQ3ILb7aJvWaHKzLK|string|eyJpdiI6IlwvcThLejZ0NlFYYW9KamRUdFZIXC9oZz09IiwidmFsdWUiOiJKUE43b0RGS3dVNTIwZHRYRDYyUVg0MTJEeUx6ZFhOakZ3SGFNb1hvRGh6RjB2R0tCTVJFcVlvZ1E2V3VvSjZQN1M5aXJuaXpcLzhSZ0FmcThwTWVCRUE9PSIsIm1hYyI6IjkzZDUzZWI2MGY1YzM2YjYxMzY1MTM2YTA2OGM2MzU4OTNjZmVjODhlYWI1MjU0ZGVjNWY3MWNhMTExOWZhOTcifQ==|string',
    'X-Requested-With':'XMLHttpRequest',
    'X-XSRF-TOKEN':'eyJpdiI6IlwvcThLejZ0NlFYYW9KamRUdFZIXC9oZz09IiwidmFsdWUiOiJKUE43b0RGS3dVNTIwZHRYRDYyUVg0MTJEeUx6ZFhOakZ3SGFNb1hvRGh6RjB2R0tCTVJFcVlvZ1E2V3VvSjZQN1M5aXJuaXpcLzhSZ0FmcThwTWVCRUE9PSIsIm1hYyI6IjkzZDUzZWI2MGY1YzM2YjYxMzY1MTM2YTA2OGM2MzU4OTNjZmVjODhlYWI1MjU0ZGVjNWY3MWNhMTExOWZhOTcifQ=='
}

# Enable or disable spider middlewares
# See http://scrapy.readthedocs.org/en/latest/topics/spider-middleware.html
#SPIDER_MIDDLEWARES = {
#    'tap_main_ad_push.middlewares.TapMainAdPushSpiderMiddleware': 543,
#}

# Enable or disable downloader middlewares
# See http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html
#DOWNLOADER_MIDDLEWARES = {
#    'tap_main_ad_push.middlewares.MyCustomDownloaderMiddleware': 543,
#}

# Enable or disable extensions
# See http://scrapy.readthedocs.org/en/latest/topics/extensions.html
#EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
#}

# Configure item pipelines
# See http://scrapy.readthedocs.org/en/latest/topics/item-pipeline.html
#ITEM_PIPELINES = {
#    'tap_main_ad_push.pipelines.TapMainAdPushPipeline': 300,
#}

# Enable and configure the AutoThrottle extension (disabled by default)
# See http://doc.scrapy.org/en/latest/topics/autothrottle.html
#AUTOTHROTTLE_ENABLED = True
# The initial download delay
#AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
#AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
#AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
#AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# See http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
#HTTPCACHE_ENABLED = True
#HTTPCACHE_EXPIRATION_SECS = 0
#HTTPCACHE_DIR = 'httpcache'
#HTTPCACHE_IGNORE_HTTP_CODES = []
#HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'
