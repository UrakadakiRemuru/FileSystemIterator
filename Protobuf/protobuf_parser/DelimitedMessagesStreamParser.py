from protobuf_parser.helpers import parseDelimited

from typing import TypeVar, Type

T = TypeVar('T')

class DelimitedMessagesStreamParser:
    def __init__(self, cls: Type[T]) -> None:
        pass

    def parse(self, data: bytes) -> list[Type[T]]:
        pass
