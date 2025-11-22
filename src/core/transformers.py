# ==============================================================================
# src/core/transformers.py
# Contiene la lógica para la composición de funciones (Semana 2).
# ==============================================================================


from typing import Callable, List, Any
from functools import reduce, partial


# --- Funciones de Composición (Paso 2.3) ---

def compose(*functions: Callable) -> Callable:
    """
    (Paso 2.3)
    Compone múltiples funciones de derecha a izquierda.
    Es decir, compose(f, g, h)(x) = f(g(h(x))).
    """
    # Usa reduce para encadenar las funciones.
    return reduce(lambda f, g: lambda x: f(g(x)), functions, lambda x: x)
  

def pipe(*functions: Callable) -> Callable:
    """
    (Paso 2.3)
    Compone múltiples funciones de izquierda a derecha (más intuitivo).
    Es decir, pipe(f, g, h)(x) = h(g(f(x))).
    """
    return reduce(lambda f, g: lambda x: g(f(x)), functions, lambda x: x)
  

# --- Clase de Pipeline (Paso 2.3) ---

class TimeSeriesPipeline:
    """
    (Paso 2.3)
    Esta clase permite construir un pipeline funcional para encadenar
    transformaciones de manera ordenada.
    Mantiene la inmutabilidad (no modifica los datos originales).
    """
    
    def __init__(self, data: List[float]):
        # Guarda una copia de los datos originales.
        self._data = data
        # Mantiene una lista de las funciones que se van a aplicar.
        self._transformations = []
     
    def add_transformation(self, func: Callable, *args, **kwargs) -> 'TimeSeriesPipeline':
        """
        Añade una nueva función (transformación) al pipeline.
        
        Usa 'partial' para guardar la función junto con sus argumentos
        (ej. 'normalize' con 'method=zscore').
        """
        # 'partial' nos permite "pre-configurar" una función.
        partial_func = partial(func, *args, **kwargs) if args or kwargs else func
        
        # Se crea una nueva instancia del pipeline (inmutabilidad).
        new_pipeline = TimeSeriesPipeline(self._data)
        
        # Se añade la nueva función a la lista de transformaciones.
        new_pipeline._transformations = self._transformations + [partial_func]
        return new_pipeline
     
    def execute(self) -> Any:
        """
        Ejecuta todas las transformaciones en orden (usando 'pipe')
        sobre los datos originales.
        """
        # Compone todas las funciones guardadas en una sola gran función.
        composed_function = pipe(*self._transformations)
        # Ejecuta la función compuesta sobre los datos.
        return composed_function(self._data)
     
    def get_data(self) -> List[float]:
        """Retorna una copia de los datos originales."""
        return self._data.copy()
