class TruthTables:

    def or_truth_table(self):
        or_table = []
        a_case = {}
        for i1, i2, e in [(0, 0, 0), (1, 1, 1), (1, 0, 1), (0, 1, 1)]:
            a_case['input1'] = i1
            a_case['input2'] = i2
            a_case['expected_output'] = e
            or_table.append(a_case)

        return or_table

    def and_truth_table(self):
        and_table = []
        a_case = {}
        for i1, i2, e in [(0, 0, 0), (1, 1, 1), (1, 0, 0), (0, 1, 0)]:
            a_case['input1'] = i1
            a_case['input2'] = i2
            a_case['expected_output'] = e
            and_table.append(a_case)

        return and_table

    def xor_truth_table(self):
        xor_table = []
        a_case = {}
        for i1, i2, e in [(0, 0, 0), (1, 1, 0), (1, 0, 1), (0, 1, 1)]:
            a_case['input1'] = i1
            a_case['input2'] = i2
            a_case['expected_output'] = e
            xor_table.append(a_case)

        return xor_table

    def not_truth_table(self):
        not_table = []
        a_case = {}
        for i1, i2, e in [(0, 1), (1, 0)]:
            a_case['input1'] = i1
            a_case['input2'] = i2
            a_case['expected_output'] = e
            not_table.append(a_case)

        return not_table
