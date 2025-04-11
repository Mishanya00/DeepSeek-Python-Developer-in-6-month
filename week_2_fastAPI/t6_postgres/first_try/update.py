import psycopg
from config import load_config
from connect import connect_to_db


config = load_config()


def update_vendor(vendor_id, new_name):
    updated_row_count = 0

    sql = """ UPDATE vendors
             SET vendor_name = %s
             WHERE vendor_id = %s
            """
    try:
        # another way to obtain connection
        conn = connect_to_db(config)
        with conn:
            with conn.cursor() as cur:
                cur.execute(sql, (new_name, vendor_id))
                updated_row_count = cur.rowcount
            conn.commit()
    except (psycopg.DatabaseError, Exception) as error:
        print(error)
    finally:
        return updated_row_count


if __name__ == '__main__':
    update_vendor(1, "Updated Corp")