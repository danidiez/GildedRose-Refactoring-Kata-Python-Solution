# -*- coding: utf-8 -*-
from python.itemTypes.AgedBrie import AgedBrie
from python.itemTypes.BackstagePasses import BackstagePasses
from python.itemTypes.Conjured import Conjured
from python.itemTypes.GenericItem import GenericItem
from python.itemTypes.Sulfuras import Sulfuras


class GildedRose(object):

    def __init__(self, items):
        self.items = items
        self.item_types = {"Backstage passes": BackstagePasses,
                           "Sulfuras": Sulfuras,
                           "Aged Brie": AgedBrie,
                           "Conjured": Conjured}

    def update_quality(self):
        for item in self.items:
            item_type = self.get_item_type(item)
            item_type.update_sell_in(item)
            item_type.update_quality(item)

    def get_item_type(self, item):
        for item_type in self.item_types:
            if item.name.startswith(item_type):
                return self.item_types[item_type]
        return GenericItem


class Item:
    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)
