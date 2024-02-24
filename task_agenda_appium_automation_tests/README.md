# Automated Testing for Task Agenda App

This project aims to automate tests for the Task Agenda app using Appium and Python. The tests are structured following the Page Object Model (POM) design pattern, enhancing maintainability and reusability. Appium Inspector is used to locate elements within the app.

## Overview

The Task Agenda app is a productivity tool for managing tasks, schedules, and reminders. Automated testing ensures its functionality remains intact across various features and interactions.

## Tools and Technologies

- Appium: Appium is an open-source tool for automating mobile applications. It supports multiple platforms (iOS, Android) and provides a unified API for both native and hybrid mobile apps.
- Python: Python is a versatile programming language with rich libraries and frameworks, making it ideal for automation tasks.
- Page Object Model (POM): POM is a design pattern used to create an object repository of mobile elements. It promotes code reusability and enhances test maintenance.
- Appium Inspector: Appium Inspector is a tool that helps inspect elements within the app and generate locators for automation scripts.

## Project Structure

The project is structured into three main directories:

- **infra**: Contains infrastructure-related code, such as configuration files, drivers, or any setup required for testing with Appium.
- **logic**: Consists of the core logic of the application, including page objects, utilities, and helpers.
- **test**: Houses the test scripts responsible for simulating user interactions and verifying functionality.

## Test Scenarios

The tests cover various scenarios and interactions within the Task Agenda app, including creating tasks,  managing schedules, and navigating through different sections.

## Running Tests

Ensure you have set up your Appium environment and configured the necessary parameters in the `infra` directory.

