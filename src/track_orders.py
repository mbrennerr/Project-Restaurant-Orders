class TrackOrders:
    def __init__(self):
        self.__orders = []

    def __len__(self):
        return len(self.__orders)

    def add_new_order(self, customer, order, day):
        return self.__orders.append({
            "customer": customer,
            "order": order,
            "day": day
        })

    def get_most_ordered_dish_per_customer(self, customer):
        filtered_order = [
            order["order"] for order in self.__orders
            if order["customer"] == customer]
        print("saída_func_most_ordered", filtered_order)
        return max(set(filtered_order), key=filtered_order.count)

    def get_never_ordered_per_customer(self, customer):
        ALL_LANCHES = [curtomer["order"] for curtomer in self.__orders]
        LANCHEs_BY_JOAO = [
            curtomer["order"]
            for curtomer in self.__orders
            if curtomer["customer"] == customer
        ]
        # print("saída_lanches", ALL_LANCHES)
        # print("saída_lanches_by_joao", LANCHEs_BY_JOAO)
        return set(set(ALL_LANCHES).difference(set(LANCHEs_BY_JOAO)))
        # return list(filtered_order)

    def get_days_never_visited_per_customer(self, customer):
        ALL_DAYS = [order["day"] for order in self.__orders]
        CUSTOMER_DAYS = [curtomer["day"]
                         for curtomer in self.__orders
                         if curtomer["customer"] == customer]
        return set(set(ALL_DAYS).difference(set(CUSTOMER_DAYS)))

    def get_busiest_day(self):
        FILTERED_DAYS = [order["day"] for order in self.__orders]
        return max(set(FILTERED_DAYS), key=FILTERED_DAYS.count)

    def get_least_busy_day(self):
        FILTERED_DAYS = [order["day"] for order in self.__orders]
        return min(set(FILTERED_DAYS), key=FILTERED_DAYS.count)


csv_parsed = [
    ["maria", "pizza", "terça-feira"],
    ["maria", "hamburguer", "terça-feira"],
    ["joao", "hamburguer", "terça-feira"],
    ["maria", "coxinha", "segunda-feira"],
    ["arnaldo", "misto-quente", "terça-feira"],
    ["jose", "hamburguer", "sabado"],
    ["maria", "hamburguer", "terça-feira"],
    ["maria", "hamburguer", "terça-feira"],
    ["joao", "hamburguer", "terça-feira"],
]

track_orders = TrackOrders()
for name, food, day in csv_parsed:
    track_orders.add_new_order(name, food, day)
most_ordered = track_orders.get_most_ordered_dish_per_customer("maria")
print("saída_teste_most_ordered", most_ordered)

track_orders = TrackOrders()
for name, food, day in csv_parsed:
    track_orders.add_new_order(name, food, day)
never_ordered = track_orders.get_never_ordered_per_customer("joao")
print("saída_teste_never_ordered", never_ordered)

track_order = TrackOrders()
for name, food, day in csv_parsed:
    track_orders.add_new_order(name, food, day)
never_visited = track_orders.get_days_never_visited_per_customer("joao")
print("saída_teste_never_visited", never_visited)
