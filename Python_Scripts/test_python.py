# Build the Prime applicant dataset
prime_final = prime.merge(
    applicants,
    left_on="APPLICANT_ID",
    right_on="CID",
    how="inner"
).merge(
    emails,
    left_on="APPLICANT_ID",
    right_on="ENTRY_ID",
    how="left"
)

# Add the Prime label
prime_final["TYPE"] = "Prime"

# Build the Subprime applicant dataset
subprime_final = subprime.merge(
    applicants,
    left_on="APPLICANT_ID",
    right_on="CID",
    how="inner"
).merge(
    emails,
    left_on="APPLICANT_ID",
    right_on="ENTRY_ID",
    how="left"
)

# Add the Subprime label
subprime_final["TYPE"] = "Subprime"

# Combine Prime and Subprime applicants
applicant_credit_file = pd.concat(
    [prime_final, subprime_final],
    ignore_index=True
)

# Return the requested columns
applicant_credit_file[[
    "APPLICANT_ID",
    "C_SCORE",
    "FIRST_NAME",
    "LAST_NAME",
    "CITY",
    "STATE",
    "EMAIL",
    "TYPE"
]]
