from flask import Flask, render_template, session, redirect, url_for

app = Flask(__name__)
import os
# 乱数の設定
app.config['SECRET_KEY'] = os.urandom(24)

from forms import InputForm

@app.route('/', methods=['GET', 'POST'])
def input():
  form = InputForm()

  # POST
  if form.validate_on_submit():
    session['name'] = form.name.data
    session['email'] = form.email.data
    return redirect(url_for('output'))

  # GET
  if 'name' in session:
    form.name.data = session['name']
  if 'email' in session:
    form.email.data = session['email']
  # GETメソッド or フォームのバリデーションを通過しなかった場合
  return render_template('input.html', form=form)

@app.route('/output')
def output():
  return render_template('output.html')


if __name__ == '__main__':
  app.run()
