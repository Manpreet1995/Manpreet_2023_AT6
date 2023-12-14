class main:
    def validate(self, list_of_inputs):
        numbers = []
        for item in list_of_inputs:
            if int(item) > 0:
                numbers.append(int(item))
        return numbers