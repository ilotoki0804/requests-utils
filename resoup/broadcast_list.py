from __future__ import annotations

import functools
from abc import abstractmethod, ABCMeta
from typing import (
    Any,
    Self,
    TypeVar,
    Generic,
    SupportsIndex,
    overload,
    Callable,
)

from bs4.element import Tag

from .full_dunder import FullDunder

T = TypeVar('T')
T_co = TypeVar('T_co', covariant=True)


class BroadcastList(list[T]):
    @property
    def bc(self) -> _BroadcastedList[T]:
        return _BroadcastedList(self)


class _BroadcastedList(FullDunder, Generic[T_co]):
    def _callable_attr_broadcast(self, *args, **kwargs) -> BroadcastList:
        __attr_name = kwargs.pop("__attr_name")
        return BroadcastList(getattr(i, __attr_name)(*args, **kwargs) for i in self._broadcastlist_value)

    def __init__(self, broadcastlist: BroadcastList[T_co]) -> None:
        self._broadcastlist_value = broadcastlist

    def __getattr__(self, __name: str) -> Callable[..., BroadcastList] | BroadcastList:
        if not self._broadcastlist_value:
            return self._broadcastlist_value

        if callable(getattr(self._broadcastlist_value[0], __name)):
            return functools.partial(self._callable_attr_broadcast, __attr_name=__name)

        return BroadcastList(getattr(i, __name) for i in self._broadcastlist_value)

    def _callable_dunder_getattr(self, __name: str, *args, **kwargs) -> Any:
        # print(__name, args, kwargs)
        return self.__getattr__(__name)(*args, **kwargs)  # type: ignore

    async def _callable_dunder_getattr_async(self, __name: str, *args, **kwargs) -> Any:
        return await self.__getattr__(__name)(*args, **kwargs)  # type: ignore

    def __setattr__(self, name: str, value) -> None:
        if name == "_broadcastlist_value":
            return object.__setattr__(self, name, value)
        super().__setattr__(value)

    def __str__(self) -> str:
        """혼란을 막기 위해 __repr__와 __str__은 broadcast 대상에서 제합니다."""
        return list.__str__(self._broadcastlist_value)

    __repr__ = __str__  # type: ignore


class TagBroadcastList(BroadcastList[Tag]):
    @property
    def bc(self) -> _TagBroadcastedList:
        return _TagBroadcastedList(self)  # type: ignore


class _TagBroadcastedList(_BroadcastedList[Tag]):
    """Chaining BroadcastED list especially for Tags."""
