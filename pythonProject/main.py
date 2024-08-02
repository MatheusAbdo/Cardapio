from flask import Flask,render_template, url_for
from forms import FormCriarConta, Formlogin



app = Flask(__name__)

app.config['SECRET_KEY']='76a1f213ec1dcfffa4365c56721164be'

@app.route('/')
def home():
    foto_logo_cardapio = url_for('static', filename='fotos/logocardapio.JPG')
    foto_logo =url_for('static', filename='fotos/LogoEspetinhoOficial.JPG')
    foto_espeto = url_for('static', filename='fotos/logoespetinho.JPG')
    return render_template('home.html',foto_logo=foto_logo,foto_espeto=foto_espeto,
    foto_logo_cardapio=foto_logo_cardapio)


@app.route('/contato')
def contato():
    return render_template('contato.html')

@app.route('/login',methods=['GET','POST'])
def login():
    form_login = Formlogin()
    form_criarconta = FormCriarConta()
    return render_template('login.html',form_login=form_login, form_criarconta=form_criarconta)

if __name__ == '__main__':
    app.run(debug=True)
