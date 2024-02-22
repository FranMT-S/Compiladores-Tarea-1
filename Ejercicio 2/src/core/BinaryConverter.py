
from .IConverter import * 
import re

class BinaryConverter(IConverter):
   


    def ToBinary(self,number) -> str:
        if(not self.IsValid(number)):
            return "no es valido"
        return number
    

    def ToOctal(self,number) -> str:
        while len(number) % 3 != 0:
            number = '0' + number  
        
        binary_group = [number[i:i+3] for i in range(0, len(number), 3)]

    
        octal = ''
        for group in binary_group:
            octal += str(int(group, 2))
        
        return octal
        

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
        
        while len(number) % 4 != 0:
            number = '0' + number  
        
        binary_groups = [number[i:i+4] for i in range(0, len(number), 4)]

        hexadecimal = ''
        for group in binary_groups:
            hexadecimal += format(int(group, 2), 'X') 
        
        return hexadecimal
    

    def IsValid(self,number) -> bool:
        pattern = r'^(0|1)+$'
        result = re.match(pattern,number)

        return bool(result)
