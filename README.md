# earnin-takehome
EarnIn's take home project

### Build
1. Pull
2. `docker compose up --build` (builds and spawns all services needed + create database)
3. `docker exec -it api bash` to enter shell
    1. `python manage.py migrate` to apply migrations (create tables)
    2. Execute `metric.utils.create_initial_metrics` to pre-fill global list of metrics (can be done via python shell)
    3. Create a super user to use the admin panel using `python manage.py createsuperuser` in python shell
4. Hit `localhost:8002/admin/` to access Admin Panel (use superuser account)
5. Endpoints (can be tested through CURL or Postman)
    - POST `/user/create/` to create user
    - POST `/account/create` to create account associated to user
    - POST `/account/1/add-metrics` to add metrics to a given account
    - GET `/account/1/metric` to fetch registered metrics to this account.
      - Registered metrics can be filtered using `?metrics=1,2,3` query parameter
    - GET `/metric/all` to get global list of metrics supported
