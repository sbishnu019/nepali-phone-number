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
