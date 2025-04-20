# Restaurant Reservation API

> API RESTful para gerenciar reservas de mesas em um restaurante, com autenticação JWT, controle de disponibilidade e administração de mesas.

---

## 🛠 Tecnologias

- Python 3.12  
- Django 5.2
- Django REST Framework  
- PostgreSQL
- Poetry  

---

## ⚙️ Status do Projeto

> Em construção

Estrutura inicial criada com as apps:

- **users**: autenticação e autorização  
- **tables**: gerenciamento de mesas  
- **reservations**: sistema de reservas  
- **utils**: validações e helpers  

Funcionalidades serão implementadas em etapas.

---

## 🚀 Como executar localmente

```bash
git clone https://github.com/seu-usuario/restaurant-reservation.git
cd restaurant-reservation
poetry install
cp .env.example .env   # configure suas variáveis de ambiente
python manage.py migrate
python manage.py runserver
```

## 📚 Roadmap

- [x] Estrutura inicial de pastas e apps  
- [ ] CRUD de usuários (registro, login)  
- [ ] CRUD de mesas  
- [ ] CRUD de reservas com validação de disponibilidade  
- [ ] Autenticação via JWT  
- [ ] Documentação Swagger / Redoc  
- [ ] Dockerização  

## 📝 Licença

MIT © Seu Nome
