from patterns import csv_utils
from patterns import report

CSV_FILE = "taxi-data.csv"

def main():
    rides = csv_utils.parse_file(CSV_FILE)
    report.get_report(rides, "web")
    report.get_report(rides, "text")

if __name__ == '__main__':
    main()
