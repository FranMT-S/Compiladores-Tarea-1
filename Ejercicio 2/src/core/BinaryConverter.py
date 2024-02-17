
from .IConverter import * 
import re

class BinaryConverter(IConverter):
   


    def ToBinary(self,number) -> str:
        if(not self.IsValid(number)):
            return "no es valido"
        
        return number

    def ToOctal(self,number) -> str:
        if(not self.IsValid(number)):
            return "no es valido"
        
        return "Binario a octal"

    def ToDecimal(self,number) -> str:
        if(not self.IsValid(number)):
            return "no es valido"
        
        return "Binario a decimal"

    def ToHexadecimal(self,number) -> str:
        if(not self.IsValid(number)):
            return "no es valido"

        return "Binario a hexadecial"
    
    def IsValid(self,number) -> bool:
        pattern = r'^(0|1)+$'
        result = re.match(pattern,number)

        return bool(result)
