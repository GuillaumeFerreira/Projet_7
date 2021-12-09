from view.dataset_view import Dataset_view
class Dataset:
    @classmethod
    def charger_dataset1(cls, store, route_params):
        store.get_data_set_1()
        Dataset_view.result()
        return "homepage", None

    @classmethod
    def charger_dataset2(cls, store, route_params):
        store.get_data_set_2()
        Dataset_view.result()

        return "homepage", None