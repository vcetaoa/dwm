import pandas as pd
from itertools import combinations
from collections import defaultdict

# Sample transaction data
data = {
    "T_id": ["T1", "T2", "T3", "T4", "T5"],
    "Items": [
        "Bread, Jelly, Butter",
        "Bread, Butter",
        "Bread, Milk, Butter",
        "Coke, Bread",
        "Coke, Milk",
    ],
}

# Create DataFrame and convert items to lists
df = pd.DataFrame(data)
df["Items"] = df["Items"].apply(lambda x: x.split(", "))


# Generate frequent itemsets
def get_frequent_itemsets(transactions, min_support):
    # Count 1-itemsets
    C1 = defaultdict(int)
    for items in transactions:
        for item in items:
            C1[item] += 1
    L1 = {item: count for item, count in C1.items() if count >= min_support}

    # Count 2-itemsets
    C2 = defaultdict(int)
    for items in transactions:
        for item1, item2 in combinations(set(items), 2):
            C2[tuple(sorted([item1, item2]))] += 1
    L2 = {item: count for item, count in C2.items() if count >= min_support}

    # Count 3-itemsets
    C3 = defaultdict(int)
    for items in transactions:
        for item1, item2, item3 in combinations(set(items), 3):
            C3[tuple(sorted([item1, item2, item3]))] += 1
    L3 = {item: count for item, count in C3.items() if count >= min_support}

    return C1, L1, C2, L2, C3, L3


# Calculate confidence for association rules
def get_association_rules(L1, L2):
    rules = []
    for itemset, support_count in L2.items():
        A, B = itemset
        confidence_A_to_B = (support_count / L1[A]) * 100 if L1[A] > 0 else 0
        confidence_B_to_A = (support_count / L1[B]) * 100 if L1[B] > 0 else 0

        rules.append(
            {
                "Rule": f"{A} -> {B}",
                "Support Count": support_count,
                "Confidence (%)": f"{confidence_A_to_B:.2f}%",
                "Confidence Ratio": f"({support_count}/{L1[A]})",
            }
        )
        rules.append(
            {
                "Rule": f"{B} -> {A}",
                "Support Count": support_count,
                "Confidence (%)": f"{confidence_B_to_A:.2f}%",
                "Confidence Ratio": f"({support_count}/{L1[B]})",
            }
        )
    return rules


# Execute functions
min_support = 2
C1, L1, C2, L2, C3, L3 = get_frequent_itemsets(df["Items"], min_support)
association_rules = get_association_rules(L1, L2)


# Display results
def display_results(C1, L1, C2, L2, C3, L3, rules):
    print("\nC1 Candidate Set:")
    print(f"{'Item':<10} : {'Support Count'}")
    for item, count in C1.items():
        print(f"{item:<10} : {count}")

    print("\nL1 Frequent Itemsets:")
    print(f"{'Item':<10} : {'Support Count'}")
    for item, count in L1.items():
        print(f"{item:<10} : {count}")

    print("\nC2 Candidate Set:")
    print(f"{'Itemset (A, B)':<20} : {'Support Count'}")
    for itemset, count in C2.items():
        print(f"{str(itemset):<20} : {count}")

    print("\nL2 Frequent Itemsets:")
    print(f"{'Itemset (A, B)':<20} : {'Support Count'}")
    for itemset, count in L2.items():
        print(f"{str(itemset):<20} : {count}")

    print("\nC3 Candidate Set:")
    print(f"{'Itemset (A, B, C)':<20} : {'Support Count'}")
    for itemset, count in C3.items():
        print(f"{str(itemset):<20} : {count}")

    print("\nL3 Frequent Itemsets:")
    print(f"{'Itemset (A, B, C)':<20} : {'Support Count'}")
    for itemset, count in L3.items():
        print(f"{str(itemset):<20} : {count}")

    print("\nAssociation Rules with Confidence:")
    print(
        f"{'Rule':<20} : {'Support Count'} | {'Confidence (%)'} | {'Confidence Ratio'}"
    )
    for rule in rules:
        print(
            f"{rule['Rule']:<20} : {rule['Support Count']} | {rule['Confidence (%)']} | {rule['Confidence Ratio']}"
        )


# Run the display
display_results(C1, L1, C2, L2, C3, L3, association_rules)


"""
Output:

C1 Candidate Set:
Item       : Support Count
Bread      : 4
Jelly      : 1
Butter     : 3
Milk       : 2
Coke       : 2

L1 Frequent Itemsets:
Item       : Support Count
Bread      : 4
Butter     : 3
Milk       : 2
Coke       : 2

C2 Candidate Set:
Itemset (A, B)       : Support Count
('Bread', 'Jelly')   : 1
('Butter', 'Jelly')  : 1
('Bread', 'Butter')  : 3
('Bread', 'Milk')    : 1
('Butter', 'Milk')   : 1
('Bread', 'Coke')    : 1
('Coke', 'Milk')     : 1

L2 Frequent Itemsets:
Itemset (A, B)       : Support Count
('Bread', 'Butter')  : 3

C3 Candidate Set:
Itemset (A, B, C)    : Support Count
('Bread', 'Butter', 'Jelly') : 1
('Bread', 'Butter', 'Milk') : 1

L3 Frequent Itemsets:
Itemset (A, B, C)    : Support Count

Association Rules with Confidence:
Rule                 : Support Count | Confidence (%) | Confidence Ratio
Bread -> Butter      : 3 | 75.00% | (3/4)
Butter -> Bread      : 3 | 100.00% | (3/3)

"""
