from flask import Flask, render_template, url_for, redirect, session, request
from flask_wtf import FlaskForm
from wtforms import SubmitField, StringField, PasswordField, EmailField
from wtforms.validators import InputRequired
from dataclasses import dataclass
import requests
from mcrcon import MCRcon
import subprocess

app = Flask(__name__)
app.config["SECRET_KEY"] = "4lwklskd103i59tu24ejdws@@$!@"

class LoginForm(FlaskForm):
    username = StringField("Nickname no Servidor:", validators=[InputRequired()])
    purchase = SubmitField("Clique aqui para comprar!")

@dataclass
class Farm:
    nome:str
    descricao:str
    preco:float
    imagem:str
    automatica:str
    rendimentomanual:int
    rendimentoautomatico:int
    video:str

@dataclass
class Set:
    nome:str
    descricao:str
    preco:float
    imagem:str
    habilidades:str
    debuff:str
    armadura:str
    arma:str
    video:str

produtos = [
    Farm(
        nome="Farm de ouro (Zumbi)",
        descricao="Consiga ouro matando zumbis da maneira mais fácil com esta farm-armadilha!",
        preco=24.99,
        imagem="/static/assets/zombie_farm.png",
        automatica="Sim",
        rendimentomanual=280,
        rendimentoautomatico=120,
        video="/static/assets/zombiefarm.mp4"
    )
]
sets = [
    Set(
        nome="Kit do Berserker",
        descricao="Incorpore um bárbaro brutal, e destrúa seus inimigos com sua fúria, sem sequer se preocupar com você mesmo!",
        preco=11.99,
        imagem="/static/assets/kitberserker.png",
        habilidades="Força 5, Velocidade 2 Permanentes",
        debuff="Tenha apenas 5 corações de vida",
        armadura="Set de Couro Completo: Todas as proteções e durabilidade 5",
        arma="Machado de Netherite: Afiação 6, Durabilidade 6, Aspecto Flamejante 2",
        video="/static/assets/berserker.mp4"
    ),
    Set(
        nome="Kit da Justiça",
        descricao="Seja um guerreiro da justiça, e recebe uma enorme benção com grandes poderes mágicos e regenerativos!",
        preco=11.99,
        imagem="/static/assets/kitjustica.png",
        habilidades="Tenha Efeito de Regeneração e Resistência Permanentes.",
        debuff="Fraco em Combates de Longa Duração.",
        armadura="Set de Ouro Completo: Proteção 7, Durabilidade 7",
        arma="Uma Espada de Abençoada Capaz de Invocar Relâmpagos em Seus Inimigos (Afiação 7 E Durabilidade 7)",
        video="/static/assets/justica.mp4"
    ),
    Set(
        nome="Kit da Determinação",
        descricao="Seja um Bravo Guerreiro que Nunca Desiste! Nenhum Inimigo Consegue Bater de Frente!",
        preco=11.99,
        imagem="/static/assets/kitdeterminacao.png",
        habilidades="Tenha Uma Armadura Imbatível e Cause Lentidão Aos Seus Inimigos! Assuste-os Com Toda a Sua Força de Vontade",
        debuff="Fraco Contra Explosões, Fraco em Combates de Longa Duração, Fraco em Perseguições",
        armadura="Set De Netherite Com Todas as Proteções Nível 10, Receba Efeito de Decomposição Permanente",
        arma="Espada de Netherite com Afiação 6 (Causa Lentidão aos Inimigos ao Atacar)",
        video="/static/assets/determinacao.mp4"
    ),
    Set(
        nome="Kit do Desbravador",
        descricao="Seja um Guerreiro Astuto e Derrube Seus Inimigos Com um Dano Imenso (Eles nem vão se dar conta!).",
        preco=11.99,
        imagem="/static/assets/kitdesbravador.png",
        habilidades="Tenha uma Leve Armadura, Adequada Para Um Guerreiro Astuto. Cause um Dano Absurdo  Envenene os Inimigos",
        debuff="Fraco em Combates de Longa Duração, Fraco Contra Inimigos Muito Resistentes, Sofre Muito Dano",
        armadura="Um Traje Completo Com Proteção 2, Demais Proteções 5",
        arma="Espada de Ferro com Durabilidade 4 (Causa Muito Dano aos Inimigos e Os Envenena), Recupera Parte de Sua Vida Ao Atacar",
        video="/static/assets/desbravador.mp4"
    ),
    Set(
        nome="Kit do Bruxo",
        descricao="Seja um Bruxo Poderoso e Cause um Dano Absurdo Com Sua Besta",
        preco=11.99,
        imagem="/static/assets/kitbruxo.png",
        habilidades="Tenha Extrema Resistência Contra Feitiços! Atire um Dardo Enfeitiçado Que Explode Seus Inimigos Com Magia Escura",
        debuff="Fraco à Curta Distância, Fraco Contra Dano Físico",
        armadura="Um Simples Traje Que Te Protege Contra Feitiços (Armadura de Couro Com Proteção Contra Explosões 10)",
        arma="Besta do Bruxo Encantada com Durabilidade 4",
        video="/static/assets/bruxo.mp4"
    ),
        Set(
        nome="Botas Dracônicas",
        descricao="Seja um Guerreiro Mestiço e Libere Seus Poderes de Dragão!",
        preco=19.99,
        imagem="/static/assets/botasdraconicas.png",
        habilidades="Liberte o Poder do Dragão, Ruja Causando Dano à Todos os Inimigos em Linha Reta, Tenha Um Poderoso Cristal Que Regenera Absurdamente Sua Vida.",
        debuff="Forte em Combate de Longa Duração, Fraco Contra o Cristal, Limitado à Área do Cristal",
        armadura="Botas Dracônicas",
        arma="N/A",
        video="/static/assets/botasdraconicas.mp4"
    ),
        Set(
        nome="Elytra",
        descricao="Voe e Explore o Mundo à Medida que Quiser!",
        preco=19.99,
        imagem="/static/assets/elytra.png",
        habilidades="Tenha a Habilidade de Voar Livremente Pelo Mundo",
        debuff="Não Pode Ser Usado Para Combate",
        armadura="Elytra",
        arma="N/A",
        video="/static/assets/elytra.mp4"
    )
]


@app.route('/purchase', methods=["POST"])
def purchase():
    nickname = request.form.get('username')
    plan_type = request.form.get('plan_type')
    session['nickname'] = nickname
    if plan_type == 'mensal':
        return redirect(f"https://pay.kiwify.com.br/k3ejHtE?nickname={nickname}")
    elif plan_type == 'trimestral':
        return redirect(f"https://pay.kiwify.com.br/AHrVA4p?nickname={nickname}")
    return redirect(url_for('vip'))


# Função para executar comando no servidor Minecraft via screen
def run_server_command(command):
    screen_name = "server"
    try:
        subprocess.run(['screen', '-S', screen_name, '-p', '0', '-X', 'stuff', f"{command}\n"], check=True)
        print(f"Command '{command}' sent to screen '{screen_name}'")
    except subprocess.CalledProcessError as e:
        print(f"Failed to send command '{command}' to screen '{screen_name}': {e}")


@app.route('/payment_confirmation', methods=['POST'])
def payment_confirmation():
    data = request.json
    if data and data.get('status') == 'compra_aprovada':
        nickname = data.get('nickname')
        if nickname:
            command = f"vip {nickname}"
            run_server_command(command)
            return "Success", 200
    return "Failure", 400


@app.route('/')
def index():
    return render_template('index.html', title="ValorKnights - Início")

@app.route('/vip')
def vip():
    form=LoginForm()
    return render_template('vip.html', title="ValorKnights - Comprar VIP", form=form)

@app.route('/loja')
def loja():
    return render_template('loja.html', title="ValorKnights - Loja", produtos=produtos, sets=sets)

@app.route('/registrar')
def registrar():
    pass

@app.route('/produto/<produto_nome>')
def produto(produto_nome):
    produto = next((prod for prod in produtos if prod.nome == produto_nome), None)
    if produto:
        return render_template('produto.html', produto=produto, tipo='Farm')
    else:
        set_item = next((set_item for set_item in sets if set_item.nome == produto_nome), None)
        if set_item:
            return render_template('produto.html', produto=set_item, tipo='Set')
        else:
            return "Produto não encontrado", 404


if __name__ == "__main__":
    app.run(host='0.0.0.0') 