# Nepali Phone Number

Nepali Phone Number is a Python library for dealing with nepali phone numbers with both nepali and english inputs.

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install nepali-phone-number.

```bash
pip install nepali-phone-number
```

## Usage

```python
from nepali_phone_number import NepaliPhoneNumber

phone_number = NepaliPhoneNumber(nepali_number_input='९८४६५११९६२') # for nepali input

phone_number.convert_to_english()   # returns "9846511962"
phone_number.is_valid_number()      # returns "True" for valid number and "False" for invalid number
phone_number.get_number_detail()    # returns number detail eg. {'number': '9846511962', 'network_provider': 'NTC'}


phone_number = NepaliPhoneNumber(english_number_input='9846511962')    # for english input
phone_number.convert_to_nepali()    # returns "९८४६५११९६२"
```

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License
[MIT](https://choosealicense.com/licenses/mit/)