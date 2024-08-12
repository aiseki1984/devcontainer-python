import MySQLdb

def connect_to_database():
    try:
        # MySQLデータベースに接続
        connection = MySQLdb.connect(
            host="mysql",      # MySQLサーバーのホスト名
            user="test",  # MySQLユーザー名
            passwd="test", # MySQLユーザーパスワード
            db="test", # 接続するデータベース名
            charset="utf8mb4"  # 文字コードを指定
        )

        print("Successfully connected to the database")
        
        # カーソルを作成
        cursor = connection.cursor()

        table_name = "books"

        # SQLクエリを実行
        cursor.execute("SELECT * FROM " + table_name)

        # 結果を取得
        results = cursor.fetchall()

        # 結果を出力
        for row in results:
            print(row)

    except MySQLdb.Error as e:
        print(f"Error while connecting to MySQL: {e}")
    finally:
        if connection:
            connection.close()
            print("MySQL connection is closed")


if __name__ == "__main__":
    # 使用例
    connect_to_database()
