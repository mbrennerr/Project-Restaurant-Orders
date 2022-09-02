import csv

# aqui vão constar os métodos pros requisitos;
# which plate is most ordered by 'maria'?;
# How many times did 'arnaldo' ask for 'hamburguer'?;
# which plates 'joao' never ordered?;
# which days 'joao' never visited?;


class Utils:
    @staticmethod
    def read_csv(path):
        if not path.endswith('.csv'):
            raise FileNotFoundError(f"Extensão inválida:'{path}'")
        try:
            with open(path, 'r', encoding='utf-8') as file:
                orders = []
                data = csv.DictReader(file, delimiter=",", quotechar='"')
                for order in data:
                    orders.append(order)
            return orders
        except FileNotFoundError:
            raise FileNotFoundError(f"Arquivo inexistente:'{path}'")
