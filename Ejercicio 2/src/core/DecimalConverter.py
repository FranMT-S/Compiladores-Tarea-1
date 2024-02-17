
from .IConverter import * 
import re

class DecimalConverter(IConverter):
   
    def ToBinary(self,number) -> str:
        return "decimal a Binario"

    def ToOctal(self,number) -> str:
       return "decimal a octal"

    def ToDecimal(self,number) -> str:
        return number

    def ToHexadecimal(self,number) -> str:
        return "decimal a hexadecimal"
    
    def IsValid(self,number) -> bool:
        pass