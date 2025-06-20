🛒 E-commerce com Microsserviços
Este projeto é um sistema de e-commerce simples baseado em arquitetura de microsserviços, com os seguintes serviços:

Auth Service – autenticação de usuários (JWT)

Product Service – gerenciamento de produtos

Cart Service – carrinho de compras

Order Service – processamento de pedidos

API Gateway – roteador central e middleware de autenticação

Frontend React – interface do usuário


📁 Estrutura do Projeto
.
├── auth-service/
├── product-service/
├── cart-service/
├── order-service/
├── api-gateway/
├── frontend/
├── docker-compose.yml
└── README.md


🚀 Pré-requisitos
Docker

Docker Compose

(Opcional) Node.js e Python localmente, caso deseje rodar sem Docker


🧪 Passo a Passo para Executar
1. Clone o repositório
git clone https://github.com/seu-usuario/seu-repositorio.git
cd seu-repositorio

2. Configure as variáveis de ambiente
Crie arquivos .env nos serviços conforme necessário. Exemplo para auth-service:
# auth-service/.env
JWT_SECRET=segredo_super_secreto
DATABASE_URL=sqlite:///./users.db
JWT_SECRET=segredo_super_secreto
DATABASE_URL=sqlite:///./users.db

3. Suba os microsserviços com Docker
docker-compose up --build
Isso irá subir todos os serviços nas seguintes portas:
| Serviço         | Porta  |
| --------------- | ------ |
| API Gateway     | `8000` |
| Frontend React  | `3000` |
| Auth Service    | `8001` |
| Product Service | `8002` |
| Cart Service    | `8003` |
| Order Service   | `8004` |

4. Acesse a aplicação
Frontend: http://localhost:3000

API Gateway: http://localhost:8000

5. Cadastro e Login
Acesse /register para criar um novo usuário

Depois de registrar, vá para /login

Após login, você será redirecionado para a tela de produtos

✅ Funcionalidades
 Registro e login com JWT

 Listagem de produtos

 Adição e remoção de itens do carrinho

 Finalização de pedidos

 Histórico de compras

 API Gateway com autenticação centralizada

📦 Tecnologias utilizadas
Backend: FastAPI, SQLAlchemy, SQLite, JWT

Frontend: React, Axios, React Router

API Gateway: FastAPI + HTTPX

Comunicação: REST

Autenticação: JWT

Ambiente: Docker + Docker Compose

👨‍💻 Desenvolvimento e Contribuição
Utilize o GitHub Projects para acompanhar as tarefas

Utilize pull requests para colaborar

Código limpo e com boas práticas de microsserviços

Seguindo o fluxo Scrum

🧹 Comandos úteis

Subir e derrubar os containers
docker-compose up --build     # sobe tudo
docker-compose down           # derruba tudo
Acessar logs de um serviço

docker-compose logs -f auth-service
Instalar dependências localmente (opcional)

# Para React
cd frontend
npm install

# Para um serviço Python
cd auth-service
pip install -r requirements.txt

📌 Licença
Este projeto é apenas para fins educacionais.
