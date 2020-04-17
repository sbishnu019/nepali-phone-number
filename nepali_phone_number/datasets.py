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
