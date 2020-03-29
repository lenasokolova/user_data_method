def build_profile(first, last, **user_info):
    """Budowa słownika zawierającego wszelkie inforamcje o użytkowniku."""
    profile = {}
    profile['first_name'] = first
    profile['last_name'] = last
    for key, value in user_info.items():
        profile[key] = value
    return profile

user_profile = build_profile('lena', 'sokolova', location = 'poland', field = 'coding', language = 'polish')
print(user_profile)
