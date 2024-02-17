
from .IConverter import * 
import re

class HexadecimalConverter(IConverter):
   
    def ToBinary(self,number) -> str:
        return "hexadecimal a Binario"

    def ToOctal(self,number) -> str:
       return "hexadecimal a octal"

    def ToDecimal(self,number) -> str:
        return "hexadecimal a decimal"

    def ToHexadecimal(self,number) -> str:
        return number


    def IsValid(self,number) -> bool:
        pass