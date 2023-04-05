#!/usr/bin/python3
"""Defines a locked class."""


class LockedClass:
    """
    Prevent the user from instantiating new LockedClass attributes from anything but attributes called 'first_name'.
    """

    __slots___ = ["first_name"]
