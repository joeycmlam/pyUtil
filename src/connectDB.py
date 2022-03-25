import logging
import psycopg2

def main():
    logging.info('main')

    try:
        # establishing the connection
        conn = psycopg2.connect(
            database="mysys", user='postgres', password='dbadmin', host='127.0.0.1', port='5432'
        )
        # Creating a cursor object using the cursor() method
        cursor = conn.cursor()

        # Executing an MYSQL function using the execute() method
        cursor.execute("select * from pflo_holding")

        # Fetch a single row using fetchone() method.
        idx = 0
        for row in cursor:
            logging.info("[{0}]: {1}".format(idx, row))
            idx += 1

    except Exception as ex:
        raise ex
    finally:
        # Closing the connection
        conn.close()

if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO, format='%(asctime)s: %(message)s')
    logging.info('start')
    main()
    logging.info('done')