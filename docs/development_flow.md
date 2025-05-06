# LINE AWS Usage Tracker 開発フロー

## 1. プロジェクト概要

LINE AWS Usage Tracker は、AWS の利用状況を月 1 回更新し、ユーザーのクエリに対して過去の結果を返却するシンプルなシステムです。

### 主な機能

- 月 1 回の AWS 利用状況データ更新
- ユーザークエリに対する過去の結果返却

## 2. 開発環境のセットアップ

### 必要なツール

- Python 3.8 以上
- AWS CLI
- LINE Messaging API

### 環境変数の設定

- AWS 認証情報
- LINE Channel Access Token
- LINE Channel Secret

## 3. アーキテクチャ設計

### システム構成

1. AWS Cost and Usage Reports (CUR)

   - レポート設定
     - レポート名
     - 時間単位（月次）
     - レポート形式（CSV）
     - レポート内容（基本的なコスト情報）

2. Amazon S3

   - バケット構造
     ```
     s3://line-aws-usage-tracker/
     ├── cur-reports/                    # CURレポートの保存先
     │   └── YYYY/MM/                   # 年月ごとのディレクトリ
     │       └── cost-report.csv        # 月次レポート
     │
     ├── query-results/                 # クエリ結果の保存先
     │   └── YYYY/MM/                  # 年月ごとのディレクトリ
     │       └── results.json          # クエリ結果
     │
     └── metadata/                      # メタデータ
         └── last-update.json          # 最終更新日時などの情報
     ```
   - アクセス制御
     - CUR レポート用の IAM ロール
     - Lambda 関数用の IAM ロール
   - ライフサイクルルール
     - 古いレポートの自動削除（オプション）

3. AWS Lambda Functions

   - 月次データ更新関数
   - ユーザークエリ応答関数

4. AWS EventBridge

   - 月 1 回の定期実行スケジューリング

5. LINE Messaging API
   - ユーザークエリの受信
   - 結果の返却

### データフロー

```
月次更新: AWS Cost and Usage Reports → S3 → 保存
ユーザークエリ: LINE → Lambda → S3(過去データ) → LINE
```

## 4. 実装手順

1. プロジェクト構造の作成

   ```
   line_aws_usage_tracker/
   ├── src/
   │   ├── lambda/
   │   │   ├── monthly_update/
   │   │   └── query_handler/
   │   └── config/
   ├── docs/
   └── terraform/
   ```

2. 各コンポーネントの実装
   - CUR 設定の実装
   - S3 バケットの設定
   - Lambda 関数の実装
     - 月次データ更新
     - ユーザークエリ応答
   - EventBridge ルールの設定（月 1 回）
