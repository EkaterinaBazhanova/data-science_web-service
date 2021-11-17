python-flask-docker

Итоговый проект курса "Машинное обучение в бизнесе".

ML: sklearn, pandas, numpy.

API: flask .

Данные: с kaggle - https://www.kaggle.com/shwetabh123/mall-customers.

Задача: кластеризовать покупателей магазина по имеющимся данным (unsupervised learning).

Используемые признаки:
-- Genre (object), 
-- Age (int64), 
-- Annual Income (k$) (int64), 
-- Spending Score (1-100) (int64).

Преобразования признаков: binarisation.

Модель: KMeans.

Клонирование репозитория и создание образа:

1. Клонирование репозиория с github
git clone https://github.com/EkaterinaBazhanova/data-science_web-service.git

2. Вход с папку со скаченными файлами
cd data-science_web-service

3. Запуск docker-compose
docker compose up --build

Открытие в браузере:
-- титульная страница: http://0.0.0.0:5000/ или http://localhost:5000/ (для windows http://127.0.0.1:5000/)
-- страница с предсказаниями: http://0.0.0.0:5000/predict или http://localhost:5000/predict (для windows http://127.0.0.1:5000/predict)
P.S. На странице predict есть два формы получения предсказания модели: через ввод данных в форму или через загрузку датасета с данными.