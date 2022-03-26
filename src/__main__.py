import logging
from holdings import holdings

def main():
    a = holdings()
    a.getHolding()

if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO, format='%(asctime)s: %(message)s')
    logging.info('start')
    main()
    logging.info('end')