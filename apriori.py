import pandas as pd 
from mlxtend.frequent_patterns import apriori, association_rules 
from mlxtend.preprocessing import TransactionEncoder 
# Load your dataset 
data = pd.read_csv('Market_Basket_Optimisation.csv', header=None) 
# Convert the dataset into a list of lists 
transactions = [] 
for i in range(len(data)): 
transactions.append([str(item) for item in data.iloc[i] if str(item) != 'nan']) 
# Apply the Transaction Encoder to one-hot encode the transactions 
te = TransactionEncoder() 
te_ary = te.fit(transactions).transform(transactions) 
df = pd.DataFrame(te_ary, columns=te.columns_) 
# Apply the Apriori algorithm 
frequent_itemsets = apriori(df, min_support=0.02, use_colnames=True) 
# Generate association rules 
rules = association_rules(frequent_itemsets, metric="confidence", min_threshold=0.5) 
# Output the frequent itemsets and association rules 
print(frequent_itemsets) 
print(rules)
