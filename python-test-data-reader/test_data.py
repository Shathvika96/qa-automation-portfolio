import csv

def validate_user_data(csvpath):

    passed = 0
    failed = 0
    errors = []

    with open(csvpath,'r') as file:
        reader = csv.DictReader(file)

        for i, row in enumerate(reader,1):
           
            if row['username'] and row['password'] and row['expected']:
                passed +=1
                print(f"Row {i}: VALID - User: {row['username']}")

            else:
                failed +=1
                errors.append(f"Row {i}: MISSING DATA")
                print(f"Row {i}: INVALID")

    print("\n==validation summary==")
    print(f"Valid rows:{passed}")
    print(f"Invalid rows:{failed}")

    if errors:
        print("Errors found:")

        for error in errors:
            print("-",error)


validate_user_data("test_data.csv")

        



            
        