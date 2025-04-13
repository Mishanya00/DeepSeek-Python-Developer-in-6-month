import psycopg
from config import load_config


def insert_vendor(vendor_name):
    sql = """INSERT INTO vendors(vendor_name)
             VALUES(%s) RETURNING vendor_id;"""
    
    vendor_id = None
    config = load_config()

    try:
        with psycopg.connect(**config) as conn:
            with conn.cursor() as cur:
                cur.execute(sql, (vendor_name,))

                # Unnecessary part
                # rows = cur.fetchone()
                # if rows:
                #     vendor_id = rows[0]
                
                conn.commit()
    except (Exception, psycopg.DatabaseError) as error:
        print(error)
    finally:
        return vendor_id
    

def insert_many_vendors(vendor_list):
    """ Insert multiple vendors into the vendors table  """

    sql = "INSERT INTO vendors(vendor_name) VALUES(%s) RETURNING *"
    config = load_config()
    try:
        with  psycopg.connect(**config) as conn:
            with  conn.cursor() as cur:
                cur.executemany(sql, vendor_list)

            conn.commit()
    except (Exception, psycopg.DatabaseError) as error:
        print(error)


if __name__ == "__main__":
    insert_vendor('Integral Corp.')

    insert_many_vendors([
        ('AKM Semiconductor Inc.',),
        ('Asahi Glass Co Ltd.',),
        ('Daikin Industries Ltd.',),
        ('Dynacast International Inc.',),
        ('Foster Electric Co. Ltd.',),
        ('Murata Manufacturing Co. Ltd.',)
    ])