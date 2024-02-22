from src.core import *

BINARY = "binary"
OCTAL = "octal"
DECIMAL = "decimal"
HEXADECIMAL = "hexadecimal"

if __name__ == '__main__':
    
    converter = None
    # coloquen sus opciones para pruebas
    data = "5"
    InputType = "octal"
    OutputType = "hexadecimal"

    # Convertir texto a minuscula por si acaso
    InputType = InputType.lower()
    #OutputType = OutputType.lower()

    # Converter Factory Method
    GetConverter = dict([(BINARY, BinaryConverter),
                            (OCTAL, OctalConverter),
                            (DECIMAL, DecimalConverter),
                            (HEXADECIMAL,HexadecimalConverter)
                        ])

    # instanciar
    converter = GetConverter[InputType]()

    if(OutputType == BINARY):
        print(converter.ToBinary(data))
    elif(OutputType == OCTAL):
        print(converter.ToOctal(data))
    elif(OutputType == DECIMAL):
        print(converter.ToDecimal(data))
    elif(OutputType == HEXADECIMAL):
        print(converter.ToHexadecimal(data))
   
 