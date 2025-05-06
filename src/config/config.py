import os

# AWS設定
AWS_REGION = os.getenv('AWS_REGION', 'ap-northeast-1')
S3_BUCKET_NAME = os.getenv('S3_BUCKET_NAME')

# LINE設定
LINE_CHANNEL_ACCESS_TOKEN = os.getenv('LINE_CHANNEL_ACCESS_TOKEN')
LINE_CHANNEL_SECRET = os.getenv('LINE_CHANNEL_SECRET')

# アプリケーション設定
APP_NAME = 'LINE AWS Usage Tracker'
APP_VERSION = '1.0.0' 