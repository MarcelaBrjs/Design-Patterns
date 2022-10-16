import abc
from array import array
from patterns.web_report import WebReport
from patterns.print_report import PrintReport
from patterns.report_generator import ReportGenerator

# Open Close: Nuevos tipos de reportes se pueden agregar sin necesidad de modificar el código existente.
# Simple Factory Design Pattern
def get_report(rides: array, report_type: str):
    if report_type == "web":
        ReportGenerator.report("financial-report.html", WebReport.format_content(rides))

    elif report_type == "text":
        ReportGenerator.report("financial-report.txt", PrintReport.format_content(rides))

    else:
        raise Exception("Tipo de reporte desconocido")