class TruthTables:

    @staticmethod
    def or_truth_table():
        or_table = {}
        or_table['operation'] = 'or'
        case_number = 1
        for i1, i2, e in [(0, 0, 0), (1, 1, 1), (1, 0, 1), (0, 1, 1)]:
            a_case = {'input1': i1, 'input2': i2, 'expected_output': e}
            or_table['case' + str(case_number)] = a_case
            case_number = case_number + 1

        return or_table

    @staticmethod
    def and_truth_table():
        and_table = {}
        and_table['operation'] = 'and'
        case_number = 1
        for i1, i2, e in [(0, 0, 0), (1, 1, 1), (1, 0, 0), (0, 1, 0)]:
            a_case = {'input1': i1, 'input2': i2, 'expected_output': e}
            and_table['case' + str(case_number)] = a_case
            case_number = case_number + 1

        return and_table

    @staticmethod
    def xor_truth_table():
        xor_table = {}
        xor_table['operation'] = 'xor'
        case_number = 1
        for i1, i2, e in [(0, 0, 0), (1, 1, 0), (1, 0, 1), (0, 1, 1)]:
            a_case = {'input1': i1, 'input2': i2, 'expected_output': e}
            xor_table['case' + str(case_number)] = a_case
            case_number = case_number + 1

        return xor_table

    @staticmethod
    def not_truth_table():
        not_table = {}
        not_table['operation'] = 'not'
        case_number = 1
        for i1, e in [(0, 1), (1, 0)]:
            a_case = {'input1': i1, 'expected_output': e}
            not_table['case' + str(case_number)] = a_case
            case_number = case_number + 1

        return not_table
