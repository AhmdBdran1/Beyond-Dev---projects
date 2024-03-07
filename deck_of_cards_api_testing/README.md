# Automated Testing for Deck of Cards API

This project aims to automate tests for the Deck of Cards API server using Python and the `requests` library. The tests are structured following a simple design pattern, ensuring the reliability and functionality of the API endpoints.

## Overview

The Deck of Cards API provides endpoints for managing decks of cards, drawing cards, and creating piles within decks. Automated testing ensures that these endpoints function correctly and return the expected responses.

## Tools and Technologies

- Python: Python is used for writing test scripts due to its simplicity and versatility.
- `requests` Library: The `requests` library is utilized for making HTTP requests to the API endpoints and handling responses.
- Unittest Framework: The Unittest framework is employed for organizing and executing test cases efficiently.

## Project Structure

The project is structured into several directories to organize the code effectively:

- **infra**: Contains any infrastructure-related code, such as configuration files or setup required for testing with the Deck of Cards API.
- **logic**: Consists of the core logic of the application, including utilities, helpers, and any additional logic required for testing.
- **tests**: Houses the test scripts responsible for sending requests to API endpoints and validating the responses.

## Test Scenarios

The tests cover various scenarios and interactions with the Deck of Cards API, including:

- Creating new decks
- Drawing cards from decks
- Creating and managing piles within decks
- Validating response formats and data integrity

## Running Tests

Ensure you have Python installed on your system and install the necessary dependencies, including the `requests` library. Configure any parameters required for testing, such as base URL or authentication tokens, in the `infra` directory.

To run the tests, navigate to the `tests` directory and execute the test script(s) using Python. Review the test results to ensure the API endpoints are functioning correctly and meeting the specified criteria.
