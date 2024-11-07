from data_fetcher import DataFetcher

class DataFetcherBuilder:
    def __init__(self, data_type):
        self.data_type = data_type
        self.limit = None
        self.order_by = None

    def limited_by(self, limit):
        self.limit = limit
        return self

    def ordered_by(self, order_by):
        self.order_by = order_by
        return self

    def create(self):
        return DataFetcher(self.data_type, self.limit, self.order_by)
