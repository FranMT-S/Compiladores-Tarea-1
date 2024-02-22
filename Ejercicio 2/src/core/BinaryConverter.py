
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
        
        oct_num = ""
        for i in range(len(number) // 3):
            triad = number[3*i:3*(i+1)]
            oct_num += str(int(triad, 2))
        return oct_num
        

    def ToDecimal(self,number) -> str:
        if(not self.IsValid(number)):
            return "no es valido"
        
        dec_num = 0
        for i in range(len(number)):
            dec_num += int(number[i]) * (2 ** (len(number) - 1 - i))
        return dec_num
        

    def ToHexadecimal(self,number) -> str:
        if(not self.IsValid(number)):
            return "no es valido"
        
        hex_num = ""
        for i in range(len(number) // 4):
            nibble = number[4*i:4*(i+1)]
            hex_num += str(int(nibble, 2))
        return hex_num
    

    def IsValid(self,number) -> bool:
        pattern = r'^(0|1)+$'
        result = re.match(pattern,number)

        return bool(result)
