from .IConverter import *
import re

class HexadecimalConverter(IConverter):
   
    def ToBinary(self, number) -> str:
        if(not self.IsValid(number)):
            return "No es un número hexadecimal válido."
        
        decimal_number = int(number, 16)
        binary_number = bin(decimal_number)[2:]  
        return binary_number

    def ToOctal(self, number) -> str:
        if(not self.IsValid(number)):
            return "No es un número hexadecimal válido."
        
        decimal_number = int(number, 16)
        octal_number = oct(decimal_number)[2:] 
        return octal_number

    def ToDecimal(self, number) -> str:
        if(not self.IsValid(number)):
            return "No es un número hexadecimal válido."
        
        decimal_number = int(number, 16)
        return str(decimal_number)

    def ToHexadecimal(self, number) -> str:
        return number

    def IsValid(self, number) -> bool:
        return bool(re.fullmatch(r'[0-9A-Fa-f]+', number))