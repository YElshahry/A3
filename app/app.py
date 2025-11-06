import os, sys
from datetime import date
from typing import List, Tuple, Optional
import psycopg2, psycopg2.extras
try:
    from dotenv import load_dotenv
    load_dotenv()
except Exception:
    pass

# Makes a connection to Postgresql using values from the .env file

def get_connection():
    conn = psycopg2.connect(
        host=os.getenv("PGHOST","localhost"),
        port=os.getenv("PGPORT","5432"),
        dbname=os.getenv("PGDATABASE","a3"),
        user=os.getenv("PGUSER","postgres"),
        password=os.getenv("PGPASSWORD",""),
    )
    conn.autocommit = True
    return conn

# Gets all the rows from the 'students' table and prints them

def getAllStudents() -> List[Tuple]:
    with get_connection() as conn:
        with conn.cursor(cursor_factory=psycopg2.extras.RealDictCursor) as cur:
            cur.execute("""SELECT student_id, first_name, last_name, email, enrollment_date
                            FROM students ORDER BY student_id ASC""")
            rows = cur.fetchall()
            print("\n== getAllStudents() ==")
            for r in rows:
                print(dict(r))
            return [tuple(r.values()) for r in rows]

# Adds a new student record into the 'students' table using the values provided

def addStudent(first_name: str, last_name: str, email: str,
               enrollment_date: Optional[date]) -> int:
    with get_connection() as conn:
        with conn.cursor() as cur:
            cur.execute(
                """
                INSERT INTO students (first_name,last_name,email,enrollment_date)
                VALUES (%s,%s,%s,%s)
                RETURNING student_id
                """,
                (first_name,last_name,email,enrollment_date)
            )
            new_id = cur.fetchone()[0]
            print(f"\n== addStudent() ==\nInserted student_id={new_id}")
            return new_id

# Updates the email for a specific student based on student_id

def updateStudentEmail(student_id: int, new_email: str) -> int:
    with get_connection() as conn:
        with conn.cursor() as cur:
            cur.execute("""UPDATE students SET email=%s WHERE student_id=%s""",
                        (new_email, student_id))
            print(f"\n== updateStudentEmail() ==\nRows updated={cur.rowcount}")
            return cur.rowcount

# Deletes student from the table using their student_id

def deleteStudent(student_id: int) -> int:
    with get_connection() as conn:
        with conn.cursor() as cur:
            cur.execute("DELETE FROM students WHERE student_id=%s", (student_id,))
            print(f"\n== deleteStudent() ==\nRows deleted={cur.rowcount}")
            return cur.rowcount

# tests all functions and calls them by order

def demo_sequence():
    try:
        getAllStudents()
        new_id = addStudent("Alice","Nguyen","alice.nguyen@example.com", date(2023,9,3))
        getAllStudents()
        updateStudentEmail(new_id, "alice.n@example.com")
        getAllStudents()
        deleteStudent(new_id)
        getAllStudents()
    except psycopg2.IntegrityError as e:
        print("\nIntegrityError (likely UNIQUE email):", e); sys.exit(1)
    except psycopg2.OperationalError as e:
        print("\nOperationalError (connection issue):", e); sys.exit(1)
    except Exception as e:
        print("\nUnexpected error:", e); sys.exit(1)

if __name__=="__main__":
    demo_sequence()