import psycopg2
import psycopg2.extras  # to make cursor return value as dictionary

print("=" * 30, "without 'WITH'", "=" * 30)
connection, cursor = (None, None)

try:
    connection = psycopg2.connect(
        host="localhost",
        dbname="demo",
        user="postgres",
        password="diwa123",
        port=5432,
    )

    cursor = connection.cursor(cursor_factory=psycopg2.extras.DictCursor)

    cursor.execute("DROP TABLE IF EXISTS student")

    # Create Table
    create_query = """
                    CREATE TABLE IF NOT EXISTS student(
                        id int PRIMARY KEY,
                        name varchar(20) NOT NULL,
                        cgpa float,
                        dept_id varchar(30)
                    )
"""
    cursor.execute(create_query)

    # Insert Values
    insert_query = "INSERT INTO student(id, name, cgpa, dept_id) VALUES(%s, %s, %s, %s)"
    insert_values = [
        (101, "Rohith", 9.78, "CSE"),
        (102, "Abhishek", 9.5, "CSE"),
        (103, "Aadithya", 9.77, "CSE"),
    ]

    for record in insert_values:
        cursor.execute(insert_query, record)

    cursor.execute("SELECT * FROM student")
    # print(cursor.fetchall())

    for record in cursor.fetchall():
        print(record["name"], record["id"], record["cgpa"])

    # Update values
    update_query = "UPDATE student SET cgpa = (cgpa + 0.1)"
    cursor.execute(update_query)

    print("----After Updating----")
    cursor.execute("SELECT * FROM student")
    for record in cursor.fetchall():
        print(record["name"], record["id"], record["cgpa"])

    # Delete row
    delete_query = "DELETE FROM student WHERE name = %s"
    delete_record = ("Abhishek",)
    cursor.execute(delete_query, delete_record)

    print("----After deleting----")
    cursor.execute("SELECT * FROM student")
    for record in cursor.fetchall():
        print(record["name"], record["id"])

    # commit to push the changes to the database
    connection.commit()
except Exception as e:
    print(e)
finally:
    if cursor is not None:
        cursor.close()
    if connection is not None:
        connection.close()


print("=" * 30, "with 'WITH'", "=" * 30)
connection = None

try:
    with psycopg2.connect(
        host="localhost",
        dbname="demo",
        user="postgres",
        password="diwa123",
        port=5432,
    ) as connection:

        with connection.cursor(cursor_factory=psycopg2.extras.DictCursor) as cursor:

            cursor.execute("DROP TABLE IF EXISTS student")

            # Create Table
            create_query = """
                            CREATE TABLE IF NOT EXISTS student(
                                id int PRIMARY KEY,
                                name varchar(20) NOT NULL,
                                cgpa float,
                                dept_id varchar(30)
                            )
        """
            cursor.execute(create_query)

            # Insert Values
            insert_query = (
                "INSERT INTO student(id, name, cgpa, dept_id) VALUES(%s, %s, %s, %s)"
            )
            insert_values = [
                (101, "Rohith", 9.78, "CSE"),
                (102, "Abhishek", 9.5, "CSE"),
                (103, "Aadithya", 9.77, "CSE"),
            ]

            for record in insert_values:
                cursor.execute(insert_query, record)

            cursor.execute("SELECT * FROM student")
            # print(cursor.fetchall())

            for record in cursor.fetchall():
                print(record["name"], record["id"], record["cgpa"])

            # Update values
            update_query = "UPDATE student SET cgpa = (cgpa + 0.1)"
            cursor.execute(update_query)

            print("----After Updating----")
            cursor.execute("SELECT * FROM student")
            for record in cursor.fetchall():
                print(record["name"], record["id"], record["cgpa"])

            # Delete row
            delete_query = "DELETE FROM student WHERE name = %s"
            delete_record = ("Abhishek",)
            cursor.execute(delete_query, delete_record)

            print("----After deleting----")
            cursor.execute("SELECT * FROM student")
            for record in cursor.fetchall():
                print(record["name"], record["id"])

            # connection.commit() # Not required when using 'with'
except Exception as e:
    print(e)
finally:

    if connection is not None:
        connection.close()
