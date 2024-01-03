#!"C:/xampp/perl/bin/perl.exe"
use CGI;
use Text::CSV;

my $cgi = CGI->new;

my $nombreUnivesidad    = $cgi->param('Nombre_Universidad');
my $periodoLicenciamiento   = $cgi->param('Periodo_Licenciamiento');
my $departamentoLocal     = $cgi->param('Departamento_Local');
my $denominacionPrograma     = $cgi->param('Denominación_Programa');

print "Content-type: text/html\n\n";
print <<HTML;
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="stylesheet" href="css/style.css">
    <title>Resultado de la Consulta</title>
    <style>
        body {
            margin: 0;
            background-image: url(../Images/background.jpg);
            background-size: auto 100%;
            background-position: center;
            height: 100vh;
        }
        h1, h2 {
            font-family: 'Franklin Gothic Medium', 'Arial Narrow', Arial, sans-serif;
            margin: 0;
        }
        h1 {
            font-size: 30px;
            font-family: 'Courier New', Courier, monospace;
        }
        h2 {
            font-size: 24px;
        }
        section {
            display: flex;
            flex-direction: column;
            align-items: center;
            justify-content: center;
        }
        div{
            display: flex;
            flex-direction: column;
            align-items: start;
            justify-content: center;
            width: 1300px;
            background-color: rgba(255, 146, 79, 0.94);
            border: solid 5px rgba(255, 55, 0, 0.8);
        }
        p {
            font-size: 20px;
            margin: 5px 0;
        }
        .titulo{
            display: flex;
            align-items: center;
            border: solid 1px rgba(255, 55, 0, 0.8);
        }
    </style>
</head>
<body>
    <section>
        <div>
            <div class = "titulo"><h1>Resultados de la Consulta</h1></div>
            <p>Nombre de la Universidad: $nombreUnivesidad</p>
            <p>Periodo de Licenciamiento: $periodoLicenciamiento</p>
            <p>Departamento Local: $departamentoLocal</p>
            <p>Denominación del programa: $denominacionPrograma</p>
        </div>
    </section>
</body>
</html>
HTML