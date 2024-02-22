
from .IConverter import * 
import re

class DecimalConverter(IConverter):
   
    def ToBinary(self,number) -> str:
        if(not self.IsValid(number)):
            return "No es un numero decimal valido"
        
        binaryNumber = " "
        number = int(number)

        while (number > 0):
            binaryNumber += str(number%2)
            number //= 2
        binaryNumber = "".join(reversed(binaryNumber))

        return binaryNumber

    def ToOctal(self,number) -> str:
        if(not self.IsValid(number)):
            return "No es un numero decimal valido"
        
        octalNumber = " "
        number = int(number)

        while(number > 0):
            octalNumber += str(number%8)
            number //= 8
        octalNumber = "".join(reversed(octalNumber))

        return octalNumber

    def ToDecimal(self,number) -> str:
        if (not self.IsValid(number)):
            return "No es un numero decimal valido"
        return number

    def ToHexadecimal(self,number) -> str:
        if(not self.IsValid(number)):
            return "No es un numero decimal valido"
        
        numbersHex = ['0','1','2','3','4','5','6','7','8','9','A','B','C','D','E','F']
        hexNumber = ""
        number = int(number)

        while(number > 0):
            hexNumber += numbersHex[number%16]
            number //= 16
        hexNumber = "".join(reversed(hexNumber))

        return hexNumber
    
    def IsValid(self,number) -> bool:
        pattern = r'^[0-9]+(\.[0-9]+)?$'
        result = re.match(pattern, number)
        return bool(result)