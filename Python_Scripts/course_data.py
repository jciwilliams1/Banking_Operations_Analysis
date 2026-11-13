import pandas as pd
from snowflake.snowpark.files import SnowflakeFile
from snowflake.snowpark.context import get_active_session


def load_course_data():
    session = get_active_session()

    with SnowflakeFile.open("@BANKING.PUBLIC.Python_CSV_stage/APPLICANT_INFO.csv", "r") as f:
        applicants = pd.read_csv(f)

    with SnowflakeFile.open("@BANKING.PUBLIC.Python_CSV_stage/DEMOGRAPHICS.csv", "r") as f:
        demographics = pd.read_csv(f)

    with SnowflakeFile.open("@BANKING.PUBLIC.Python_CSV_stage/CONTACT_EMAIL.csv", "r") as f:
        emails = pd.read_csv(f)

    with SnowflakeFile.open("@BANKING.PUBLIC.Python_CSV_stage/GUARANTOR.csv", "r") as f:
        guarantor = pd.read_csv(f)

    with SnowflakeFile.open("@BANKING.PUBLIC.Python_CSV_stage/PRIME.csv", "r") as f:
        prime = pd.read_csv(f)

    with SnowflakeFile.open("@BANKING.PUBLIC.Python_CSV_stage/SUBPRIME.csv", "r") as f:
        subprime = pd.read_csv(f)

    with SnowflakeFile.open("@BANKING.PUBLIC.Python_CSV_stage/LENDING_.csv", "r") as f:
        lending = pd.read_csv(f)

    return applicants, demographics, emails, guarantor, prime, subprime, lending