# Solid Principles
1. Single Responsability
    - Su única responsabilidad es generar el reporte.
    https://github.com/MarcelaBrjs/Design-Patterns/blob/97e8488984f7eeaad40ea39146960953da803657/src/patterns/report_generator.py#L3
      
    - Su única responsabilidad es dar formato al contenido del reporte impreso.
    https://github.com/MarcelaBrjs/Design-Patterns/blob/97e8488984f7eeaad40ea39146960953da803657/src/patterns/print_report.py#L8
    
    - Su única responsabilidad es dar formato al contenido del reporte web.
    https://github.com/MarcelaBrjs/Design-Patterns/blob/97e8488984f7eeaad40ea39146960953da803657/src/patterns/web_report.py#L6
    
2. Open Close
    - Nuevos tipos de reportes se pueden agregar sin necesidad de modificar el código existente.
    https://github.com/MarcelaBrjs/Design-Patterns/blob/97e8488984f7eeaad40ea39146960953da803657/src/patterns/report.py#L9
    
3. Dependency Inversion
    - Report no depende del tipo de reporte ni del formato de este.
    https://github.com/MarcelaBrjs/Design-Patterns/blob/97e8488984f7eeaad40ea39146960953da803657/src/patterns/report_generator.py#L7

# Building the Project Locally
Install VirtualEnvironment (one time)

    >python -m pip install virtualenv

Create virtual environment

    >virtualenv virtual_project

1. This will create a virtual environment project folder and install python there.
2. This step can be skipped if you already have the folder locally.

Open virtual environment (Unix type OS)

    >source virtual_project/bin/activate

1. This will activate the virtual environment.  Yous should see `(virtual_project)` to the left of the terminal prompt.
2. This step will be needed each time.

Install requirements
    
    >python -m pip install -r requirements.txt

Install local src/ folder

    >python -m pip install -e src 

# Building Docker Image
At the root of the project run

    >docker image build -t YOUR_NAME .

This will create a docker image using the `Dockerfile` with the image name `YOUR_NAME`

Run container

    >docker run YOUR_NAME
