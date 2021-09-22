# -*- coding: utf-8 -*-

from python.itemTypes.GenericItem import GenericItem


class AgedBrie(GenericItem):

    @staticmethod
    def update_quality(item):
        AgedBrie.increase_quality(item, 1)
