import logging
import psycopg2

def main():
    logging.info('main')

    try:
        # establishing the connection
        conn = psycopg2.connect(
            database="postgres", user='postgres', password='dbadmin', host='127.0.0.1', port='5432'
        )
        # Creating a cursor object using the cursor() method
        cursor = conn.cursor()

        # Executing an MYSQL function using the execute() method
        cursor.execute("select version()")

        # Fetch a single row using fetchone() method.
        data = cursor.fetchone()
        logging.info("Connection established to: {0}".format(data))
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