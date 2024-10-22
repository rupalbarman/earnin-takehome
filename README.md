# earnin-takehome
EarnIn's take home project

### Build
1. Pull
2. `docker compose up --build` (builds and spawns all services needed + create database)
3. `docker exec -it api bash` to enter shell
    1. `python manage.py migrate` to apply migrations (create tables)
4. Hit `localhost:8002/admin/` to access Admin Panel
