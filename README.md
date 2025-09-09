# MotorHero - Sistema de Consulta e Orçamento de Óleo Automotivo

## Sobre o Projeto
MotorHero é uma aplicação web fullstack para **consulta de veículos por placa** e **geração de orçamentos de óleo**, integrando dados de API externa da Valvoline.  
O sistema calcula automaticamente a quantidade de frascos necessária, exibe informações step-by-step e mantém um dashboard com métricas de consultas.

---

## Tecnologias Utilizadas
**Backend:**
- Python 3.10+
- FastAPI 0.104+
- PostgreSQL/SQLite
- Cache em memória com TTL de 2 horas

**Frontend:**
- React 18 + Vite
- Tailwind CSS
- Framer Motion (animações)
- Dark Mode

**Integração:**
- API externa: Valvoline Oil API

---

## Decisões Técnicas

### Cálculo de Frascos
Implementei o cálculo seguindo a lógica:
1. Conversão de litros para ML (4.0L → 4000ml)
2. Extração do tamanho do frasco do retorno da API
3. Divisão com arredondamento para cima (ceil)
4. Cálculo de sobra em ML e percentual

### Cache
Implementei cache em memória com TTL de 2 horas para:
- Economizar chamadas à API
- Melhorar tempo de resposta
- Reduzir custos

### Tratamento de Placas
Normalização remove caracteres especiais e valida:
- Formato antigo: ABC1234
- Formato Mercosul: ABC1D23

## Screenshots

<p align="center">
  <img src="https://github.com/user-attachments/assets/5c6d2610-4daa-412c-9c73-cb74a5f7f65f" width="500" />
  <img src="https://github.com/user-attachments/assets/e9ef6b2e-64a8-4748-b329-177841a05e70" width="500" />
</p>

<p align="center">
  <img src="https://github.com/user-attachments/assets/11e9bf98-3272-43d6-a9a7-b3fe2aa5ae64" width="250" />
  <img src="https://github.com/user-attachments/assets/4eb0b501-1348-4039-92b0-d87c06e9a359" width="250" />
</p>
<p align="center">
  <img src="https://github.com/user-attachments/assets/12ed9823-ebf9-48b5-ab51-8e97c2cd24dc" width="500" />
  </p>


## Funcionalidades
- ✅ Consulta de veículo por placa com **normalização e validação**
- ✅ Integração com API externa de óleo
- ✅ Cálculo automático de frascos e sobra em ML/percentual
- ✅ Dashboard com analytics de consultas (diárias, semanais, top marcas e óleo mais usado)
- ✅ Visualização step-by-step do cálculo
- ✅ Geração de orçamento detalhado
- ✅ Cache de consultas em memória
- ✅ Dark mode
- ⚡ Responsividade completa e animações

---

## Como Rodar

### Git Clone
```bash
git clone https://github.com/CesarDanilo/motorhero-challenge.git
```

### Backend
```bash
cd motorhero-challenge\backend
python -m venv venv
venv\Scripts\activate 
pip install -r requirements.txt
uvicorn app.main:app --reload
```

### Frontend
```bash
cd frontend
npm install
npm run dev
```

### Usando Docker

Se você quiser rodar via Docker, siga os passos:

1. Build da imagem
```bash
docker build -t motorhero-backend ./backend
docker build -t motorhero-frontend ./frontend
```

2. Rodar o container
```bash
docker run -p 8000:8000 motorhero-backend
docker run -p 5173:5173 motorhero-frontend
```

