# demo_scrapy
scrapyの使用感を掴むためのリポジトリ

# 起動方法メモ
```bash
# コンテナをビルド
docker compose build

# コンテナ起動
docker compose up -d

# コンテナに入る
docker compose exec app bash
```

# プロジェクト作成コマンド
```bash
# プロジェクトの雛形作成
poetry run scrapy startproject myproject

# Spiderの作成
poetry genspider myproject project_spider
```

# 実行メモ
```bash
# Scrapy実行（コンテナに入った状態で）
poetry run scrapy crawl myproject

# ファイル形式で出力する方法
poetry run scrapy crawl myproject -o output.json
```