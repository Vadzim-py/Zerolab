
def is_superuser_or_staff(user):
    return user.is_superuser or user.is_staff
