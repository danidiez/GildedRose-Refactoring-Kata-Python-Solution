# -*- coding: utf-8 -*-


class GenericItem:

    quality_limit = 50

    @staticmethod
    def update_quality(item):  # Generic function to update the quality of an Item (can be override)
        if item.sell_in < 0:
            GenericItem.decrease_quality(item, 2)
        else:
            GenericItem.decrease_quality(item, 1)

    @staticmethod
    def update_sell_in(item):  # Generic function to update the SellIn of an Item (can be override)
        item.sell_in -= 1

    @staticmethod
    def decrease_quality(item, decrease_value):   # Generic function to decrease the value of quality
        if (item.quality - decrease_value) >= 0:
            item.quality -= decrease_value
        else:
            item.quality = 0

    @staticmethod
    def increase_quality(item, increase_value):   # Generic function to increase the value of quality
        if (item.quality + increase_value) <= GenericItem.quality_limit:
            item.quality += increase_value
        elif item.quality < GenericItem.quality_limit:
            item.quality = GenericItem.quality_limit
