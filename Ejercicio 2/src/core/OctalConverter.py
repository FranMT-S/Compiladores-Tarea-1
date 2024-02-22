from .IConverter import * 
import re

class OctalConverter(IConverter):
   
    def ToBinary(self, number) -> str:
        if not self.IsValid(number):
            return "No es un número octal válido."
        
        binary_num = ""
        for digit in number:
            binary_num += format(int(digit), '03b')
        return binary_num

    def ToOctal(self, number) -> str:
        return number

    def ToDecimal(self, number) -> str:
        if not self.IsValid(number):
            return "No es un número octal válido."
        
        dec_num = 0
        for i in range(len(number)):
            dec_num += int(number[i]) * (8 ** (len(number) - 1 - i))
        return str(dec_num)

    def ToHexadecimal(self, number) -> str:
        if not self.IsValid(number):
            return "No es un número octal válido."
        
        dec_num = int(self.ToDecimal(number))
        hex_num = hex(dec_num)[2:]
        return hex_num

    def IsValid(self, number) -> bool:
        pattern = r'^[0-7]+$'
        result = re.match(pattern, number)
        return bool(result)