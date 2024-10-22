# Star Schema Setup Guide

## 1) Create a Database
- **Steps:**
  1. Open SQL Server Management Studio (SSMS).
  2. Right-click on **Databases** in the Object Explorer.
  3. Select **New Database**.
  4. Enter the database name and click **OK** to create it.

---

## 2) Create Dimension and Fact Tables
- **Steps:**
  1. In the Object Explorer, expand your database.
  2. Right-click on **Tables** and select **New > Table**.
  3. Add **column names** and **data types** as needed.
  4. Uncheck **Allow Null Values** if the column should not contain nulls.
  5. After adding columns, click the **Close** button.
  6. **Save the table** with a suitable name (e.g., `Fact_Sales` or `Dim_Product`).

---

## 3) Create a Database Diagram
- **Steps:**
  1. In the Object Explorer, expand your database.
  2. Right-click on **Database Diagrams** and select **New Database Diagram**.
  3. Add the required **tables** to the diagram by selecting them from the list.
  4. Click **OK** to generate the diagram.

---

## 4) Set Primary Keys in the Diagram
- **Steps:**
  1. In the database diagram, **right-click** on the column you want to set as the primary key.
  2. Select **Set Primary Key** from the context menu.

---

## 5) Add Relationships to the Diagram
- **Steps:**
  1. In the diagram, **right-click** on the **fact table** and select **Relationships**.
  2. Click **Add** to add a new relationship.
  3. In the **Tables and Columns Specification** section, click **...** to specify related tables.
  4. Select the **foreign key column** from the dimension table and **match it with the primary key** in the fact table.
  5. Click **OK** to establish the relationship.

---

## Conclusion
Following these steps will help you successfully set up a **Star Schema** with a **fact table**, **dimension tables**, and **relationships** in your database. The primary keys and foreign keys will ensure a well-structured relational model.
