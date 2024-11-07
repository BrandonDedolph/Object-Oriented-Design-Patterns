class DataFetcher:
    def __init__(self, data_type, limit=None, order_by=None):
        self.data_type = data_type
        self.limit = limit
        self.order_by = order_by

    def __str__(self):
        return f"DataFetcher(data_type={self.data_type}, limit={self.limit}, order_by={self.order_by})"
