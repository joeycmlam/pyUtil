import logging
import psycopg2
import dataSource

def main():
    logging.info('main')

    db = None
    try:
        db = dataSource.dataSource()
        db.getInstance().connect()
        cur = db.getInstance().getData('select * from pflo_holding')

        # Fetch a single row using fetchone() method.
        idx = 0
        for aRow in cur:
            logging.info("[{0}]: {1}".format(idx, aRow))
            idx += 1

    except Exception as ex:
        raise ex
    finally:
        db.close()

if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO, format='%(asctime)s: %(message)s')
    logging.info('start')
    main()
    logging.info('done')