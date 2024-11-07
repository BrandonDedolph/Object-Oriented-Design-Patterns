from data_fetcher_builder import DataFetcherBuilder

data_fetcher = (DataFetcherBuilder("users")
                .limited_by(10)
                .ordered_by("username")
                .create())

print(data_fetcher)
