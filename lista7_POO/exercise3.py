class List_personalized(list):
    def __init__(self, list, weights=[]) -> None:
        super().__init__()
        self.p_list = list
        self.w_list = weights
        
    def avrage(self) -> float:
        avrage = sum(self.p_list)/len(self.p_list)
        return avrage

    def weighted_avrage(self) -> float:
        weighted_numbers = []
        for number in self.p_list:
            for weight in self.w_list:
                weighted_number = number*weight
                weighted_numbers.append(weighted_number)
        wheited_avrage = sum(weighted_numbers)/len(weighted_numbers)
        return wheited_avrage


ordinary_list = [10,10,10,5,5,5]
# weight_list = [1,4,1,1,2,1]

lista_p = List_personalized(ordinary_list)
print(lista_p.avrage())
# print(lista_p.weighted_avrage())
