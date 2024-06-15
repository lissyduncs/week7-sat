def personal_details(**kwargs):
    for key, value in kwargs.items():
        print(f"{key} ---> {value}")

personal_details(name="lissy", address="Sydney")