# Read-only reference solution.
def account_role_arn(account_id, role_name):
    return f'arn:aws:iam::{account_id}:role/{role_name}'
print(account_role_arn('123456789012','InventoryRole'))
