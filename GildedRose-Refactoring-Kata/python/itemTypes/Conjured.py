# -*- coding: utf-8 -*-

from python.itemTypes.GenericItem import GenericItem


class Conjured(GenericItem):

    @staticmethod
    def update_quality(item):
        if item.sell_in < 0:
            GenericItem.decrease_quality(item, 4)
        else:
            GenericItem.decrease_quality(item, 2)
