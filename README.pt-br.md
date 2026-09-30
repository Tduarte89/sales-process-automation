# 📊 Automação de Processos e Relatório de Vendas (RPA com Python)

🌍 **Idioma:** [English](README.md) | Português

![Python](https://img.shields.io/badge/Python-3.10%2B-blue?logo=python&logoColor=white)
![Pandas](https://img.shields.io/badge/Pandas-Data%20Analysis-150458?logo=pandas&logoColor=white)
![PyAutoGUI](https://img.shields.io/badge/RPA-PyAutoGUI-green)
![Status](https://img.shields.io/badge/Status-Concluído-brightgreen)

Projeto prático de **Robotic Process Automation (RPA)** e **Análise de Dados** desenvolvido em Python. O objetivo é automatizar a rotina operacional diária de coleta de dados de vendas, cálculo dos principais indicadores de desempenho (KPIs) e envio de relatório executivo por e-mail.

---

## 🎯 Cenário de Negócio

Em muitas operações comerciais, analistas precisam realizar tarefas manuais e repetitivas todos os dias:
1. Acessar o sistema de arquivos em nuvem (Google Drive);
2. Baixar a base atualizada de vendas do dia anterior;
3. Consolidar os números de faturamento e volume de itens vendidos;
4. Redigir e enviar um e-mail formal com o resumo para a diretoria.

Esse processo consome tempo e está sujeito a falhas operacionais. Esta automação executa o ciclo completo em poucos segundos, garantindo precisão e produtividade.

---

## 🛠️ Tecnologias e Bibliotecas

- **[Python](https://www.python.org/):** Linguagem base do projeto.
- **[Pandas](https://pandas.pydata.org/):** Manipulação, tratamento e cálculo dos indicadores da base de dados.
- **[OpenPyXL](https://openpyxl.readthedocs.io/):** Motor de leitura e integração de planilhas Excel (`.xlsx`).
- **[PyAutoGUI](https://pyautogui.readthedocs.io/):** Automação de interface gráfica (RPA) para controle de mouse e teclado.
- **[Pyperclip](https://pypi.org/project/pyperclip/):** Tratamento de caracteres especiais e acentuação no envio de textos via clipboard.
- **[python-dotenv](https://github.com/theskumar/python-dotenv):** Gerenciamento seguro de variáveis de ambiente e proteção de dados confidenciais.

---

## 📁 Estrutura do Repositório

```text
sales-process-automation/
│
├── data/
│   └── Vendas - Dez.xlsx      # Base de dados de exemplo com histórico de vendas
│
├── First Automation.ipynb     # Notebook Jupyter com a exploração interativa passo a passo
├── sales_automation.py        # Script Python modularizado e pronto para produção
├── requirements.txt           # Dependências do projeto
├── .env.example               # Modelo para variáveis de ambiente e segurança
├── .gitignore                 # Arquivos e diretórios ignorados pelo Git
├── README.md                  # Documentação principal em Inglês
└── README.pt-br.md            # Documentação em Português
```

---

## ⚙️ Como Executar o Projeto

### Pré-requisitos
- Python 3.10 ou superior instalado.
- Google Chrome instalado.

### 1. Clonar o repositório
```bash
git clone https://github.com/SEU-USUARIO/sales-process-automation.git
cd sales-process-automation
```

### 2. Criar e ativar o ambiente virtual (Recomendado)
```bash
# Windows
python -m venv venv
venv\Scripts\activate
```

### 3. Instalar as dependências
```bash
pip install -r requirements.txt
```

### 4. Configurar as Variáveis de Ambiente (Protocolo de Segurança)
Copie o arquivo `.env.example` para criar o seu `.env` privado:
```bash
copy .env.example .env
```
Abra o `.env` e defina o e-mail de destino, o link do Drive e o nome do remetente. *(O arquivo `.env` real está no `.gitignore` e nunca será enviado para o GitHub).*

### 5. Executar a automação
```bash
python sales_automation.py
```

---

## 🔍 Métricas Consolidadas pelo Script

Ao processar a base de vendas, o script extrai automaticamente os totais:
- **Faturamento Total:** Soma da coluna `Valor Final` (ex: `R$ 2.917.311,00`).
- **Quantidade de Produtos:** Soma da coluna `Quantidade` (ex: `15.227 itens`).

---

## 💡 Notas Técnicas e Boas Práticas

> [!IMPORTANT]
> **Protocolo de Segurança (Twelve-Factor App):**  
> E-mails reais, links de sistemas internos e caminhos de pastas locais foram totalmente desacoplados do código-fonte através de variáveis de ambiente (`.env`). O arquivo `.env` é explicitamente bloqueado no `.gitignore`, evitando o vazamento acidental de dados pessoais e corporativos em repositórios públicos.

> [!NOTE]
> **Calibração de Coordenadas:**  
> Por utilizar a biblioteca `pyautogui` para interação com a interface gráfica, as coordenadas `(x, y)` dos cliques dependem da resolução da tela e da posição da janela do navegador. Caso execute em um monitor diferente, você pode utilizar a função utilitária `calibrate_coordinates()` presente no script para calibrar os pontos de clique.

> [!TIP]
> **Evoluções Futuras:**  
> - Substituir a automação de interface do e-mail por biblioteca de envio direto (SMTP nativo ou APIs como SendGrid/Gmail);
> - Utilizar a API do Google Drive para download headless sem necessidade de cliques na tela;
> - Agendar a execução automática diária utilizando o Agendador de Tarefas do Windows (Task Scheduler) ou Cron.

---

## 👤 Autor

Desenvolvido por **Thiago A. Duarte**.  
- LinkedIn: https://www.linkedin.com/in/thiago-duarte-32a64839 
- GitHub: https://github.com/Tduarte89
