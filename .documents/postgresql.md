# PostgreSQL Docker コンテナでの基本操作

PostgreSQL 17.4 のコンテナでの操作方法を紹介します。

## コンテナへのログイン

```bash
# コンテナIDの確認
docker ps

# psqlコマンドでコンテナ内のPostgreSQLに接続
docker exec -it [コンテナID] psql -U postgres
```

または、コンテナ内の bash シェルに入る場合：

```bash
docker exec -it [コンテナID] bash
```

## PostgreSQL の基本操作

### データベース操作

```sql
-- データベース一覧の表示
\l

-- 新しいデータベースの作成
CREATE DATABASE mydb;

-- データベースの選択
\c mydb

-- データベースの削除
DROP DATABASE mydb;
```

### テーブル操作

```sql
-- テーブルの作成
CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    email VARCHAR(100) UNIQUE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- テーブル一覧の表示
\dt

-- テーブル構造の確認
\d users

-- テーブルの削除
DROP TABLE users;
```

### データ操作

```sql
-- データの挿入
INSERT INTO users (name, email) VALUES ('山田太郎', 'taro@example.com');

-- データの取得
SELECT * FROM users;

-- 条件付きデータ取得
SELECT * FROM users WHERE name LIKE '山田%';

-- データの更新
UPDATE users SET email = 'new_taro@example.com' WHERE id = 1;

-- データの削除
DELETE FROM users WHERE id = 1;
```

### インデックス操作

```sql
-- インデックスの作成
CREATE INDEX idx_users_name ON users (name);

-- インデックス一覧の表示
\di

-- インデックスの削除
DROP INDEX idx_users_name;
```

### ユーザー管理

```sql
-- 新しいユーザーの作成
CREATE USER app_user WITH PASSWORD 'password123';

-- ユーザー権限の付与
GRANT ALL PRIVILEGES ON DATABASE mydb TO app_user;
GRANT ALL PRIVILEGES ON TABLE users TO app_user;

-- ユーザー一覧表示
\du

-- ユーザーの削除
DROP USER app_user;
```

### トランザクション

```sql
-- トランザクション開始
BEGIN;

-- SQL文を実行
INSERT INTO users (name, email) VALUES ('佐藤次郎', 'jiro@example.com');
UPDATE users SET email = 'updated_jiro@example.com' WHERE name = '佐藤次郎';

-- コミット
COMMIT;

-- または、ロールバック
ROLLBACK;
```

### psql 便利コマンド

```
\? -- ヘルプ表示
\h -- SQLコマンドのヘルプ
\q -- PostgreSQLを終了
\timing -- クエリ実行時間の表示切替
\i file.sql -- ファイルからSQLを実行
\e -- エディタでクエリ編集
\copy -- CSV等のインポート/エクスポート
```

## サンプルデータの作成と操作例

```sql
-- サンプルデータベースの作成
CREATE DATABASE shop;
\c shop

-- 商品テーブルの作成
CREATE TABLE products (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    price INTEGER NOT NULL,
    stock INTEGER NOT NULL DEFAULT 0,
    description TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- サンプルデータの挿入
INSERT INTO products (name, price, stock, description) VALUES
    ('ノートPC', 80000, 10, 'スタンダードモデル'),
    ('タブレット', 40000, 15, '10インチディスプレイ'),
    ('スマートフォン', 60000, 20, 'ハイエンドモデル'),
    ('マウス', 3000, 50, 'ワイヤレス'),
    ('キーボード', 5000, 30, 'メカニカル');

-- データの取得と集計
SELECT COUNT(*) FROM products;
SELECT SUM(price * stock) AS total_inventory_value FROM products;
SELECT name, price FROM products ORDER BY price DESC;
```

これらの操作を通じて、PostgreSQL の基本的な使い方が理解できます。より詳細な情報は公式ドキュメントを参照してください。
