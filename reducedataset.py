import pandas as pd

fake = pd.read_csv("Fake.csv")
true = pd.read_csv("True.csv")

fake_small = fake.head(60000)
true_small = true.head(60000)

fake_small.to_csv("Fake.csv", index=False)
true_small.to_csv("True.csv", index=False)

print ("process is complete")
print("Files reduced successfully!")