import json
import boto3
import os
from datetime import datetime

def lambda_handler(event, context):
    """
    AWS Cost and Usage Reportsの月次データを取得し、S3に保存するLambda関数
    """
    try:
        # S3クライアントの初期化
        s3 = boto3.client('s3')
        
        # 現在の年月を取得
        current_date = datetime.now()
        year = str(current_date.year)
        month = str(current_date.month).zfill(2)
        
        # S3のパスを設定
        bucket_name = os.environ['S3_BUCKET_NAME']
        key = f"cur-reports/{year}/{month}/cost-report.csv"
        
        # メタデータを更新
        metadata = {
            'last_update': current_date.isoformat(),
            'year': year,
            'month': month
        }
        
        # メタデータをS3に保存
        s3.put_object(
            Bucket=bucket_name,
            Key='metadata/last-update.json',
            Body=json.dumps(metadata),
            ContentType='application/json'
        )
        
        return {
            'statusCode': 200,
            'body': json.dumps({
                'message': 'Monthly update completed successfully',
                'metadata': metadata
            })
        }
        
    except Exception as e:
        return {
            'statusCode': 500,
            'body': json.dumps({
                'message': 'Error occurred during monthly update',
                'error': str(e)
            })
        } 