class Data:
    valid_login = 'Maksim2021'
    valid_password = 'qwerty'
    valid_firstname = 'Maks'
    valid_courier_data = {'login': 'Maksim2021', 'password': 'qwerty', 'firstName': 'Maks'}
    courier_data_without_name = {'login': 'Maksim2021', 'password': '9876'}
    courier_data_with_wrong_password = {'login': 'Maksim2021', 'password': '987654'}


class OrderData:
    order_data_grey_1 = {
        'firstName': 'Макс',
        'lastName': 'Пейн',
        'address': 'Ботаническая, 11',
        'metroStation': 5,
        'phone': '+79998887766',
        'rentTime': 3,
        'deliveryDate': '2026-10-29',
        'comment': 'За 1 час связаться по телефону',
        'color': [
            'Grey'
        ]
    }

    order_data_black_2 = {
        'firstName': 'Аполлон',
        'lastName': 'Бельведерский',
        'address': 'Южный бульвар, 5',
        'metroStation': 8,
        'phone': '+79268882211',
        'rentTime': 6,
        'deliveryDate': '2026-10-30',
        'comment': 'Оставить у двери',
        'color': [
            'Black'
        ]
    }

    order_data_two_colors_3 = {
        'firstName': 'Венера',
        'lastName': 'Милосская',
        'address': 'Паркоая, 2',
        'metroStation': 11,
        'phone': '+79857774455',
        'rentTime': 1,
        'deliveryDate': '2026-10-31',
        'comment': 'Жду.',
        'color': [
            'Black', 'Grey'
        ]
    }

    order_data_no_colors_4 = {
        'firstName': 'Кощей',
        'lastName': 'Бессмертный',
        'address': 'Замок Кощея, 3',
        'metroStation': 18,
        'phone': '+79095551122',
        'rentTime': 2,
        'deliveryDate': '2026-10-28',
        'comment': 'Созвон за 2 часа',
        'color': []
    }
