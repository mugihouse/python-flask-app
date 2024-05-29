from flask import Flask

# インスタンス作成
app = Flask(__name__)

# ルーティング
@app.route('/')
def hello_world():
  return '<h1>ハローワールド</h1>'

# 実行
if __name__ == '__main__':
  app.run(port=8000)
