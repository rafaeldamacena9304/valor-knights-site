# 🎮 ValorKnights Demo Site (Flask)

> Este projeto é um site demonstrativo para um servidor Minecraft, construído como exercício prático para explorar o desenvolvimento web com Flask e integrações essenciais.

---

## 🔍 Descrição

O **ValorKnights Demo Site** apresenta uma interface visual inspirada no universo do Minecraft, permitindo ao visitante:

- Explorar produtos e kits especiais (Farms e Sets) disponíveis para compra.
- Iniciar o processo de aquisição de privilégios VIP via redirecionamento para gateways de pagamento.
- Receber confirmação de pagamento e, automaticamente, executar comandos RCON no servidor Minecraft para conceder o VIP.

Esta aplicação foi implementada de forma orientada durante um curso prático, consolidando conceitos-chave do desenvolvimento backend com Flask, mas não representa um sistema de produção completo.

---

## 🛠️ Tecnologias Utilizadas

- **Python 3.x**
- **Flask**: Microframework web para rotas e renderização de templates.
- **Flask-WTF** / **WTForms**: Validação e gerenciamento de formulários.
- **mcrcon**: Biblioteca para envio de comandos RCON ao servidor Minecraft.
- **subprocess**: Integração com o utilitário `screen` para comunicação com o servidor em execução.
- **Requests**: Consumo de webhooks de confirmação de pagamento.
- **Jinja2**: Templates HTML dinâmicos.

---

## 🚧 Segurança e Limitações

:warning: **Aviso de Demonstração**

- A `SECRET_KEY` está hardcoded no código apenas para fins de demonstração. **Não utilize** este valor em produção.
- Ausência de mecanismos avançados de autenticação, criptografia e proteção contra CSRF.
- O fluxo de pagamento e confirmação é simplificado e não deve ser adotado sem auditoria de segurança.

Este projeto serve para ilustrar padrões e integrações básicas, mas **não** substitui as melhores práticas de segurança.

---

## 🚀 Pré‑requisitos

Antes de executar, certifique-se de ter instalado:

- Python 3.6 ou superior
- **Ambiente virtual**: `python -m venv venv`
- Acesso ao servidor Minecraft configurado para RCON (porta e senha)

---

## ⚙️ Como Executar Localmente

1. **Clone o repositório**

   ```bash
   git clone https://github.com/seu-usuario/valor-knights-site.git
   cd valor-knights-site
   ```

2. **Criar e ativar ambiente virtual**

   ```bash
   python -m venv venv
   source venv/bin/activate  # No Windows: venv\Scripts\activate
   pip install -r requirements.txt
   ```

3. **Executar o aplicativo**

   ```bash
   python app.py
   ```

Acesse em `http://127.0.0.1:5000/`.

---

## 📦 Endpoints Principais

| Rota                     | Método | Descrição                                          |
| ------------------------ | ------ | -------------------------------------------------- |
| `/`                      | GET    | Página inicial                                     |
| `/vip`                   | GET    | Formulário de compra VIP                           |
| `/loja`                  | GET    | Exibe lista de produtos e kits                     |
| `/produto/<nome>`        | GET    | Detalha um produto ou kit específico               |
| `/purchase`              | POST   | Redireciona para gateway de pagamento (mensal/trimestral) |
| `/payment_confirmation`  | POST   | Webhook de confirmação, dispara comando RCON VIP   |

---

## 🤝 Contribuição

Sugestões de melhorias, correções de bugs ou aprimoramentos de segurança são bem-vindos:

1. Abra uma _issue_ descrevendo a proposta.
2. Faça um _fork_ e crie uma branch (`git checkout -b feature-nome`).
3. Envie um _pull request_.

---

##### Desenvolvido como demonstração prática para integração Flask e Minecraft RCON  
