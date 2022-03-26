import logging
import psycopg2
import dataSource

def main():
    logging.info('main')

    try:
        # establishing the connection
        # conn = psycopg2.connect(
        #     database="mysys", user='postgres', password='dbadmin', host='127.0.0.1', port='5432'
        # )

        db = dataSource()

        db.connect()

        cur = db.getData('select * from pflo_holding')

        # Fetch a single row using fetchone() method.
        idx = 0
        for row in cur:
            logging.info("[{0}]: {1}".format(idx, row))
            idx += 1

    except Exception as ex:
        raise ex
    finally:
        # Closing the connection
        # conn.close()
        dataSource.dataSource.close()

if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO, format='%(asctime)s: %(message)s')
    logging.info('start')
    main()
    logging.info('done')