# Reference design — implement and test your own version first.
def plan_change(resource, desired, dry_run=True):
    return {'resource':resource,'desired':desired,'action':'PLAN' if dry_run else 'APPLY'}
print(plan_change('i-001','stopped'))
