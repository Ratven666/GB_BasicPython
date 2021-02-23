def main(argv):
   program, *args = argv
   for arg in args:
       print(f"Результат для {arg.upper()} - {currency_rates(arg)}")

   return 0


if __name__ == '__main__':
   import sys
   from utils import currency_rates

   exit(main(sys.argv))
