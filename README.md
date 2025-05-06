# LINE AWS Usage Tracker

AWS の利用状況を月 1 回更新し、ユーザーのクエリに対して過去の結果を返却するシンプルなシステムです。

## 機能

- 月 1 回の AWS 利用状況データ更新
- ユーザークエリに対する過去の結果返却

## システム構成

- AWS Cost and Usage Reports (CUR)
- Amazon S3
- AWS Lambda
- AWS EventBridge
- LINE Messaging API

## 開発フロー

詳細な開発フローは [docs/development_flow.md](docs/development_flow.md) を参照してください。
