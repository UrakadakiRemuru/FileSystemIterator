from typing import TypeVar, Any, Type

T = TypeVar('T')

def parseDelimited(data: Any, cls: Type[T]) -> tuple[Type[T], int]:
    """
    \brief Расшифровывает сообщение,
    предваренное длиной из массива байтов.
        
    \param data Массив данных.
    \param cls Тип сообщения.

    \return Возвращает кортеж из
    расшифрованного сообщения и количество байт,
    которое потребовалось для расшифровки.
    """
    pass
