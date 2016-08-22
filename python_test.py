def solution(X):
    if (X <= 20000):
        tax = X * 0.2
        final_tax = tax - 3300
        int(final_tax)
        if (final_tax < 0):
            final_tax = 0
        return final_tax
    if (X > 20000):
        lower_tax = 20000 * 0.2
        remaining_income = X - 20000
        upper_tax = remaining_income * 0.4
        tax = lower_tax + upper_tax
        final_tax = tax - 3300
        int(final_tax)
        if (final_tax < 0):
            final_tax = 0
        return final_tax

solution(40000)
