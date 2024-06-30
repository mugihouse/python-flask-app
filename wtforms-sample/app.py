from flask import Flask, render_template, request

app = Flask(__name__)

from forms import UserInfoForm

@app.route('/', methods=['GET', 'POST'])
def show_enter():
  form = UserInfoForm(request.form)
  if request.method == "POST" and form.validate():
    return render_template('result.html', form=form)
  # POST以外と「form.validate()がfalse」
  return render_template('enter2.html', form=form)


if __name__ == '__main__':
    app.run()
