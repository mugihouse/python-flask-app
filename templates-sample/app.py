from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
  return render_template('top.html')

@app.route('/list')
def item_list():
  return render_template('list.html')

@app.route('/detail/<int:id>')
def item_detail(id):
  return render_template('detail.html', show_id=id)

@app.route('/multiple')
def show_jinja_multiple():
  word1 = "テンプレートエンジン"
  word2 = "神社"
  return render_template('jinja/show1.html', temp= word1, jinja=word2)

@app.route('/dict')
def show_jinja_dict():
  words = {
    'temp': "てんぷれーとえんじん",
    'jinja': "じんじゃ"
  }
  return render_template('jinja/show3.html', key = words)

@app.route('/list2')
def show_jinja_list():
  hero_list = ['桃太郎', '金太郎', '浦島太郎']
  return render_template('jinja/show4.html', users = hero_list)

class Hero:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def __str__(self):
    return f'名前：{self.name} 年齢：{self.age}'

@app.route('/class')
def show_jinja_class():
  hana = Hero('花咲かじいさん', 99)
  return render_template('jinja/show5.html', user = hana)

class Item:
  def __init__(self, id, name):
    self.id = id
    self.name = name
  def __str__(self):
    return f'商品ID:{self.id} 商品名:{self.name}'

@app.route('/for_list')
def show_for_list():
  item_list = [Item(1, "団子"), Item(2, "肉まん"), Item(3, "どら焼き")]
  return render_template('for_list.html', items = item_list)

@app.route('/if_detail/<int:id>')
def show_if_detail(id):
  item_list = [Item(1, "団子"), Item(2, "肉まん"), Item(3, "どら焼き")]
  return render_template('if_detail.html', show_id = id, items = item_list)

@app.route('/if')
@app.route('/if/<target>')
def show_jinja_if(target="colorless"):
  print(target)
  return render_template('jinja/if_else.html', color=target)

if __name__ == '__main__':
  app.run(port=8000)
