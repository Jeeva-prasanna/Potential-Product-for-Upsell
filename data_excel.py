import pandas as pd
import random

df = pd.read_csv('CDR-Call-Details.csv')


existing = set(df['Phone Number'])
seen = set()

def generate_unique_number():

    while True:
        num = f'{random.randint(100, 999)}-{random.randint(0, 9999):04d}'
        if num not in seen and num not in existing:
            return num

random.seed(42)

new_numbers = []
dup_count = 0

for num in df['Phone Number']:
    if num not in seen:

        seen.add(num)
        new_numbers.append(num)
    else:

        dup_count += 1
        new_num = generate_unique_number()
        seen.add(new_num)
        new_numbers.append(new_num)

df['Phone Number'] = new_numbers


print(f"Total rows: {len(df)}")
print(f"Duplicates replaced: {dup_count}")
print(f"Unique phone numbers now: {df['Phone Number'].nunique()}")
print(f"\nChurn distribution (left untouched, still imbalanced):")
print(df['Churn'].value_counts())
print(df['Churn'].value_counts(normalize=True) * 100)


df.to_csv('CDR-Call-Details-deduped.csv', index=False)
