def recursive_nth_fibo(n):
    if n == 1 or n == 0:
        return n
    return recursive_nth_fibo(n-1) + recursive_nth_fibo(n-2)


def main():
    print(recursive_nth_fibo(7))


if __name__ == "__main__":
    main()
