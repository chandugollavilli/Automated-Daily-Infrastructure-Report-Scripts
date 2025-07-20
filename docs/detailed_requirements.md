# Daily Infrastructure Report Project: Detailed Requirements

## 1. Introduction

This document provides a detailed breakdown of the functional and non-functional requirements for the Daily Infrastructure Report Project. These requirements will guide the development and implementation phases, ensuring that the final solution meets the organization's needs for automated infrastructure reporting.

## 2. Functional Requirements

### 2.1. Data Collection Requirements

#### 2.1.1. Number of Running Servers

*   **FR-DC-001:** The system SHALL collect the total number of running servers within the defined infrastructure scope daily.
*   **FR-DC-002:** The system SHALL identify and count servers based on their operational status (e.g., 'running', 'active').
*   **FR-DC-003:** The data collection mechanism SHALL be compatible with the organization's existing server management platforms (e.g., VMware vSphere, AWS EC2, physical servers accessible via SSH).
*   **FR-DC-004:** The collected data SHALL include the server hostname or IP address for identification purposes.

#### 2.1.2. Disk Usage Per Host

*   **FR-DC-005:** The system SHALL collect disk usage statistics for each host daily.
*   **FR-DC-006:** For each host, the system SHALL report the total disk space, used disk space, and available disk space for all mounted filesystems.
*   **FR-DC-007:** The system SHALL be able to collect disk usage from various operating systems (e.g., Linux, Windows).
*   **FR-DC-008:** The data SHALL be presented in a human-readable format (e.g., GB, TB) and include percentage utilization.

#### 2.1.3. User Logins from `/var/log/secure`

*   **FR-DC-009:** The system SHALL parse the `/var/log/secure` file (or equivalent for non-Linux systems) on each relevant server daily to extract user login information.
*   **FR-DC-010:** The system SHALL identify successful and failed login attempts.
*   **FR-DC-011:** The collected data SHALL include the timestamp of the login attempt, username, source IP address, and login status (success/failure).
*   **FR-DC-012:** The system SHALL handle log rotation and ensure all relevant log entries from the previous 24 hours are processed.

#### 2.1.4. System Uptime

*   **FR-DC-013:** The system SHALL collect the uptime for each server daily.
*   **FR-DC-014:** Uptime SHALL be reported in a clear, human-readable format (e.g., days, hours, minutes).

### 2.2. Report Generation Requirements

#### 2.2.1. Report Formats

*   **FR-RG-001:** The system SHALL generate daily reports in both PDF and Excel formats.
*   **FR-RG-002:** The PDF report SHALL be suitable for quick viewing and printing, providing a high-level summary.
*   **FR-RG-003:** The Excel report SHALL provide detailed, tabular data that can be easily filtered, sorted, and used for further analysis.

#### 2.2.2. Report Content

*   **FR-RG-004:** The report SHALL include a summary section for each collected metric (running servers, disk usage, user logins, system uptime).
*   **FR-RG-005:** The report SHALL clearly indicate the date and time of data collection.
*   **FR-RG-006:** Disk usage section SHALL highlight hosts with high disk utilization (e.g., >80%).
*   **FR-RG-007:** User login section SHALL summarize successful and failed login attempts, potentially highlighting unusual activity.
*   **FR-RG-008:** The report SHALL be visually appealing and easy to read, using appropriate formatting, charts (where applicable), and tables.

### 2.3. Report Distribution Requirements

*   **FR-RD-001:** The system SHALL automatically email the generated PDF and Excel reports to a predefined system administration group every morning.
*   **FR-RD-002:** The email SHALL have a clear subject line indicating the report type and date.
*   **FR-RD-003:** The email body SHALL include a brief summary or introduction to the attached reports.
*   **FR-RD-004:** The system SHALL support standard email protocols (e.g., SMTP) for sending emails.

## 3. Non-Functional Requirements

### 3.1. Performance Requirements

*   **NFR-PERF-001:** Data collection and report generation SHALL be completed within a reasonable timeframe (e.g., within 30 minutes) to ensure timely delivery of reports.
*   **NFR-PERF-002:** The system SHALL not significantly impact the performance of the monitored servers during data collection.

### 3.2. Security Requirements

*   **NFR-SEC-001:** All credentials used for accessing servers (e.g., SSH keys) SHALL be stored securely and encrypted.
*   **NFR-SEC-002:** The system SHALL use secure communication protocols (e.g., SSH, HTTPS) for data transfer.
*   **NFR-SEC-003:** Access to the report generation system and generated reports SHALL be restricted to authorized personnel.

### 3.3. Reliability and Availability Requirements

*   **NFR-REL-001:** The data collection and report generation processes SHALL be highly reliable, with minimal failures.
*   **NFR-REL-002:** The system SHALL include error handling mechanisms to gracefully manage issues during data collection or report generation.
*   **NFR-REL-003:** In case of failure, the system SHALL log errors and notify administrators.

### 3.4. Maintainability Requirements

*   **NFR-MAINT-001:** The codebase SHALL be well-structured, modular, and easy to understand.
*   **NFR-MAINT-002:** The system SHALL be configurable, allowing easy modification of server lists, report recipients, and thresholds.
*   **NFR-MAINT-003:** Comprehensive documentation SHALL be provided to facilitate future maintenance and enhancements.

### 3.5. Scalability Requirements

*   **NFR-SCAL-001:** The system SHALL be designed to accommodate an increasing number of monitored servers without significant degradation in performance.

## 4. Environmental Requirements

*   **ENV-001:** The system SHALL operate on a Linux-based server environment.
*   **ENV-002:** Required software dependencies (e.g., Python, necessary libraries) SHALL be clearly documented and easily installable.

## 5. User Interface Requirements (N/A)

This project does not involve a graphical user interface for end-users. Interaction will primarily be through automated processes and email distribution.

## 6. Conclusion

These detailed requirements provide a clear foundation for the development of the Daily Infrastructure Report Project. Adherence to these specifications will ensure the delivery of a robust, secure, and efficient reporting solution that meets the organization's operational needs.


