import requests
import smtplib
import email.message

#pegar a informação 
requisicao = requests.get("https://economia.awesomeapi.com.br/last/USD-BRL")

requisicao_dicionario = requisicao.json()
#selecionando os parâmetros do dicionario especifico
#format float = são números com decimais

cotacao = float(requisicao_dicionario['USDBRL']['bid'])
print(cotacao)


#enviar um aviso por email

# ---- funcao
def enviar_email():
        corpo_email = """
        <p> Parágrafo1</p>
        <p> Parágrafo2</p>
        """

        msg = email.message.Message()
        msg['subject'] = "Assunto"
        msg['From']  = 'remetente'
        msg['To'] = 'destinatario'
        password = 'senha'
        msg.add_header('content-type', 'text/html')
        msg.set_payload(corpo_email)

        s = smtplib.SMTP('smtp.gmail.com:587')
        s.starttls()
        #LOGIN CREDENTIALS FOR SENDING THE MAIL
        s.login(msg['From'], password)
        s.sendmail(msg['From'], [msg['To']], msg.as_string().encode('utf-8'))
        print('Email enviado')

#codigo padrao 

#coment - requisicao json é um dicionario method a cima 


#deploy - heroku