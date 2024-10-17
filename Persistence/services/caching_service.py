import time

class CachingService:
    def __init__(self, expiration_time=300):
        """
        Inicializa el servicio de caché.
        :param expiration_time: Tiempo en segundos para la expiración de los datos cacheados.
        """
        self.cache = {}
        self.expiration_time = expiration_time

    def get(self, key):
        """
        Devuelve un valor cacheado si está disponible y no ha expirado.
        """
        if key in self.cache:
            value, timestamp = self.cache[key]
            if time.time() - timestamp < self.expiration_time:
                return value
            else:
                del self.cache[key]
        return None

    def set(self, key, value):
        """
        Guarda un valor en el caché con una marca de tiempo.
        """
        self.cache[key] = (value, time.time())

    def invalidate(self, key):
        """
        Invalida una entrada en el caché.
        """
        if key in self.cache:
            del self.cache[key]

    def clear(self):
        """
        Limpia todas las entradas en el caché.
        """
        self.cache.clear()
