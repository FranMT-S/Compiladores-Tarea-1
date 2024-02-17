from .IConverter import * 
import re

class OctalConverter(IConverter):
   
    def ToBinary(self,number) -> str:
        return "octal a Binario"

    def ToOctal(self,number) -> str:
       return number

    def ToDecimal(self,number) -> str:
        return "octal a decimal"

    def ToHexadecimal(self,number) -> str:
        return "octal a hexadecimal"
    
    def IsValid(self,number) -> bool:
        pass