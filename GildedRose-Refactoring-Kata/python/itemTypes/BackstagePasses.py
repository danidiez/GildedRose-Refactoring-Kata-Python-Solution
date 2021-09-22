# -*- coding: utf-8 -*-

from python.itemTypes.GenericItem import GenericItem


class BackstagePasses(GenericItem):

    @staticmethod
    def update_quality(item):
        if item.sell_in < 0:
            item.quality = 0
        elif item.sell_in <= 5:
            BackstagePasses.increase_quality(item, 3)
        elif item.sell_in <= 10:
            BackstagePasses.increase_quality(item, 2)
        else:
            BackstagePasses.increase_quality(item, 1)
