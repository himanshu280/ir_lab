from posting_list_generator import resolve

pre_order = {
    "!": 3,
    "^": 2,
    "+": 1,
}


def query_parser(query=None):
    if query is None:
        print("Empty query")
        return
    else:
        term_list = query.split(" ")
        operator_stack = []
        term_stack = []

        # reading terms in query one at a time
        for term in term_list:

            # if term is an operator
            if term == "^" or term == "+" or term == "!":

                # poping according to precedence order
                while(len(operator_stack) != 0 and pre_order[operator_stack[-1]] > pre_order[term]):
                    operator = operator_stack.pop()
                    term_2 = None
                    term_1 = None

                    # pop 2 terms if not operator
                    if(operator != "!"):
                        term_2 = term_stack.pop()

                    term_1 = term_stack.pop()

                    # if 'not' operator found
                    if(term_2 is None):
                        if(type(term_1) == list):
                            term_stack.append(
                                resolve(
                                    w_1=None,
                                    w_2=None,
                                    operator=operator,
                                    list_1=term_1,
                                    list_2=None
                                )
                            )
                        else:
                            term_stack.append(
                                resolve(
                                    w_1=term_1,
                                    w_2=None,
                                    operator=operator,
                                    list_1=None,
                                    list_2=None))
                    # if 'and' or 'or' operator found
                    else:
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
                        elif(type(term_1) != list and type(term_2) == list):
                            term_stack.append(
                                resolve(
                                    w_1=term_1,
                                    w_2=None,
                                    operator=operator,
                                    list_1=term_2,
                                    list_2=None))
                        elif(type(term_1) == list and type(term_2) != list):
                            term_stack.append(
                                resolve(
                                    w_1=term_2,
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

        # if parser reached end of query
        while(len(operator_stack) >= 1):
            # print(term_stack)
            operator = operator_stack.pop()
            term_2 = None
            term_1 = None

            # print(operator)

            if(operator != "!"):
                term_2 = term_stack.pop()

            term_1 = term_stack.pop()

            if(term_2 is None):
                if(type(term_1) == list):
                    term_stack.append(
                        resolve(
                            w_1=None,
                            w_2=None,
                            operator=operator,
                            list_1=term_1,
                            list_2=None
                        )
                    )
                else:
                    term_stack.append(
                        resolve(
                            w_1=term_1,
                            w_2=None,
                            operator=operator,
                            list_1=None,
                            list_2=None))
            else:
                if(type(term_1) == list and type(term_2) == list):
                    term_stack.append(
                        resolve(
                            w_1=None,
                            w_2=None, operator=operator,
                            list_1=term_1,
                            list_2=term_2))
                elif(type(term_1) == list and type(term_2) != list):
                    term_stack.append(
                        resolve(
                            w_1=term_2,
                            w_2=None,
                            operator=operator,
                            list_1=term_1,
                            list_2=None))
                elif(type(term_1) != list and type(term_2) == list):
                    term_stack.append(
                        resolve(
                            w_1=term_1,
                            w_2=None,
                            operator=operator,
                            list_1=term_2,
                            list_2=None))
                else:
                    term_stack.append(
                        resolve(
                            w_1=term_1,
                            w_2=term_2,
                            operator=operator,
                            list_1=None,
                            list_2=None))

        term_stack[0].sort()
        term_stack[0].reverse()
        print(term_stack[0])


query_parser(query="hello ^ read + made + research")
