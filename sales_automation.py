"""
Process & Sales Automation (Python RPA)

Automates the daily workflow:
1. Accesses cloud storage (Google Drive) to download the daily sales dataset;
2. Processes and calculates key business metrics (Revenue & Quantity Sold) with Pandas;
3. Drafts and dispatches an executive summary report via email (Gmail).

Security & Best Practices:
- Sensitive parameters (email, drive link, file paths) are managed via
  environment variables (.env) to prevent credential leakage.
"""

import os
import time
from pathlib import Path
import pandas as pd
import pyautogui
import pyperclip
from dotenv import load_dotenv

# ==============================================================================
# SECURITY PROTOCOL & ENVIRONMENT CONFIGURATION
# ==============================================================================
# Load environment variables from local .env file (if present)
PROJECT_DIR = Path(__file__).parent.resolve()
load_dotenv(PROJECT_DIR / ".env")

# Safety configuration for PyAutoGUI
pyautogui.PAUSE = 1.0  # 1-second pause between commands to guarantee UI stability

# Parameters retrieved safely from environment variables (with safe defaults)
DRIVE_URL = os.getenv("DRIVE_URL", "https://drive.google.com/drive/folders/your_folder_id")
RECIPIENT_EMAIL = os.getenv("RECIPIENT_EMAIL", "management@example.com")
SENDER_NAME = os.getenv("SENDER_NAME", "Operations Analyst")

# Data path is strictly relative to the project directory
DATA_REL_PATH = os.getenv("DATA_PATH", "data/Vendas - Dez.xlsx")
DATASET_PATH = PROJECT_DIR / DATA_REL_PATH


def validate_dataset_path() -> Path:
    """Validates that the dataset exists within the project directory."""
    if not DATASET_PATH.exists():
        raise FileNotFoundError(
            f"Dataset not found at expected location: {DATASET_PATH}.\n"
            f"Please verify that the file exists in the project 'data/' directory."
        )
    return DATASET_PATH


# ==============================================================================
# AUTOMATION WORKFLOW
# ==============================================================================
def download_drive_report(drive_url: str) -> None:
    """
    Launches Chrome and downloads the latest sales file from Google Drive.
    NOTE: Screen click coordinates are calibrated to a specific desktop resolution.
    """
    print("[1/3] Accessing cloud system and downloading dataset...")
    pyautogui.press("win")
    pyautogui.write("chrome")
    pyautogui.press("enter")
    time.sleep(2)

    # Click browser focus if needed
    pyautogui.click(x=684, y=509)
    time.sleep(0.5)

    # Navigate to Drive URL
    pyautogui.write(drive_url)
    pyautogui.press("enter")
    time.sleep(3)

    # Drive UI Navigation to trigger download
    pyautogui.click(x=318, y=321, clicks=2)
    time.sleep(1)
    pyautogui.click(x=321, y=331)  # Select file
    time.sleep(0.5)
    pyautogui.click(x=553, y=243)  # More options menu (3 dots)
    time.sleep(0.5)
    pyautogui.click(x=586, y=317)  # Download action
    time.sleep(5)  # Wait for file download completion


def calculate_kpis(file_path: Path) -> tuple[float, int]:
    """
    Reads the Excel sales dataset and aggregates core business KPIs:
    - Total Revenue (sum of 'Valor Final' column)
    - Total Units Sold (sum of 'Quantidade' column)
    """
    print(f"[2/3] Processing sales dataset: {file_path.name}...")
    df = pd.read_excel(file_path)

    total_revenue = float(df["Valor Final"].sum())
    total_quantity = int(df["Quantidade"].sum())

    print(f"      - Total Revenue: ${total_revenue:,.2f}")
    print(f"      - Units Sold:    {total_quantity:,}")

    return total_revenue, total_quantity


def send_gmail_report(recipient: str, total_revenue: float, total_quantity: int) -> None:
    """
    Opens Gmail in the browser and sends the daily summary report.
    """
    print(f"[3/3] Sending executive summary via Gmail to {recipient}...")
    pyautogui.hotkey("ctrl", "t")  # Open new browser tab
    pyautogui.write("https://mail.google.com/")
    pyautogui.press("enter")
    time.sleep(3)

    # Click Compose button
    pyautogui.click(x=63, y=216)
    time.sleep(1)

    # Fill recipient
    pyautogui.write(recipient)
    pyautogui.press("tab")
    pyautogui.press("tab")

    # Subject line
    pyperclip.copy("Daily Sales Report - Summary")
    pyautogui.hotkey("ctrl", "v")
    pyautogui.press("tab")

    # Email message body
    email_body = f"""Dear Management,

Please find below the consolidated daily sales report:

- Total Revenue: ${total_revenue:,.2f}
- Total Units Sold: {total_quantity:,}

Please let me know if you need any additional insights.

Best regards,
{SENDER_NAME}
"""
    pyperclip.copy(email_body)
    pyautogui.hotkey("ctrl", "v")
    time.sleep(0.5)

    # Click Send button
    pyautogui.click(x=1005, y=1021)
    print("Success! Report email dispatched.")


def calibrate_coordinates() -> None:
    """
    Helper function to inspect mouse cursor coordinates on screen.
    Run this utility if you need to recalibrate UI coordinates for different screen resolutions.
    """
    print("Move your mouse to the target UI element. Capturing in 5 seconds...")
    time.sleep(5)
    print(f"Current cursor position: {pyautogui.position()}")


def main():
    print("=" * 60)
    print("STARTING SALES PROCESS AUTOMATION (RPA)")
    print("=" * 60)

    # 1. Download report (Uncomment to execute live Drive download flow)
    # download_drive_report(DRIVE_URL)

    # 2. Validate and compute KPIs
    data_path = validate_dataset_path()
    revenue, quantity = calculate_kpis(data_path)

    # 3. Send report via email (Uncomment to dispatch email via Gmail web)
    # send_gmail_report(RECIPIENT_EMAIL, revenue, quantity)

    print("\nWorkflow completed successfully!")


if __name__ == "__main__":
    main()
