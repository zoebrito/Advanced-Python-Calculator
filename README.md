# Advanced Python Calculator

This project is an advanced Python-based calculator application developed as a midterm assignment for a Software Engineering graduate course. The calculator integrates various professional software development practices, including clean and maintainable code, design patterns, logging, dynamic configuration via environment variables, data handling with Pandas, and a command-line interface for real-time user interaction.

## Setup Instructions

To run the calculator application locally, follow these steps:

1. Clone the repository to your local machine.
2. Ensure you have Python 3.x installed.
3. Install the required dependencies by running `pip install -r requirements.txt`.
4. Create a `.env` file in the root directory and configure the necessary environment variables (see `.env` for reference).
5. Run the application by executing `python3 main.py` in your terminal.

## Usage Examples

Once the application is running, you can interact with the calculator using the command-line interface. Here are some usage examples:

- To perform addition: `add 5 3`
- To perform subtraction: `subtract 10 7`
- To perform multiplication: `multiply 4 6`
- To perform division: `divide 20 4`
- To view calculation history: `history`
- To clear calculation history: `clear`
- To exit the application: `exit`

## Design Patterns

The project utilizes several design patterns to ensure modular, scalable, and maintainable code. These include:

- **Singleton Pattern**: Implemented for the `CommandHandler` class to ensure there's only one instance of the command handler throughout the application's lifecycle.
[Link to implementation.](https://github.com/zoebrito/midterm/blob/pandas/command_handler.py)

- **Factory Pattern**: Used for dynamic plugin loading and command registration in the `CommandHandler` class, allowing for easy extension of functionality. 
[Link to implementation.](https://github.com/zoebrito/midterm/blob/pandas/plugins/calculator_plugin.py)

## Environment Variables

The application supports dynamic configuration via environment variables. Environment variables are loaded from a `.env` file using the `python-dotenv` library. Configuration options include logging level, log file path, and other application-specific settings. 
[Link to configuration example.](https://github.com/zoebrito/midterm/blob/pandas/.env)

## Logging

Logging is an essential aspect of the application for tracking events, errors, and user interactions. It's configured to log messages to both the console and a log file. Logging levels can be dynamically configured via environment variables, with default settings ensuring informative and actionable logs. 
[Link to logging implementation.](https://github.com/zoebrito/midterm/blob/pandas/app/app.py)

## Error Handling

The project adopts both "Look Before You Leap" (LBYL) and "Easier to Ask for Forgiveness than Permission" (EAFP) error handling approaches using try/except blocks.

- LBYL: Used to validate user input before performing calculations, ensuring that only valid input is processed. 
[Link to LBYL implementation.](https://github.com/zoebrito/midterm/blob/pandas/app/app.py)

- EAFP: Employed for handling file operations, configuration loading, and other runtime errors, allowing the application to gracefully recover from unexpected situations. 
[Link to EAFP implementation.](https://github.com/zoebrito/midterm/blob/pandas/history_manager.py)
