# Before you start 

This project is meant to test several API endpoints for the Fireblocks system. Leave a like and subscribe if you liked :)

If you prefer to just go to the Google Sheet and take a look at the test cases, you can do it [here](https://docs.google.com/document/d/1Gq_HSwqKGWgrFVYLJRWqtagT6Z0xGB9Q1ExWDVD4VLQ/edit).

If you prefer to read it here, please continue.

## Table of Contents

1. [Create User Endpoint](#create-user-endpoint)
2. [GET Multiple Users Endpoint](#get-multiple-users-endpoint)
3. [GET Single User Endpoint](#get-single-user-endpoint)
4. [PATCH Single User Endpoint](#patch-single-user-endpoint)
5. [Delete User Endpoint](#delete-user-endpoint)
6. [Create Transactions Endpoint](#create-transactions-endpoint)
7. [Get Transactions Endpoint](#get-transactions-endpoint)

---

## Create User Endpoint

1. **Create User (Sanity Scenario)**
   - **Test Case:** User sends a request to create a new user with valid parameters (name, balance).
   - **Assertion:** Expecting a 2xx status code and a response indicating successful user creation.
   - **Test Data:**
    ```json
    "name": "string",
    "balance": 1
    ```

2. **Create User Without Mandatory Field - Name**
   - **Test Case:** User sends a request without the mandatory field 'name' to the create user endpoint.
   - **Assertion:** Expecting a 5xx status code indicating a server error demanding the 'name' field for user creation.
   - **Test Data:**
    ```json
    "balance": 1
    ```

3. **Create User Without Mandatory Field - Balance**
   - **Test Case:** User sends a request without the mandatory field 'balance' to the create user endpoint.
   - **Assertion:** Expecting a 5xx status code indicating a server error demanding the 'balance' field for user creation.
   - **Test Data:**
    ```json
    "name": "king omri"
    ```

4. **Create User with Negative Balance**
   - **Test Case:** User attempts to create a user with a negative balance.
   - **Assertion:** Expecting a 4xx status code and a response indicating that the balance cannot be negative.
   - **Test Data:**
    ```json
    "name": "king omri",
    "balance": -1
    ```

5. **Create User When Sending Balance as String**
   - **Test Case:** User attempts to create a user with a balance sent as a string instead of a number.
   - **Assertion:** Expecting a 4xx status code and a response indicating that the balance field should be a number.
   - **Test Data:**
    ```json
    "name": "king omri",
    "Balance": "1"
    ```

6. **Create User with Optional Fields**
   - **Test Case:** User attempts to create a user with optional fields not mentioned in the endpoint schema.
   - **Assertion:** Expecting a 4xx status code and a response message indicating that the field does not exist.
   - **Test Data:**
    ```json
    "name": "king omri",
    "balance": 1,
    "A": 1
    ```

7. **Create User When Sending the Balance Field Twice**
   - **Test Case:** User attempts to send the 'balance' field twice in the request.
   - **Assertion:** Expecting a 4xx status code and a response message indicating that the 'balance' field is already in the body.
   - **Test Data:**
    ```json
    {
      "name": "king omri",
      "balance": -1,
      "balance": 10
    }
    ```

8. **Create User When Sending the Name Field Twice**
   - **Test Case:** User attempts to send the 'name' field twice in the request.
   - **Assertion:** Expecting a 4xx status code and a response message indicating that the 'name' field is already in the body.
   - **Test Data:**
    ```json
    {
      "name": "-1",
      "name": "king omri",
      "balance": 10
    }
    ```

9. **Create User with Decimal Balance**
   - **Test Case:** User attempts to create a user with a decimal balance.
   - **Assertion:** Expecting a 2xx status code and a response indicating successful user creation.
   - **Test Data:**
    ```json
    "name": "string",
    "balance": 0.5
    ```

10. **Create User with Large Number in the Balance**
    - **Test Case:** User attempts to create a user with a large number in the balance.
    - **Assertion:** Expecting a 2xx status code and a response indicating successful user creation.
    - **Test Data:**
    ```json
    "name": "string",
    "balance": "10000000000000000"
    ```

11. **Create User with Empty Name**
    - **Test Case:** User attempts to create a user with an empty name.
    - **Assertion:** Expecting a 4xx status code and a response message indicating that the user name cannot be empty.
    - **Test Data:**
    ```json
    "name": ""
    ```

---

## GET Multiple Users Endpoint

1. **Get Users (Sanity Scenario)**
   - **Test Case:** Retrieve users that are known to exist in the database.
   - **Assertion:** Expecting a 2xx status code and a response containing the user data.
   - **Test Data:**
    ```json
    name: "omri"
    ```

2. **Get Users That Do Not Exist in the DB**
   - **Test Case:** Attempt to retrieve users that are known not to exist.
   - **Assertion:** Expecting a 4xx status code and a response message indicating that the user does not exist.
   - **Test Data:**
    ```json
    name: "uuid"
    ```

3. **Get Users with Same Balance**
   - **Test Case:** Retrieve all users that have the same balance.
   - **Assertion:** Expecting a 2xx status code and all users with the same balance.
   - **Test Data:**
    ```json
    Balance: 0
    ```

4. **Get Users with Unique Chars in Name**
   - **Test Case:** Retrieve users with unique characters in their name.
   - **Assertion:** Expecting a 2xx status code and a response message included with the user data.
   - **Test Data:**
    ```json
    name: "Jose*’"
    ```

5. **Get Users with Empty String Name**
   - **Test Case:** Retrieve only users with empty names and not all users.
   - **Assertion:** Expecting a 2xx status code and a response message included with the user data.
   - **Test Data:**
    ```json
    Name: ""
    ```

6. **Get Users with the Name "name"**
   - **Test Case:** Retrieve users only with the name "name" and not all users.
   - **Assertion:** Expecting a 2xx status code and a response message included with the user data.
   - **Test Data:**
    ```json
    Name: "name"
    ```

7. **Get Users with Special Characters in Name**
   - **Test Case:** Retrieve users with special characters in their names.
   - **Assertion:** Expecting a 2xx status code and a response message included with the user data.
   - **Test Data:**
    ```json
    Name: "!@#$%^&*()"
    ```

8. **Get Users with Numeric Characters in Name**
   - **Test Case:** Retrieve users with numeric characters in their names.
   - **Assertion:** Expecting a 2xx status code and a response message included with the user data.
   - **Test Data:**
    ```json
    Name: "12345"
    ```

9. **Get Users with Long Name**
   - **Test Case:** Retrieve users with a long name.
   - **Assertion:** Expecting a 2xx status code and a response message included with the user data.
   - **Test Data:**
    ```json
    Name: "a".repeat(256)
    ```

10. **Get Users with Name Containing Spaces**
    - **Test Case:** Retrieve users with names containing spaces.
    - **Assertion:** Expecting a 2xx status code and a response message included with the user data.
    - **Test Data:**
    ```json
    Name: "John Doe"
    ```

---

## GET Single User Endpoint

1. **Get User (Sanity Scenario)**
   - **Test Case:** Retrieve a user (known to exist in the DB) and verify the response.
   - **Assertion:** Expecting a 2xx status code and a response containing the user data.
   - **Test Data:**
    ```json
    Id: 2106
    ```

2. **Get User That Does Not Exist in the DB**
   - **Test Case:** Attempt to retrieve a user that is known not to exist.
   - **Assertion:** Expecting a 4xx status code and a response message indicating that the user does not exist.
   - **Test Data:**
    ```json
    Id: 1234
    ```

3. **Get User 0000 from the DB**
   - **Test Case:** Retrieve the user with ID 0000 (assuming it's the first user ever created in the system).
   - **Assertion:** Expecting a 2xx status code and a response containing the user data.
   - **Test Data:**
    ```json
    Id: 0000
    ```

4. **Get User with ID That Has Decimal Point (0.5)**
   - **Test Case:** Attempt to retrieve a user with a decimal ID.
   - **Assertion:** Expecting a 4xx status code and a response message indicating that the user was not found.
   - **Test Data:**
    ```json
    Id: 0.5
    ```

5. **Get User with Large ID**
   - **Test Case:** Retrieve a user with a large ID.
   - **Assertion:** Expecting a 2xx status code and a response containing the user data.
   - **Test Data:**
    ```json
    Id: 10000000000000000
    ```

6. **Get User with Alphanumeric ID**
   - **Test Case:** Retrieve a user with an alphanumeric ID.
   - **Assertion:** Expecting a 2xx status code and a response containing the user data.
   - **Test Data:**
    ```json
    Id: "abc123"
    ```

7. **Get User with Special Characters in ID**
   - **Test Case:** Retrieve a user with special characters in the ID.
   - **Assertion:** Expecting a 2xx status code and a response containing the user data.
   - **Test Data:**
    ```json
    Id: "!@#$%^&*()"
    ```

8. **Get User with Negative ID**
   - **Test Case:** Retrieve a user with a negative ID.
   - **Assertion:** Expecting a 4xx status code and a response message indicating that the user was not found.
   - **Test Data:**
    ```json
    Id: -1
    ```

9. **Get User with Empty ID**
   - **Test Case:** Retrieve a user with an empty ID.
   - **Assertion:** Expecting a 404 status code and a response message indicating that the user was not found.
   - **Test Data:**
    ```json
    Id: ""
    ```

10. **Get User with Non-Alphanumeric Characters in ID**
    - **Test Case:** Retrieve a user with non-alphanumeric characters in the ID.
    - **Assertion:** Expecting a 4xx status code and a response message indicating that the user was not found.
    - **Test Data:**
    ```json
    Id: "$%#@!"
    ```

---
## PATCH Single User Endpoint

1. **Update User Sanity Scenario**
   - **Test Case:** Update a user (known to exist in the DB) and retrieve the updated data.
   - **Assertion:** Expecting a 2xx status code and a response containing the updated user data.
   - **Test Data:**
    ```json
    Id: 2106
    ```

2. **Update User That Does Not Exist in the DB**
   - **Test Case:** Attempt to update a user that is known not to exist.
   - **Assertion:** Expecting a 4xx status code and a response message indicating that the user does not exist.
   - **Test Data:**
    ```json
    Id: 1234
    ```

3. **Update User with Empty Name (“”)***
   - **Test Case:** Attempt to update a user with an empty name (empty string).
   - **Assertion:** Expecting a 4xx status code and a response message indicating that the user name cannot be an empty string.
   - **Test Data:**
    ```json
    Id: 2106,
    "name": ""
    ```

4. **Update User with Decimal Balance**
   - **Test Case:** Attempt to update a user with a decimal balance (e.g., 0.5).
   - **Assertion:** Expecting a 2xx status code and a response indicating successful user update.
   - **Test Data:**
    ```json
    Id: 2106,
    "name": "string",
    "balance": 0.5
    ```

5. **Update User with Optional Fields**
   - **Test Case:** Attempt to update a user with optional fields not mentioned in the endpoint schema.
   - **Assertion:** Expecting a 2xx status code and a response indicating successful user update (ignoring optional fields).
   - **Test Data:**
    ```json
    Id: 2106,
    "name": "king omri",
    "balance": 1,
    "A": 1
    ```

6. **Update User with Negative Balance**
   - **Test Case:** Attempt to update a user with a negative balance.
   - **Assertion:** Expecting a 4xx status code and a response indicating that the balance cannot be negative.
   - **Test Data:**
    ```json
    Id: 2106,
    "name": "king omri",
    "balance": -1
    ```

7. **Update User Without Mandatory Field - Name**
   - **Test Case:** Attempt to update a user without the mandatory field 'name.'
   - **Assertion:** Expecting a 5xx status code indicating a server error demanding the 'name' field for user update.
   - **Test Data:**
    ```json
    Id: 2106,
    "balance": 1
    ```

8. **Update User Without Mandatory Field - Balance**
   - **Test Case:** Attempt to update a user without the mandatory field 'balance.'
   - **Assertion:** Expecting a 5xx status code indicating a server error demanding the 'balance' field for user update.
   - **Test Data:**
    ```json
    Id: 2106,
    "name": "king omri"
    ```

## Delete User Endpoint

1. **Delete User Sanity Scenario**
   - **Test Case:** Delete a user (known to exist in the DB) and attempt to retrieve the deleted user.
   - **Assertion:** Expecting a 2xx status code and a response containing the deleted user data.
   - **Test Data:**
    ```json
    Id: 2106
    ```

2. **Delete User That Does Not Exist in the DB**
   - **Test Case:** Attempt to delete a user that is known not to exist.
   - **Assertion:** Expecting a 4xx status code and a response message indicating that the user does not exist.
   - **Test Data:**
    ```json
    Id: 1234
    ```

## Create Transactions Endpoint

1. **Create Transactions - Sanity**
   - **Test Case:** Create a transaction and verify it by checking the response status code (2xx) and the presence of a UUID in the response.
   - **Test Data:**
    ```json
    sourceId: 1,
    destinationId: 1,
    Amount: 1
    ```

2. **Create Transactions - sourceId is Missing**
   - **Test Case:** Attempt to create a transaction without the mandatory field 'sourceId.'
   - **Assertion:** Expecting a 5xx status code indicating a server error demanding the 'sourceId' field for transaction creation.
   - **Test Data:**
    ```json
    sourceId: null,
    destinationId: 1,
    Amount: 1
    ```

3. **Create Transactions - destinationId is Missing**
   - **Test Case:** Attempt to create a transaction without the mandatory field 'destinationId.'
   - **Assertion:** Expecting a 5xx status code indicating a server error demanding the 'destinationId' field for transaction creation.
   - **Test Data:**
    ```json
    sourceId: 1,
    destinationId: null,
    Amount: 1
    ```

4. **Create Transactions - Amount is Missing**
   - **Test Case:** Attempt to create a transaction without the mandatory field 'Amount.'
   - **Assertion:** Expecting a 5xx status code indicating a server error demanding the 'Amount' field for transaction creation.
   - **Test Data:**
    ```json
    sourceId: 1,
    destinationId: 1,
    Amount: 0
    ```

5. **Create Transactions with Negative Amount**
   - **Test Case:** Create a transaction with a negative amount.
   - **Assertion:** Expecting a 2xx status code and a response containing the UUID.
   - **Test Data:**
    ```json
    sourceId: 1,
    destinationId: 1,
    Amount: -5
    ```

6. **Create Transactions When Amount Set to 0**
   - **Test Case:** Create a transaction with an amount set to 0.
   - **Assertion:** Expecting a 2xx status code and a response containing the UUID.
   - **Test Data:**
    ```json
    sourceId: 1,
    destinationId: 1,
    Amount: 0
    ```

7. **Create Transactions When Amount Set to 0.5 (Decimal Number)**
   - **Test Case:** Create a transaction with an amount set to 0.5 (decimal number).
   - **Assertion:** Expecting a 2xx status code and a response containing the UUID.
   - **Test Data:**
    ```json
    sourceId: 1,
    destinationId: 1,
    Amount: 0.5
    ```

8. **Create Transaction When the sourceId and destinationId Are the Same**
   - **Test Case:** Create a transaction where the sourceId and destinationId are the same.
   - **Assertion:** Expecting a 2xx status code and a





## Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/jtizdev/fireblocks.git
    ```

2. Navigate to the project directory:

    ```bash
    cd fireblocks
    ```

4. export environments variables:
   ```bash
    export BASE_URL=https://fb-sandbox-dot-shell-dev-env.uc.r.appspot.com export TOKEN=youremaili@gmail.com

    ```


## Running Tests

To run the tests, follow these steps:

1. Ensure that pytest is installed:

    ```bash
    pip install pytest
    ```

2. Navigate to the `tests` directory:

    ```bash
    cd fireblocks/tests
    ```

3. Run pytest:

    ```bash
    python -m pytest
    ```

This command will execute all the tests in the specified directory and provide you with the results.


## Authors

- [@omribashan](https://github.com/jtizdev)

