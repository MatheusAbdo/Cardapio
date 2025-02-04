from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired,Length, Email, EqualTo


class FormCriarConta(FlaskForm):
    username = StringField('Nome do Usuário', validators=[DataRequired()])
    email = StringField('E-mail', validators=[DataRequired(),Email()])
    senha = PasswordField('Senha', validators=[DataRequired(), Length(6,20)])
    confirmacao_senha = PasswordField('Confirmação de Senha', validators=[DataRequired(),EqualTo('senha')])
    botao_criar_conta = SubmitField('Criar Conta')

class Formlogin(FlaskForm):
    email = StringField('E-mail',validators=[DataRequired(), Email()])
    senha = PasswordField('Senha',validators=[DataRequired(),Length(6,20)])
    lembrar_dados = BooleanField('Lembrar Dados de Acesso')
    botao_login = SubmitField('Fazer Login')