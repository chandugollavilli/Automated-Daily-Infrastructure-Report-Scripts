# Daily Infrastructure Report: Report Templates Design

## 1. Introduction

This document outlines the design specifications for the daily infrastructure reports, which will be generated in both PDF and Excel formats. The goal is to ensure consistency, clarity, and comprehensiveness in the presentation of critical infrastructure metrics to the system administration team.

## 2. PDF Report Template Design

The PDF report is intended for quick viewing and high-level summaries. It will prioritize readability and a clean, professional appearance.

### 2.1. General Layout

*   **Header:**
    *   Title: "Daily Infrastructure Report"
    *   Date and Time of Report Generation (e.g., YYYY-MM-DD HH:MM:SS)
*   **Body:** Divided into sections for each metric.
*   **Footer:** Page number (e.g., "Page X of Y").

### 2.2. Section Breakdown

#### 2.2.1. Running Servers

*   **Title:** "1. Running Servers"
*   **Content:**
    *   Total count of running servers.
    *   A list of hostnames for all running servers.

#### 2.2.2. Disk Usage per Host

*   **Title:** "2. Disk Usage per Host"
*   **Content:**
    *   For each monitored host:
        *   Hostname.
        *   A table summarizing disk usage for each mounted filesystem:
            *   **Headers:** Filesystem, Size, Used, Avail, Use%, Mounted On.
            *   **Data:** Corresponding values for each disk.

#### 2.2.3. User Logins

*   **Title:** "3. User Logins"
*   **Content:**
    *   For each monitored host:
        *   Hostname.
        *   Summary of successful login attempts.
        *   Summary of failed login attempts.
        *   A table listing recent login attempts:
            *   **Headers:** Timestamp, Username, Source IP, Status.
            *   **Data:** Details for each login event.

#### 2.2.4. System Uptime

*   **Title:** "4. System Uptime"
*   **Content:**
    *   For each monitored host:
        *   Hostname.
        *   Current system uptime (e.g., "up X days, Y hours, Z minutes").

### 2.3. Styling and Formatting

*   **Fonts:** Arial (or similar sans-serif font) for readability.
*   **Font Sizes:** Titles (12pt bold), Section Titles (12pt bold), Body Text (10pt regular), Table Headers (10pt bold), Table Data (8pt regular).
*   **Alignment:** Titles centered, section titles left-aligned, body text justified, table content centered.
*   **Spacing:** Adequate line spacing and margins for visual comfort.
*   **Page Breaks:** Intelligent page breaks to ensure tables and sections are not awkwardly split.

## 3. Excel Report Template Design

The Excel report is designed for detailed data analysis, allowing administrators to filter, sort, and manipulate data as needed. Each major data category will reside on a separate worksheet.

### 3.1. Workbook Structure

*   **Sheet 1: "Running Servers"**
*   **Sheet 2: "Disk Usage"**
*   **Sheet 3: "User Logins"**
*   **Sheet 4: "System Uptime"**

### 3.2. Worksheet Breakdown

#### 3.2.1. "Running Servers" Sheet

*   **Columns:**
    *   A: Metric
    *   B: Value
*   **Content:**
    *   Row 1: "Total Running Servers", [Count]
    *   Row 2: "Running Server Hostnames"
    *   Subsequent Rows: Individual server hostnames.

#### 3.2.2. "Disk Usage" Sheet

*   **Columns:**
    *   A: Host
    *   B: Filesystem
    *   C: Size
    *   D: Used
    *   E: Avail
    *   F: Use%
    *   G: Mounted On
*   **Content:** Tabular data with one row per filesystem per host.

#### 3.2.3. "User Logins" Sheet

*   **Columns:**
    *   A: Host
    *   B: Timestamp
    *   C: Username
    *   D: Source IP
    *   E: Status (Success/Failed)
*   **Content:** Tabular data with one row per login event per host.

#### 3.2.4. "System Uptime" Sheet

*   **Columns:**
    *   A: Host
    *   B: Uptime
*   **Content:** Tabular data with one row per host, showing its uptime string.

### 3.3. Styling and Formatting

*   **Headers:** Bold text, potentially with a background fill for clarity.
*   **Data:** Standard text formatting.
*   **Column Widths:** Auto-fit to content for optimal readability.
*   **Filtering:** Ensure data is in a format suitable for Excel's built-in filtering and sorting capabilities.

## 4. Conclusion

These template designs aim to provide clear, actionable, and easily digestible information to the system administration team. The dual format (PDF for summary, Excel for detail) caters to different analytical needs, ensuring maximum utility of the generated reports.


