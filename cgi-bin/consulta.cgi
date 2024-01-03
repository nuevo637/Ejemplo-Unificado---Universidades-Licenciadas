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
</head>
<body>
    <section>
        <h1>Resultados de la Consulta</h1>
        <p>Nombre de la Universidad: $nombreUnivesidad</p>
        <p>Periodo de Licenciamiento: $periodoLicenciamiento</p>
        <p>Departamento Local: $departamentoLocal</p>
        <p>Denominación del programa: $denominacionPrograma</p>
    </section>
</body>
</html>
HTML