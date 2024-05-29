from flask import Flask

app = Flask(__name__)

# routing
# トップページ
@app.route('/')
def index():
  return '<h1>Topページ</h1>'

@app.route('/list')
def item_list():
  return '<h1>商品一覧ページ</h1>'

@app.route('/detail')
def item_detail():
  return '<h1>商品詳細ページ</h1>'

if __name__ == '__main__':
  app.run(port=8000)
