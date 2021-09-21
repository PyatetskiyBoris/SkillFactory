Учебный проект о вкусной и здоровой пище.

Исследование датасета Tripadvisor с ресторанами.

Цель - подготовить датасет к обучению модели, предсказывающей рейтинг ресторана, для избежания накрутки рейтинга ресторанами

Первоначальная версия датасета состоит из десяти столбцов, содержащих следующую информацию:

Restaurant_id — идентификационный номер ресторана / сети ресторанов;
City — город, в котором находится ресторан;
Cuisine Style — кухня или кухни, к которым можно отнести блюда, предлагаемые в ресторане;
Ranking — место, которое занимает данный ресторан среди всех ресторанов своего города;
Rating — рейтинг ресторана по данным TripAdvisor (именно это значение должна будет предсказывать модель);
Price Range — диапазон цен в ресторане;
Number of Reviews — количество отзывов о ресторане;
Reviews — данные о двух отзывах, которые отображаются на сайте ресторана;
URL_TA — URL страницы ресторана на TripAdvisor;
ID_TA — идентификатор ресторана в базе данных TripAdvisor.