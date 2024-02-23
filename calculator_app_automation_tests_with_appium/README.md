# Automated Testing for Calculator App

This project aims to automate tests for a calculator app using Appium and Python. The tests are structured following the Page Object Model (POM) design pattern, enhancing maintainability and reusability.

## Overview

The Calculator App is a commonly used utility on mobile devices, and automated testing ensures its functionality remains intact across various operations.

## Tools and Technologies

- Appium: Appium is an open-source tool for automating mobile applications. It supports multiple platforms (iOS, Android) and provides a unified API for both native and hybrid mobile apps.
- Python: Python is a versatile programming language with rich libraries and frameworks, making it ideal for automation tasks.
- Page Object Model (POM): POM is a design pattern used to create an object repository of mobile elements. It promotes code reusability and enhances test maintenance.

## Project Structure

The project is structured into three main directories:

- **infra**: Contains infrastructure-related code, such as configuration files, drivers, or any setup required for testing with Appium.
- **logic**: Consists of the core logic of the application, including page objects, utilities, and helpers.
- **test**: Houses the test scripts responsible for simulating user interactions and verifying functionality.

## Test Scenarios

The tests cover the main operations of the calculator app, including addition, subtraction, multiplication, and division. Each operation is tested for accuracy and responsiveness.

## Running Tests

Ensure you have set up your Appium environment and configured the necessary parameters in the `infra` directory.
