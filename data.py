import pandas as pd

# read data
df = pd.read_csv("data/data.csv")

# # for summary table, home graphs and employee table
# st_active = st_applied = st_verif_success = st_verif_fail = 0

# # for i in df["Status"].unique():
# #     print(i)
# #
# # CREDIT_DECISION_SUCCESS ---------------------------------> st_active
# # EMPLOYEE_VERIFICATION_SUCCESS ---------------------------> st_verif_success
# # APPLIED -------------------------------------------------> st_applied
# # CREDIT_WORTHINESS_SUCCESS
# # EMPLOYEE_VERIFICATION_FAILED ----------------------------> st_verif_fail
# # PRE_SCREENING_SUCCESS
# # PRE_SCREENING_FAILED

# for status in df["Status"]:
#     if status == "APPLIED":
#         st_applied += 1
#         # df_st["Status"][status] = "Applied"
#     elif status == "CREDIT_DECISION_SUCCESS":
#         st_active += 1
#         # df_st["Status"][status] = "Active"
#     elif status == "EMPLOYEE_VERIFICATION_SUCCESS":
#         st_verif_success += 1
#         # df_st["Status"][status] = "Verif Success"
#     elif status == "EMPLOYEE_VERIFICATION_FAILED":
#         st_verif_fail += 1
#         # df_st["Status"][status] = "Verif Failed"

# print(st_active, " ", st_applied, " ", st_verif_success, " ", st_verif_fail)