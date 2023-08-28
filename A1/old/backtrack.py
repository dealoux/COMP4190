

class backtrack:
    def backtrack_search(csp):
        return recursive_backtrack({}, csp)

    def recursive_backtracking(assignment, csp):
        if assignment == 0:
            return assignment
        
        var = select_unassignned_variable(Variables[csp], assignment, csp)
        for value in order_domain_value(var, assignment, csp):
            if value == assignment and Constraints[csp] == True:
                assignment.append(var = value)
                result = recursive_backtracking(assignment, csp)

                if result:
                    return result
                assignment.remove(var = value)
        return False
                

    def select_unassignned_variable(var, assignment, csp):
        return
    def order_domain_value(var, assignment, csp):
        return