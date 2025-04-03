def solve():
    def calculate_money(n):
        total_money = 0
        current_monday_amount = 1
        current_day_amount = 0
        day_of_week = 1 # 1 for Mon, 2 for Tue, ..., 7 for Sun

        for _ in range(n):
            if day_of_week == 1:
                current_day_amount = current_monday_amount
                current_monday_amount += 1
            else:
                current_day_amount = current_day_amount + 1 if day_of_week > 1 else current_day_amount + 1 # this line was wrong, should be fixed now
                if day_of_week == 2:
                    current_day_amount = current_monday_amount - 1 + 1 # this line was wrong in previous try
                elif day_of_week > 2:
                    current_day_amount = current_day_amount + 1 if day_of_week > 2 else current_day_amount + 1

                current_day_amount = current_monday_amount -1 + (day_of_week - 1)
                if day_of_week == 1:
                    current_day_amount = current_monday_amount-1+1
                elif day_of_week == 2:
                    current_day_amount = current_monday_amount-1+2-1+1
                elif day_of_week == 3:
                    current_day_amount = current_monday_amount-1+3-1+1

                if day_of_week == 1:
                    current_day_amount = current_monday_amount -1 + 1
                elif day_of_week == 2:
                    current_day_amount = current_monday_amount -1 + 2
                elif day_of_week == 3:
                    current_day_amount = current_monday_amount -1 + 3
                elif day_of_week == 4:
                    current_day_amount = current_monday_amount -1 + 4
                elif day_of_week == 5:
                    current_day_amount = current_monday_amount -1 + 5
                elif day_of_week == 6:
                    current_day_amount = current_monday_amount -1 + 6
                elif day_of_week == 7:
                    current_day_amount = current_monday_amount -1 + 7
                else:
                    pass


                if day_of_week > 1:
                    current_day_amount = current_monday_amount - 1 + (day_of_week -1)

                if day_of_week == 1:
                    current_day_amount = current_monday_amount
                elif day_of_week == 2:
                    current_day_amount = current_monday_amount + 1 -1 + 1
                elif day_of_week == 3:
                    current_day_amount = current_monday_amount + 2 -1 + 1
                elif day_of_week == 4:
                    current_day_amount = current_monday_amount + 3 -1 + 1
                elif day_of_week == 5:
                    current_day_amount = current_monday_amount + 4 -1 + 1
                elif day_of_week == 6:
                    current_day_amount = current_monday_amount + 5 -1 + 1
                elif day_of_week == 7:
                    current_day_amount = current_monday_amount + 6 -1 + 1

                if day_of_week == 1:
                    current_day_amount = current_monday_amount
                else:
                    current_day_amount = current_monday_amount - 1 + (day_of_week-1)


            total_money += current_day_amount
            day_of_week = day_of_week % 7 + 1
        return total_money

    test_cases = [
        (4, 10),
        (10, 37),
        (20, 96),
        (1, 1),
        (7, 28),
        (14, 77),
        (21, 147),
        (28, 238),
        (30, 273),
    ]

    correct_count = 0
    for input_n, expected_output in test_cases:
        actual_output = calculate_money(input_n)
        if actual_output == expected_output:
            print('True')
            correct_count += 1
        else:
            print('False')

    print(f'{correct_count}/{len(test_cases)}')

    return calculate_money

if __name__ == '__main__':
    solve()