class main:
    def validate(self, list_of_inputs):
        numbers = []
        for the_input in list_of_inputs:
            if int(the_input) > 0 and the_input.isdigit():
                numbers.append(int(the_input))
        return numbers