class OperationResult:
    def __init__(self, is_success: bool, message: str = "", data=None):
        """
        Clase que encapsula el resultado de una operación.
        
        :param is_success: Define si la operación fue exitosa.
        :param message: Mensaje opcional sobre el resultado.
        :param data: Resultado opcional de la operación.
        """
        self.is_success = is_success
        self.message = message
        self.data = data

    @classmethod
    def success(cls, data=None, message: str = "Operation completed successfully"):
        """
        Método de fábrica para resultados exitosos.
        
        :param data: Datos resultantes de la operación (opcional).
        :param message: Mensaje de éxito (por defecto "Operation completed successfully").
        :return: Instancia de OperationResult representando éxito.
        """
        return cls(is_success=True, message=message, data=data)

    @classmethod
    def failure(cls, message: str = "Operation failed"):
        """
        Método de fábrica para resultados fallidos.
        
        :param message: Mensaje de fallo.
        :return: Instancia de OperationResult representando fallo.
        """
        return cls(is_success=False, message=message)

    def __repr__(self):
        """
        Representación legible de la clase.
        """
        return f"<OperationResult(success={self.is_success}, message='{self.message}', data={self.data})>"
