# -*- coding: utf-8 -*-

from python.itemTypes.GenericItem import GenericItem


class Sulfuras(GenericItem):

    quality_limit = 80

    @staticmethod
    def update_quality(item):
        item.quality = Sulfuras.quality_limit

    @staticmethod
    def update_sell_in(item):
        pass
