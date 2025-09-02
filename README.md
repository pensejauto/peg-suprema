# PEG SUPREMA 8x1 — Deploy Ready

## Como rodar localmente
```bash
pip install -r requirements.txt
python app.py
# acesse http://127.0.0.1:5000
```

## Como rodar no Render
1. Suba esta pasta no GitHub.
2. Crie um Web Service no Render.
   - Build Command: `pip install -r requirements.txt`
   - Start Command: `gunicorn app:app`
3. Após o deploy, acesse a URL pública.

## Estrutura
- app.py → servidor Flask
- requirements.txt → dependências
- Procfile → instrução Gunicorn
- templates/ → HTML do painel e da PEGSTORE
- products.json → catálogo inicial de produtos