# Binderlabs API Security Simulator (BASS-Env)

Binderlabs API Security Simulator (**BASS-Env**) is a deliberately vulnerable API environment designed to be susceptible to the **OWASP Top 10 API Security Risks – 2023**. It serves as a practice ground for cybersecurity professionals to enhance their **API hacking skills** and deepen their knowledge in **API security testing**.

## Installation

### Prerequisites

Ensure you have the following installed on your system:

- **PHP**
- **MySQL**
- **Postman Client**

### Setup Instructions

#### 1. Clone the repository:

```sh
git clone https://github.com/JeffreyGaor/Binderapis_scanner.git
cd Binderapis_scanner
```

#### 2. Create MySQL Database:

Login into MySQL and create the required database:

```sh
mysql -u root -p -e "CREATE DATABASE bass;"
```

#### 3. Import the Database:

```sh
cd BASS/database
mysql -u [username] -p [database_name] < bass.sql
```

#### 4. Start the PHP Server (Laravel):

```sh
cd BASS/BASS_Env
php artisan serve --host={{hostip}} --port=8000
```

---

# Binderlabs API Security Scanner (BASS-Scanner)

**BASS-Scanner** is a tool designed to aid cybersecurity professionals in **API security testing**. It automates the identification of security flaws, particularly those related to the **OWASP Top 10 API Security Risks**, reducing the time required for penetration testing engagements.

## Requirements

### Install the dependencies with:

```sh
git clone https://github.com/JeffreyGaor/Binderapis_scanner.git
cd BASS/BASS_Scanner
pip3 install -r requirements.txt
```

- **Chrome Browser** (for detecting SSRF attacks)

---

## Features

### 🔍 **Fuzz Testing**

- **Dynamic Fuzzing**: Automatically generates and sends a variety of malformed and unexpected data to API endpoints to identify vulnerabilities and unexpected behavior.

### 🛡 **Security Risk Detection**

- **OWASP Top 10 Coverage**: Performs automated scans to detect and report on security issues outlined in the OWASP Top 10 API Security Risks.
- **Injection Detection**: Identifies potential vulnerabilities such as **SQL injection, NoSQL injection, and command injection**.

### 🔑 **Authentication & Authorization Testing**

- **Token Analysis**: Evaluates the strength of authentication tokens and identifies potential weaknesses in token handling mechanisms.
- **Access Control Checks**: Analyzes API endpoints to ensure proper access controls are in place, preventing unauthorized access.

---

## 🚧 Usage

Under construction…

---

## 📚 References
