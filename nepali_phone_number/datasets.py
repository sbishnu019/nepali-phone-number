english_digits_data = [
    {
        'digit': str(number),
        'unicode': '{}'.format(number).encode(encoding='UTF-8')
    } for number in range(0, 10)
]

english_digits = [digit.get('digit') for digit in english_digits_data]
english_encodes = [digit.get('unicode') for digit in english_digits_data]

nepali_digits_data = [
    {
        'digit': '०',
        'unicode': '०'.encode(encoding='UTF-8')
    },
    {
        'digit': '१',
        'unicode': '१'.encode(encoding='UTF-8')
    },
    {
        'digit': '२',
        'unicode': '२'.encode(encoding='UTF-8')
    },
    {
        'digit': '३',
        'unicode': '३'.encode(encoding='UTF-8')
    },
    {
        'digit': '४',
        'unicode': '४'.encode(encoding='UTF-8')
    },
    {
        'digit': '५',
        'unicode': '५'.encode(encoding='UTF-8')
    },
    {
        'digit': '६',
        'unicode': '६'.encode(encoding='UTF-8')
    },
    {
        'digit': '७',
        'unicode': '७'.encode(encoding='UTF-8')
    },
    {
        'digit': '८',
        'unicode': '८'.encode(encoding='UTF-8')
    },
    {
        'digit': '९',
        'unicode': '९'.encode(encoding='UTF-8')
    }
]

nepali_digits = [digit.get('digit') for digit in nepali_digits_data]
nepali_encodes = [digit.get('unicode') for digit in nepali_digits_data]

nepali_english_digits = [
    {
        'english': english_digits_data[index]['unicode'],
        'nepali': nepali_digits_data[index]['unicode']
    } for index in range(0, 10)
]


# LandLine Area Codes

land_line_data = {
        '097': 'Achham',
        '095': 'Baitadi',
        '081': 'Banke',
        '053': 'Bara',
        '084': 'Bardia',
        '083': 'Bheri',
        '029': 'Bhojpur',
        '056': 'Chitwan',
        '096': 'Dadeldhura',
        '089': 'Dailekh',
        '093': 'Darchula',
        '010': 'Dhading',
        '026': 'Dhankuta',
        '041': 'Dhanusha',
        '068': 'Dhawalagiri',
        '049': 'Dolkha',
        '094': 'Doti',
        '064': 'Gandaki',
        '079': 'Gulmi',
        '027': 'Ilam',
        '046': 'Janakpur',
        '087': 'Jumla',
        '091': 'Kailali',
        '076': 'Kapilvastu',
        '061': 'Kaski',
        '01': 'Kathmandu',
        '036': 'Khotang',
        '025': 'Koshi',
        '066': 'Lamjung',
        '077': 'Lumbini',
        '099': 'Mahakali',
        '044': 'Mahottari',
        '057': 'Makwanpur',
        '023': 'Mechi',
        '021': 'Morang',
        '069': 'Myagdi',
        '055': 'Narayani',
        '037': 'Okhaldhunga',
        '075': 'Palpa',
        '024': 'Panchthar',
        '067': 'Parbat',
        '051': 'Parsa',
        '086': 'Pyuthan',
        '082': 'Rapti',
        '071': 'Rupandehi',
        '033': 'Sagarmatha',
        '031': 'Saptari',
        '092': 'Seti',
        '047': 'Sindhuli',
        '038': 'Solukhumbu',
        '063': 'Syangia',
        '035': 'Udaypur',
    }

# Ncell Zone Data
ncell_data = [
    {
        'zone': 'Mechi',
        'prepaid': [
            '98140', '98150', '98170', '98240', '98249', '98049', '98079', '98060', '98149', '98159', '98169', '98179',
            '98160', '98259', '98269', '98279'
        ],
        'pro': ['98014']
    },
    {
        'zone': 'Koshi',
        'prepaid': [
            '98040', '98190', '98110', '98113', '98123', '98009', '98043', '98070', '98073', '98053',
            '98143', '98153', '98163', '98173', '98193', '98104', '98105', '98243', '98253', '98263'
        ],
        'pro': [
            '98027', '98207'
        ]
    },
    {
        'zone': 'Sagarmatha',
        'prepaid': [
            '98047', '98077', '98059', '98147', '98157', '98167', '98177',
            '98197', '98199', '98117', '98247', '98257', '98267'
        ],
        'pro': ['98015']
    },
    {
        'zone': 'Janakpur',
        'prepaid': [
            '98048', '98076', '98078', '98148', '98158', '98168', '98178', '98198', '98196',
            '98176', '98120', '98121', '98008', '98096', '98248', '98258', '98268'
        ],
        'pro': ['98016']
    },
    {
        'zone': 'Narayani',
        'prepaid': [
            '98042', '98068', '98071', '98072', '98142', '98152', '98162', '98172', '98192', '98111',
            '98112', '98118', '98122', '98091', '98092', '98211', '98212', '98218', '98242', '98252'
        ],
        'pro': [
            '98029', '98209'
        ]
    },
    {
        'zone': 'Bagmati',
        'prepaid': [
            '9803', '9808', '9813', '9818', '98100', '98101', '98102', '98103', '98230', '98231',
            '98232', '98233', '98234', '98235', '98236', '98237', '98238', '98239'
        ],
        'pro': [
            '98021', '98020', '98011', '98022', '98018', '98019', '98012', '98010', '98023', '98024'
        ]
    },
    {
        'zone': 'Gandaki',
        'prepaid': [
            '98166', '98241', '98251', '98261', '98041', '98065', '98066', '98067',
            '98058', '98141', '98151', '98161', '98171', '98191', '98271', '98291', '98266'
        ],
        'pro': ['98028']
    },
    {
        'zone': 'Lumbini',
        'prepaid': [
            '98129', '98007', '98214', '98215', '98219', '98044', '98069', '98074', '98075', '98054',
            '98144', '98154', '98164', '98174', '98194', '98175', '98114', '98115', '98119', '98244', '98254'
        ],
        'pro': ['98026']
    },
    {
        'zone': 'Dhaulagiri',
        'prepaid': [
            '98061', '98051', '98052', '98213'
        ],
        'pro': ['9801300']
    },
    {
        'zone': 'Rapti',
        'prepaid': [
            '98062', '98095', '98097', '98098', '98128', '98108', '98109', '98228', '98229'
        ],
        'pro': ['9801325']
    },
    {
        'zone': 'Karnali',
        'prepaid': [
            '98063', '98093'
        ],
        'pro': ['9801350']
    },
    {
        'zone': 'Bheri',
        'prepaid': [
            '98195', '98124', '98125', '98005', '98224', '98225', '98045',
            '98145', '98155', '98165', '98245', '98255', '98265'
        ],
        'pro': ['98025']
    },
    {
        'zone': 'Seti',
        'prepaid': [
            '98046', '98146', '98156', '98116', '98126', '98006', '98246', '98256', '98216', '98226'
        ],
        'pro': ['98017']
    },
    {
        'zone': 'Mahakali',
        'prepaid': [
            '98127', '98106', '98107', '9805740', '98064', '98094'
        ],
        'pro': ['9801375']
    },
]
