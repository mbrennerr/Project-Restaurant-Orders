from utils.utils import Utils


def analyze_log(path_to_file):
    order = Utils.read_csv(path_to_file)
    return order
