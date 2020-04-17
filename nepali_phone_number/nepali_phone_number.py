from nepali_phone_number.config import config
from nepali_phone_number.datasets import nepali_english_digits
from nepali_phone_number.exceptions import InvalidEnglishNumberException, InvalidNepaliNumberException
from nepali_phone_number.validators import is_english_number, is_nepali_number

from nepali_phone_number.exceptions import InvalidNumberException
from nepali_phone_number.regexs import (
    ncell_phone_number_regex,
    ntc_phone_number_regex,
    sky_phone_number_regex,
    utl_phone_number_regex,
    hello_phone_number_regex,
    smart_cell_phone_number_regex,
    phone_number_regex
)


class NepaliPhoneNumber:
    """
    Class For Nepali Number
    """

    def __init__(self, nepali_number_input=None, english_number_input=None):

        if not nepali_number_input and not english_number_input:
            raise ValueError('At least one params required.')
        if nepali_number_input and english_number_input:
            raise ValueError('Only one param is allowed.')

        self._nepali_number = nepali_number_input
        self._english_number = english_number_input

        self._validate_inputs()

    def _validate_inputs(self):
        if self._english_number:
            if is_english_number(number=str(self._english_number)):
                self._english_number = str(self._english_number)
            else:
                raise InvalidEnglishNumberException()
        else:
            if is_nepali_number(number=str(self._nepali_number)):
                self._nepali_number = str(self._nepali_number)
            else:
                raise InvalidNepaliNumberException()

    def convert_to_nepali(self):
        if self._nepali_number:
            raise ValueError('With english_input_number, convert_to_nepali() can\'t be called.')

        converted_number = ''
        for n in self._english_number:
            for index in nepali_english_digits:
                if n.encode(encoding=config['encoding']) == index['english']:
                    converted_number += index['nepali'].decode(encoding=config['encoding'])
        return converted_number

    def convert_to_english(self):
        if self._english_number:
            raise ValueError('With english_input_number, convert_to_english() can\'t be called.')

        converted_number = ''
        for n in self._nepali_number:
            for index in nepali_english_digits:
                if n.encode(encoding=config['encoding']) == index['nepali']:
                    converted_number += index['english'].decode(encoding=config['encoding'])
        return converted_number

    def get_number_detail(self):
        if self._english_number:
            number = self._english_number
        else:
            number = self.convert_to_english()

        return NumberDetail(number=number).get_detail()

    def is_valid_number(self):
        if self._english_number:
            number = self._english_number
        else:
            number = self.convert_to_english()

        if phone_number_regex.match(number):
            return True
        return False
        
        
class NumberDetail:
    def __init__(self, number: str):
        self._number = number
    
    def get_detail(self):
        return {
            'number': self._number,
            'network_provider': self._get_network_provider()
        }

    def _get_network_provider(self):
        if ncell_phone_number_regex.match(self._number):
            return 'NCELL'
        elif ntc_phone_number_regex.match(self._number):
            return 'NTC'
        elif sky_phone_number_regex.match(self._number):
            return 'SKY'
        elif utl_phone_number_regex.match(self._number):
            return 'UTL'
        elif hello_phone_number_regex.match(self._number):
            return 'HELLO'
        elif smart_cell_phone_number_regex.match(self._number):
            return 'SMART CELL'
        else:
            raise InvalidNumberException('Invalid Phone Number.')
