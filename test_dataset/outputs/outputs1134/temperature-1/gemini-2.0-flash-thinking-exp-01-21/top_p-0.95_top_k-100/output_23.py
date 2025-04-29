def get_intersection(interval1, interval2):
    start1, end1 = interval1
    start2, end2 = interval2
    intersection_start = max(start1, start2)
    intersection_end = min(end1, end2)
    if intersection_start < intersection_end:
        return [intersection_start, intersection_end]
    else:
        return None

class MyCalendarTwo:
    def __init__(self):
        self.booked = []
        self.double_booked = []

    def book(self, start, end):
        for db_start, db_end in self.double_booked:
            intersection = get_intersection([start, end], [db_start, db_end])
            if intersection:
                return False
        
        current_double_booked = []
        for b_start, b_end in self.booked:
            intersection = get_intersection([start, end], [b_start, b_end])
            if intersection:
                current_double_booked.append(intersection)
                
        self.double_booked.extend(current_double_booked)
        self.booked.append([start, end])
        return True

def run_tests():
    test_cases = [
        ([[], ['book', 'book', 'book', 'book', 'book', 'book']], [[10, 20], [50, 60], [10, 40], [5, 15], [5, 10], [25, 55]], [True, True, True, False, True, True]),
        ([[], ['book', 'book', 'book']], [[10, 20], [10, 40], [10, 30]], [True, True, False]),
        ([[], ['book', 'book', 'book', 'book']], [[24, 40], [43, 50], [27, 43], [5, 21]], [True, True, True, True]),
        ([[], ['book', 'book', 'book', 'book']], [[47, 50], [33, 41], [39, 45], [33, 42]], [True, True, True, False]),
    ]
    
    total_tests = len(test_cases)
    correct_tests = 0
    
    for i in range(total_tests):
        init_commands, book_commands = test_cases[i][0]
        book_args_list = test_cases[i][1]
        expected_outputs = test_cases[i][2]
        
        calendar = MyCalendarTwo()
        actual_outputs = []
        
        for j in range(len(book_commands)):
            command = book_commands[j]
            args = book_args_list[j]
            if command == 'book':
                result = calendar.book(args[0], args[1])
                actual_outputs.append(result)
                
        if actual_outputs == expected_outputs:
            print('True')
            correct_tests += 1
        else:
            print('False')
            
    print(f'{correct_tests}/{total_tests}')

if __name__ == '__main__':
    run_tests()