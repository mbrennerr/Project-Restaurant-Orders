

class InventoryControl:
    INGREDIENTS = {
        'hamburguer': ['pao', 'carne', 'queijo'],
        'pizza': ['massa', 'queijo', 'molho'],
        'misto-quente': ['pao', 'queijo', 'presunto'],
        'coxinha': ['massa', 'frango'],
    }
    MINIMUM_INVENTORY = {
        'pao': 50,
        'carne': 50,
        'queijo': 100,
        'molho': 50,
        'presunto': 50,
        'massa': 50,
        'frango': 50,
    }

    def __init__(self):
        self._orders = []
        self._need_to_buy = {
            'pao': 0,
            'carne': 0,
            'queijo': 0,
            'molho': 0,
            'presunto': 0,
            'massa': 0,
            'frango': 0,
        }
        self.lanches = ['hamburguer', 'pizza', 'misto-quente', 'coxinha']
        self.out_of_stock = set()

    def add_new_order(self, customer, order, day):
        self._orders.append((customer, order, day))
        ingredient_is_not_avaliable = set(
            self.INGREDIENTS).intersection(self.out_of_stock)
        if len(ingredient_is_not_avaliable) > 0:
            return False
        for ingredient in self.INGREDIENTS[order]:
            self ._need_to_buy[ingredient] += 1
            in_stock = self.MINIMUM_INVENTORY[ingredient] - \
                self._need_to_buy[ingredient]
            if not in_stock > 0:
                self.out_of_stock.add(ingredient)
        return False

    def get_quantities_to_buy(self):
        return self._need_to_buy

    def get_available_dishes(self):
        avaliable_dishes = set(self.lanches)
        for dishes in self.INGREDIENTS:
            for ingredient in self.INGREDIENTS[dishes]:
                if ingredient in self.out_of_stock:
                    avaliable_dishes.discard(dishes)

        print("saida", avaliable_dishes)
        return avaliable_dishes
