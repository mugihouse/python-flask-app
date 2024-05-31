from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
  return render_template('top.html')

@app.route('/list')
def item_list():
  return render_template('list.html')

@app.route('/detail')
def item_detail():
  return render_template('detail.html')

if __name__ == '__main__':
  app.run(port=8000)
