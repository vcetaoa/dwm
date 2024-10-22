
# OLAP Operations in SQL

## 1) Roll-up
```sql
SELECT Time_dw.yr, SUM(Total_sales)
FROM Fact_sales
JOIN Product_dw ON Fact_sales.prod_id = Product_dw.prod_id
JOIN Time_dw ON Fact_sales.time_id = Time_dw.time_id
GROUP BY Time_dw.yr;
```

## 2) Drill-down
```sql
SELECT Time_dw.qt, SUM(Total_sales)
FROM Fact_sales 
JOIN Product_dw ON Fact_sales.prod_id = Product_dw.prod_id
JOIN Time_dw ON Fact_sales.time_id = Time_dw.time_id
GROUP BY Time_dw.qt;
```

## 3) Pivot
```sql
SELECT yr, month, qt
FROM Time_dw AS source_table;
```

## 4) Slice
```sql
SELECT Prod_name, Total_sales
FROM Fact_sales
INNER JOIN Product_dw ON Fact_sales.prod_id = Product_dw.prod_id;
```

## 5) Dice
```sql
SELECT Prod_name, Total_sales, day
FROM ((Fact_sales
INNER JOIN Product_dw ON Fact_sales.prod_id = Product_dw.prod_id)
JOIN Time_dw ON Fact_sales.time_id = Time_dw.time_id);
```
