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
### BACKEND
- cd backend
- pip install -r requirements.txt
- uvicorn app.main:app --reload

### FRONTEND
- cd frontend
- npm install
- npm run dev


