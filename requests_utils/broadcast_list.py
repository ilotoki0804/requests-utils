from __future__ import annotations

import functools
from abc import abstractmethod, ABCMeta
from typing import (
    Any,
    Self,
    TypeVar,
    # Generic,
    SupportsIndex,
    overload,
)

from bs4.element import Tag

T = TypeVar('T')

#########################
# LEGACY BROADCAST LIST #
#########################


class AbstractBroadcastList(list[T], metaclass=ABCMeta):
    @abstractmethod
    def _callable_attr_broadcast(self, *args, __attr_name: str | None = None, **kwargs) -> Any:
        ...

    @abstractmethod
    def _attr_broadcast(self, attr_name: str) -> Any:
        ...

    def __getattr__(self, __name: str):
        if __name.startswith('E'):
            __name = __name.removeprefix('E')

        if not self.value:
            return self.value

        # every element contained in list are assumed to be share same type.
        if callable(getattr(self[0], __name)):
            return functools.partial(self._callable_attr_broadcast, __attr_name=__name)
        else:
            return self._attr_broadcast(__name)


class NonchainingBroadcastList(AbstractBroadcastList[T]):
    def _callable_attr_broadcast(self, *args, __attr_name: str | None = None, **kwargs):
        if __attr_name is None:
            raise ValueError('__attr_name is empty. This function not intended to use outside of class.')
        return [getattr(i, __attr_name)(*args, **kwargs) for i in self]

    def _attr_broadcast(self, attr_name: str):
        return [getattr(i, attr_name) for i in self]

    @overload
    def __getitem__(self, __item: SupportsIndex) -> T:
        ...

    @overload
    def __getitem__(self, __item: slice) -> list[T]:
        ...

    @overload
    def __getitem__(self, __item) -> list:
        ...

    def __getitem__(self, __item) -> T | list[T] | list:
        """받은 값이 string인 경우 broadcasting하지만, 아니라면 리스트의 방법에 따릅니다.
        예를 들어 `thislist[0]`이나 `thislist[:4]`는 리스트의 메소드이지만,
        `thislist['src']`는 브로드캐스트됩니다."""
        if isinstance(__item, (SupportsIndex, slice)):
            return super().__getitem__(__item)

        return getattr(self, 'E__getitem__')(__item)


class ChainingBroadcastList(AbstractBroadcastList[T]):
    def _callable_attr_broadcast(self, *args, __attr_name: str | None = None, **kwargs):
        if __attr_name is None:
            raise ValueError('__attr_name is empty. This function not intended to use outside of class.')
        return ChainingBroadcastList([getattr(i, __attr_name)(*args, **kwargs) for i in self])

    def _attr_broadcast(self, attr_name: str):
        return ChainingBroadcastList([getattr(i, attr_name) for i in self])

    @overload
    def __getitem__(self, __item: SupportsIndex) -> T:
        ...

    @overload
    def __getitem__(self, __item: slice) -> Self:
        ...

    @overload
    def __getitem__(self, __item) -> ChainingBroadcastList:
        ...

    def __getitem__(self, __item) -> T | Self | ChainingBroadcastList:
        """받은 값이 string인 경우 broadcasting하지만, 아니라면 리스트의 방법에 따릅니다.
        예를 들어 `thislist[0]`이나 `thislist[:4]`는 리스트의 메소드이지만,
        `thislist['src']`는 브로드캐스트됩니다."""
        if isinstance(__item, SupportsIndex):
            return super().__getitem__(__item)
        if isinstance(__item, slice):
            return ChainingBroadcastList(super().__getitem__(__item))

        return getattr(self, 'E__getitem__')(__item)


class TagBroadcastList(ChainingBroadcastList[Tag]):
    """Chaining Broadcast list especially for Tags."""
