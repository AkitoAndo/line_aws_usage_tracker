import json
import boto3
import os
from datetime import datetime

def lambda_handler(event, context):
    """
    LINEからのクエリを受け取り、過去の結果を返却するLambda関数
    """
    try:
        # S3クライアントの初期化
        s3 = boto3.client('s3')
        
        # 環境変数から設定を取得
        bucket_name = os.environ['S3_BUCKET_NAME']
        
        # メタデータを取得
        metadata_response = s3.get_object(
            Bucket=bucket_name,
            Key='metadata/last-update.json'
        )
        metadata = json.loads(metadata_response['Body'].read().decode('utf-8'))
        
        # 最新のレポートを取得
        year = metadata['year']
        month = metadata['month']
        report_key = f"cur-reports/{year}/{month}/cost-report.csv"
        
        # レポートの内容を取得
        report_response = s3.get_object(
            Bucket=bucket_name,
            Key=report_key
        )
        report_content = report_response['Body'].read().decode('utf-8')
        
        return {
            'statusCode': 200,
            'body': json.dumps({
                'message': 'Query processed successfully',
                'data': {
                    'last_update': metadata['last_update'],
                    'report_content': report_content
                }
            })
        }
        
    except Exception as e:
        return {
            'statusCode': 500,
            'body': json.dumps({
                'message': 'Error occurred while processing query',
                'error': str(e)
            })
        } 