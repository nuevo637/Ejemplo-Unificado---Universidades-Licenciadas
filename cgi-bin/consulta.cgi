#!"C:/xampp/perl/bin/perl.exe"
use CGI;
use Text::CSV;
use utf8;
my $cgi = CGI->new;

my $nombreUnivesidad = $cgi->param('Nombre_Universidad');
my $periodoLicenciamiento = $cgi->param('Periodo_Licenciamiento');
my $departamentoLocal = $cgi->param('Departamento_Local');
my $denominacionPrograma = $cgi->param('Denominación_Programa');

utf8::decode($nombreUnivesidad);
utf8::decode($periodoLicenciamiento);
utf8::decode($departamentoLocal);
utf8::decode($denominacionPrograma);

my $archivo = 'bd\Programas de Universidades.csv';
open my $fh, '<', $archivo;

my $csv = Text::CSV->new({ binary => 1, sep_char => '|' });

my $tableKey = "";
if (my $fila = $csv->getline($fh)) {
    for my $valor (@$fila) {
        $tableKey .= "<th>$valor</th>\n";
    }
}

my $tableValues = "";
my $coincidencias1 = 0;
my $coincidencias2 = 0;
my $coincidencias3 = 0;
my $coincidencias4 = 0;
my $coincidenciasTotales = 0;

while (my $fila = $csv->getline($fh)) {
    if (($fila->[1] eq $nombreUni ) && ($fila->[4] eq $periodoLic ) &&($fila->[10] eq $depLocal ) &&($fila->[16] eq $denoProg )) {
        $tableValues .= "<tr>";
        for my $valor (@$fila) {
            $tableValues .= "<td>$valor</td>\n";
        }
        $tableValues .= "</tr>";
        $coincidenciasTotales++;
    }
    if ($fila->[1] eq $nombreUnivesidad) {
        $coincidencias1++;
    }
    if ($fila->[4] eq $periodoLicenciamiento){
        $coincidencias2++;
    }
    if ($fila->[10] eq $departamentoLocal) {
        $coincidencias3++;
    }
    if ($fila->[16] eq $denominacionPrograma){
        $coincidencias4++;
    }
}
if($coincidenciasTotales == 0){
    $coincidenciasTotales = "No existen valores que cumplan con los campos"
}else{
    $coincidenciasTotales = "Existen $coincidenciasTotales coincidencias de todos los campos"
}

close $fh;

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
            <div class = "titulo"><h1>Coincidencias Halladas</h1></div>
	    <p>Coincidencias Totales: $coincidenciasTotales</p>
            <p>Nombre de la Universidad: $nombreUnivesidad -> Se encontraron $coincidencias1 coincidencias </p>
            <p>Periodo de Licenciamiento: $periodoLicenciamiento- > Se encontraron $coincidencias2 coincidencias </p>
            <p>Departamento Local: $departamentoLocal -> Se encontraron $coincidencias3 coincidencias </p>
            <p>Denominación del programa: $denominacionPrograma -> Se encontraron $coincidencias4 coincidencias </p>
        </div>
    </section>
</body>
</html>
HTML