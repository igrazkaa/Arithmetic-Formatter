from pytest import main
from arithmetic_arranger import arithmetic_arranger

if __name__ == '__main__':
    print(arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49"], True))
    print(arithmetic_arranger(['32 - 698', '1 - 3801', '45 + 43', '123 + 49', '988 + 40'], True))

    # Run unit tests automatically
    main(['-vv'])