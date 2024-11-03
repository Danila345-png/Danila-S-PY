# TODO Напишите функцию find_common_participants
def find_common_participants(list1, list2, sep = ","):
    group_list1 = list1.split(sep)
    group_list2 = list2.split(sep)
    common_participants = []
    for participant in group_list1:
        if participant in group_list2:
            common_participants.append(participant)
    return sorted(common_participants)

participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"

# TODO Провеьте работу функции с разделителем отличным от запятой
result = find_common_participants(participants_first_group,participants_second_group, sep = ".")
