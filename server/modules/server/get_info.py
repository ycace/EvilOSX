# -*- coding: utf-8 -*-
__author__ = "Marten4n6"
__license__ = "GPLv3"

from server.modules.helper import ModuleABC


class Module(ModuleABC):
    def get_info(self) -> dict:
        return {
            "Author:": ["Marten4n6"],
            "Description": "Return basic information about the bot.",
            "References": [],
            "Stoppable": False
        }
