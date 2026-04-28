# Cloud SQL Assignment

## Overview

In this assignment, you will create a **Cloud SQL instance** on Google Cloud Platform and connect to it using the built-in **SQL client in the console**. This activity will give you hands-on experience with GCP’s managed relational database service and reinforce concepts like instance creation, database configuration, and basic SQL operations.

## Instructions

### Step 1: Create a Cloud SQL Instance

* Log in to your Google Cloud Console: [https://console.cloud.google.com](https://console.cloud.google.com)

* In the left-hand navigation menu, go to **SQL**.

* Click **"Create instance"** and select **MySQL**.

* Configure the instance with the following settings:

    * **Instance ID**: `cloudsql-assignment`

    * **Root password**: Set a secure password (remember this!)

    * **Region**: Select a region near you

    * **Zone availability**: Choose "Single zone" (default)

* Click **"Create Instance"** to begin provisioning (this may take a few minutes).

### Step 2: Create a Database

* After the instance is created, click into `cloudsql-assignment`.

* In the instance menu, select **Databases**, then click **"Create database"**.

* Use the following details:

    * **Database name**: `student_db`

    * Leave all other settings as default, then click **Create**.

### Step 3: Connect and Run a SQL Query

* In the SQL instance overview page, click **Cloud SQL Studio** in the left navigation pane.

* When prompted, enter your **root password**.

* Once connected, run the following SQL commands:

    ```sql

    CREATE TABLE test_table (
        id INT PRIMARY KEY,
        name VARCHAR(50)
    );

    INSERT INTO test_table (id, name) VALUES (1, 'GCP Learner');
    SELECT * FROM test_table;

    ```

* Take a screenshot showing the output of the final `SELECT` query.

## Requirements

* A MySQL Cloud SQL instance named `cloudsql-assignment` created successfully.

* A database named `student_db` created within the instance.

* A table named `test_table` created and populated with one record.

* Valid results when running SELECT query from step 3

