index_character = ["RT", "CF", "JM", "AN"]

def interpret_choices(survey_item, choices_item):
    choices_item -= 4
    result = [0] * 4
    
    if survey_item[0] > survey_item[1]:
        survey_item = survey_item[::-1]
        choices_item *= -1

    char_to_index = {'R': 0, 'C': 1, 'J': 2, 'A': 3}
    result[char_to_index[survey_item[0]]] += choices_item
    return result

def make_answer(result):
    return ''.join(
        index_character[i][0] if result[i] <= 0 else index_character[i][1]
        for i in range(4)
    )

def solution(survey, choices):
    result = [0] * 4
    for s_item, c_item in zip(survey, choices):
        temp_result = interpret_choices(s_item, c_item)
        result = [r + t for r, t in zip(result, temp_result)]
    return make_answer(result)
