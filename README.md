# AsyncIO HTTP Server

## Project Overview

This project is a simple HTTP server built using Python's AsyncIO library, developed as part of a school assignment at the University of Malawi. The server handles HTTP client requests asynchronously, serving HTML templates and processing form submissions. It demonstrates the use of asynchronous programming in Python to manage concurrent client connections efficiently.

The server:

- Serves an `index.html` page when accessed at `http://localhost:8085/`.
- Serves a `register.html` form at `http://localhost:8085/register`.
- Handles form submissions via POST requests to `/submit`, capturing username and email fields and saving them to a `db.txt` file in the format `username email_address` per line.
- Supports serving static assets (e.g., images) from an `assets/` directory.
- Returns a 404 error for unrecognized paths.

## Prerequisites

To run this project, you need:

- Python 3.7 or higher
- No external dependencies are required, as the project uses Python's standard library (`asyncio` and `urllib.parse`).

## Installation

1. **Clone the Repository:**
   ```bash
   git clone https://github.com/your-username/asyncio-http-server.git
   cd asyncio-http-server
   ```

2. **Project Structure:**
   Ensure the following files and directories are present:
   ```
   asyncio-http-server/
   ├── templates/
   │   ├── index.html
   │   ├── register.html
   ├── assets/ (optional, for static files like images)
   ├── db.txt (created automatically on form submission)
   ├── server.py
   └── README.md
   ```

3. **Create HTML Templates:**
   Create a `templates/` directory and add the following files:

   **index.html:** A simple homepage. Example:
   ```html
   <!DOCTYPE html>
   <html>
   <head><title>Welcome</title></head>
   <body><h1>Welcome to the AsyncIO Server</h1></body>
   </html>
   ```

   **register.html:** A form with username and email fields, submitting to `/submit`. Example:
   ```html
   <!DOCTYPE html>
   <html>
   <head><title>Register</title></head>
   <body>
     <h1>Register</h1>
     <form method="POST" action="/submit">
       <label>Username: <input type="text" name="username"></label><br>
       <label>Email: <input type="text" name="email"></label><br>
       <input type="submit" value="Submit">
     </form>
   </body>
   </html>
   ```

## Usage

1. **Run the Server:**
   ```bash
   python server.py
   ```

   The server will start on `http://localhost:8085`. You will see a message like:
   ```
   server running on ('localhost', 8085)
   ```

2. **Access the Server:**

   Open a web browser and navigate to:
   - `http://localhost:8085/` to view the homepage.
   - `http://localhost:8085/register` to view the registration form.

   Submit the form on the `/register` page to send a POST request to `/submit`. The server will write the username and email to `db.txt` and display a success message.

3. **View Form Data:**

   Check the `db.txt` file in the project root to see the submitted data in the format:
   ```
   username email_address
   ```

4. **Serve Static Assets (Optional):**

   Place image files in an `assets/` directory.
   Access them via `http://localhost:8085/assets/filename.jpg`.

## Notes

- The server currently overwrites `db.txt` with each new form submission. To append new entries, modify the code to use append mode.
- The server assumes `content_type='image/jpeg'` for assets. Additional content types (e.g., PNG, CSS) can be supported with code changes.
- Basic error handling ensures connections close gracefully on exceptions.

## Acknowledgments

Special thanks to my lecturer, [Ramsey Ith Njema II](https://github.com/rnjema), for providing guidance and instruction during the course at the University of Malawi, which made this project possible.

Inspired by Python's official asyncio documentation.

## License

This project is licensed under the MIT License. See the LICENSE file for details.
