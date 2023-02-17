def buscar(Input):
    accepted_numbers = [5, 7, 9]
    inserted_numbers_dict = {i: False for i in accepted_numbers}
    
    Output = []
    for n in Input:
        if n in inserted_numbers_dict and not inserted_numbers_dict[n]:
            Output.append(n)
            inserted_numbers_dict[n] = True
            
    Output.sort()
    return Output
