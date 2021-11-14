import os
from flask import Flask, render_template, request, redirect
from flask_mail import Mail, Message
from form_contato import ContactForm, csrf

mail = Mail()

app = Flask(__name__)
SECRET_KEY = os.urandom(32)
app.config['SECRET_KEY'] = 'sworfish'
csrf.init_app(app)

app.config['MAIL_SERVER']='smtp.office365.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USERNAME'] = 'ciscorp@live.com'
app.config['MAIL_PASSWORD'] = 'okXnG3cr'
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True

mail.init_app(app)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/sobre')
def sobre():
    return render_template('sobre.html')

@app.route('/contato', methods=['POST', 'GET'])
def contato():
    form = ContactForm()
    if form.validate_on_submit():        
        print('-------------------------')
        print(request.form['name'])
        print(request.form['email'])
        print(request.form['subject'])
        print(request.form['message'])       
        print('-------------------------')
        send_message(request.form)
        return redirect('/sucesso')    

    return render_template('forms/contatos/contato.html', form=form)

@app.route('/sucesso')
def success():
    return render_template('forms/email/sucesso.html')

def send_message(message):
    print(message.get('name'))

    msg = Message(message.get('subject'), sender = message.get('email'),
            recipients = ['ciscorp.tech@gmail.com'],
            body= message.get('message')
    )  
    mail.send(msg)

if __name__ == "__main__":
    app.run(debug=True)