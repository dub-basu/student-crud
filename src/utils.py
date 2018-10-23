class Student:
        
    def __init__(self, roll_number = None, name = None, rank = None ):
        self.roll_number = roll_number
        self.name = name
        self.rank = rank

def merge_sort(students):

    def merge(list1, list2):
        count1, count2 = 0, 0
        len1 = len(list1)
        len2 = len(list2)
        
        merged_list = []

        while count1 < len1 and count2 < len2:
            if compare(list1[count1], list2[count2]):
                merged_list.append(list1[count1])
                count1 += 1
            else:
                merged_list.append(list2[count2])
                count2 += 1

        while(count1 < len1):
            merged_list.append(list1[count1])
            count1 += 1

        while(count2 < len2):
            merged_list.append(list2[count2])
            count2 += 1

        return merged_list

    
    def compare(stud1, stud2):
        if(stud1.name.lower() < stud2.name.lower()):
            return True
        else:
            return False

    number_of_students = len(students)
    
    if number_of_students <= 1:
        return students
    elif number_of_students > 1:
        first_half = students[:number_of_students//2]
        second_half = students[number_of_students//2:]

        first_half = merge_sort(first_half)
        second_half = merge_sort(second_half)

        students = merge(first_half, second_half)

        return students
        