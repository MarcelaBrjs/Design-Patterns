# Single Responsability
# Su única responsabilidad es generar el reporte.
class ReportGenerator:

    # Dependency Inversion
    # Report no depende del tipo de reporte ni del formato de este.
    def report(fileName, content):
        with open(fileName, "w") as file:
            file.write(content)