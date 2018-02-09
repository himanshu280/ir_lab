from posting_list_generator import resolve

pre_order = {
    "^": 1,
    "+": 2,
    "!": 3
}


def query_parser(query=None):
    if query is None:
        print("Empty query")
        return
    else:
        term_list = query.split(" ")
        operator_stack = []
        term_stack = []
        for term in term_list:
            if term == "^" or term == "+" or term == "!":
                while(len(operator_stack[-1]) != 0 and pre_order[operator_stack[-1]] > pre_order[term]):
                    term_1 = term_stack.pop()
                    term_2 = term_stack.pop()
                    operator = operator_stack.pop()

                    if(type(term_1) == list and type(term_2) == list):
                        term_stack.append(
                            resolve(
                                w_1=None,
                                w_2=None,
                                operator=operator,
                                list_1=term_1,
                                list_2=term_2
                            )
                        )
                    elif(
                        (type(term_1) != list and type(term_2) == list)
                        or
                            (type(term_1) == list and type(term_2) != list)):
                        term_stack.append(
                            resolve(
                                w_1=term_1,
                                w_2=None,
                                operator=operator,
                                list_1=term_1,
                                list_2=None))
                    else:
                        term_stack.append(
                            resolve(
                                w_1=term_1,
                                w_2=term_2,
                                operator=operator,
                                list_1=None,
                                list_2=None))
                operator_stack.append(term)
            else:
                term_stack.append(term)

        while(len(term_stack) > 1):
            term_1 = term_stack.pop()
            term_2 = term_stack.pop()
            operator = operator_stack.pop()

            if(type(term_1) == list and type(term_2) == list):
                term_stack.append(
                    resolve(
                        w_1=None,
                        w_2=None, operator=operator,
                        list_1=term_1,
                        list_2=term_2))
            elif(
                (type(term_1) != list and type(term_2) == list)
                or
                    (type(term_1) == list and type(term_2) != list)):
                term_stack.append(
                    resolve(
                        w_1=term_1,
                        w_2=None,
                        operator=operator,
                        list_1=term_1,
                        list_2=None))
            else:
                term_stack.append(
                    resolve(
                        w_1=term_1,
                        w_2=term_2,
                        operator=operator,
                        list_1=None,
                        list_2=None))

        print(term_stack[0])


query_parser(query="read ^ made")
