
from abc import ABC, abstractmethod
class IConverter (ABC):
   
    @abstractmethod
    def ToBinary(self,number) -> str:
        pass

    @abstractmethod
    def ToOctal(self,number) -> str:
        pass

    @abstractmethod
    def ToDecimal(self,number) -> str:
        pass

    @abstractmethod
    def ToHexadecimal(self,number) -> str:
        pass

    # @abstractmethod
    def IsValid(self,number) -> bool:
        pass