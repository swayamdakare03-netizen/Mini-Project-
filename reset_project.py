
# ==========================================
# DEIVS - DATABASE RESET MODULE
# ==========================================

import sqlite3

DATABASE_NAME = "evidence.db"


# ------------------------------------------
# RESET DATABASE
# ------------------------------------------

def reset_database():

    print("\n========================================")
    print("          DEIVS RESET SYSTEM")
    print("========================================")

    print("\nWARNING: THIS ACTION IS PERMANENT!")

    print("\nThe following data will be deleted:")
    print("1. All registered evidence records")
    print("2. All verification history")
    print("3. All existing Evidence IDs")

    print("\nThe following will be preserved:")
    print("1. Original evidence files")
    print("2. Generated PDF reports")
    print("3. Database structure")
    print("4. Python project files")

    confirmation = input(
        "\nType RESET to confirm: "
    ).strip()

    if confirmation != "RESET":

        print("\nDatabase reset cancelled!")
        return False

    connection = None

    try:

        connection = sqlite3.connect(DATABASE_NAME)

        cursor = connection.cursor()

        # Delete verification history first
        cursor.execute("""
        DELETE FROM verification_history
        """)

        # Delete all evidence records
        cursor.execute("""
        DELETE FROM evidence
        """)

        # Reset automatic ID counters
        cursor.execute("""
        DELETE FROM sqlite_sequence
        WHERE name IN ('evidence', 'verification_history')
        """)

        connection.commit()

        print("\n========================================")
        print("       DATABASE RESET SUCCESSFUL!")
        print("========================================")

        print("\nAll evidence records deleted.")
        print("Verification history cleared.")
        print("Evidence IDs reset to 1.")
        print("Database structure preserved.")

        print("\nDEIVS IS READY FOR A FRESH START!")

        return True

    except sqlite3.Error as error:

        if connection:
            connection.rollback()

        print("\nDatabase reset failed!")
        print("Error:", error)

        return False

    finally:

        if connection:
            connection.close()


# ------------------------------------------
# TEST RESET MODULE
# ------------------------------------------

if __name__ == "__main__":

    reset_database()
