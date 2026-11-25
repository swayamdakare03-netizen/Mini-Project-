
# ==========================================
# DEIVS - EVIDENCE VERIFICATION MODULE
# ==========================================

import os

from hashing import calculate_sha256

from database import (
    get_evidence_by_id,
    save_verification
)


# ------------------------------------------
# 1. VERIFY EVIDENCE
# ------------------------------------------

def verify_evidence(evidence_id):

    # Retrieve evidence record
    record = get_evidence_by_id(evidence_id)

    if record is None:

        print("\nEvidence ID not found!")
        return

    # Check whether evidence is deleted
    if record[6] == "DELETED":

        print("\nThis evidence record has been deleted!")
        print("Verification is not allowed.")
        return

    file_name = record[1]
    file_path = record[2]
    original_hash = record[4]

    print("\n========== EVIDENCE VERIFICATION ==========")

    print("Evidence ID:", evidence_id)
    print("File Name:", file_name)

    # Check whether original file exists
    if not os.path.isfile(file_path):

        current_hash = None
        status = "MISSING"

        print("\nWARNING: Evidence file not found!")

    else:

        # Calculate current SHA-256 hash
        current_hash = calculate_sha256(file_path)

        if current_hash is None:

            status = "ERROR"

            print("\nERROR: Unable to read evidence file!")

        elif original_hash == current_hash:

            status = "UNCHANGED"

            print("\nSUCCESS: Evidence is unchanged!")

        else:

            status = "MODIFIED"

            print("\nWARNING: Evidence modification detected!")

    # Save verification history
    save_verification(
        evidence_id,
        current_hash,
        status
    )

    # Display results
    print("\nOriginal Hash:", original_hash)
    print("Current Hash:", current_hash)
    print("Verification Status:", status)

    print("===========================================")


# ------------------------------------------
# TEST VERIFICATION MODULE
# ------------------------------------------

if __name__ == "__main__":

    print("\n===== DEIVS VERIFICATION SYSTEM =====")

    try:

        evidence_id = int(
            input("Enter Evidence ID: ")
        )

        verify_evidence(evidence_id)

    except ValueError:

        print("Please enter a valid numeric Evidence ID!")
