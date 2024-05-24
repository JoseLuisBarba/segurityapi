from enum import Enum

class TimeWindowStatus(Enum):
    SERVE: bool = True
    INVALID: bool = False



class TimeWindow:
    def __init__(self, a: float , b: float) -> None:
        """Crea una instancia de Time Window

        Args:
            a (float): Limite de tiempo inferior.
            b (float): Limite de tiempo superior.
        """
        self._a, self._b = a , b

    @property
    def a(self) -> float:
        """_summary_

        Returns:
            float: Limite de tiempo inferior
        """
        return self._a
    
    
    @property
    def b(self) -> float:
        """_summary_

        Returns:
            float: Limite de tiempo superior.
        """
        return self._b
    
    @a.setter
    def a(self, value: float)-> None:
        """_summary_

        Args:
            value (float): valor para limite de tiempo inferior.
        """
        self._a = value
    
    @b.setter
    def b(self, value: float) -> None:
        """_summary_

        Args:
            value (float): valor para limite de tiempo superior.
        """
        self._b = value



    def check_status(self, x: float) -> bool:
        """Verifica si un valor se encuentra dentro de la ventana de tiempo

        Args:
            x (float): valor de tiempo a compropar

        Returns:
            bool: True si es cierto sino False
        """
        if self.a <= x <= self.b:
            return TimeWindowStatus.SERVE
        return TimeWindowStatus.INVALID
    
    
    
    def to_json(self):
        return {
            'a': self.a,
            'b': self.b
        }
        