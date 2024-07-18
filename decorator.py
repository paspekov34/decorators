def is_prime(func):
    def wrapper(*args):
        result = func(*args)
        if result > 1:
            for i in range(2, int(result * 0.5) + 1):
                if result % i == 0:
                    return result
            print("Простое")
        else:
            print("Составное")
        return result
    return wrapper


@is_prime
def sum_three(a, b, c):
    result = a + b + c
    return result


result = sum_three(2, 3, 6)
print(result)
