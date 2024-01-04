#!"C:/xampp/perl/bin/perl.exe"
use strict;
use warnings;
use CGI;
use utf8;

open(IN, "ProgramasdeUniversidades.csv") or die("Error: No se pudo leer el archivo");
my @arr = <IN>;
close(IN);

binmode STDOUT, ":utf8";

my $q = CGI->new;
my $kind = $q->param("kind");
my $keyword = $q->param("keyword");

print $q->header(-type => "text/html", -charset => "UTF-8");
print<<HTML;
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="stylesheet" href="css/style.css">
    <title>Resultados de la Búsqueda</title>
    <style>
      body{
        margin: 0;
        background-image: url(../Images/background.jpg);
        background-size: auto 100%; 
        background-position: center; 
        height: 100vh;
      }
      h2{
        font-family: 'Franklin Gothic Medium', 'Arial Narrow', Arial, sans-serif;
        margin: 0;
        font-size: 24px;
      }
      section{
        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: center;
        background-color: rgba(255, 146, 79, 0.94);
        border: solid 5px rgba(255, 55, 0, 0.8);
        padding: 20px;
      }
      table{
        width: 100%;
        border-collapse: collapse;
        margin-top: 20px;
      }
      th, td{
        border: 1px solid black;
        padding: 10px;
        text-align: left;
      }
    </style>
</head>
<body>
  <section>
HTML

my @matchedResults = search($kind, $keyword, \@arr);

print "<h2>Resultados de la Búsqueda</h2>";

if (@matchedResults) {
    print "<table>";
    print "<tr>
            <th>Codigo de entidad</th>
            <th>Nombre</th>
            <th>Tipo de Gestion</th>
            <th>Periodo de licenciamiento</th>
            <th>Departamento local</th>
            <th>Denominación del programa</th>
            <th>Programa</th>
          </tr>";

    foreach my $result (@matchedResults) {
        print "<tr>";
        foreach my $value (@$result) {
            print "<td>$value</td>";
        }
        print "</tr>";
    }

    print "</table>";
} else {
    print "<p>No se encontraron resultados.</p>";
}

print <<HTML;
  </section>
</body>
</html>
HTML

sub search {
  my $kind = $_[0];
  my $keyword = lc($_[1]); 
  my $arrayRef = $_[2];
  my @array = @$arrayRef;
  my $size = readHeader(@array);
  my $pattern = generateRegExp($size);

  my @matchedResults;

  foreach my $line (@array) {
    utf8::decode($line);  
    if($line =~ /$pattern/) {
      my @items = map { trim($_) } ($1, $2, $3, $5, $11, fixDenominacion($7), $17);
      my $item = lc(kindSearch($kind, \@items));

      if(index($item, $keyword) != -1) {
        push @matchedResults, \@items;
      }
    }
  }

  return @matchedResults;
}

sub kindSearch {
  my $itemsRef = $_[1];
  my @items = @$itemsRef;
  my $kind = $_[0];

  if($kind eq "nombreUniversidad") {
    return $items[1];
  }
  if($kind eq "periodoLicenciamiento") {
    return $items[3];
  }
  if($kind eq "departamentoLocal") {
    return $items[4];
  }
  if($kind eq "denominacionPrograma") {
    return $items[5];
  }
}

sub readHeader {
  my $line = $_[0];
  my $count = 1;
  while($line =~ /^([^\|]+)\|(.+)/) {
    $count++;
    $line = $2;
  }
  return $count;
}

sub generateRegExp {
  my $n = $_[0];
  my $exp = "^";
  for(my $i = 0; $i < $n - 1; $i++) {
    $exp .= '([^\|]+)\|';
  }
  $exp .= "([^\|]+)";
  return $exp;
}

sub trim {
  my $string = shift;
  $string =~ s/^\s+|\s+$//g;
  return $string;
}

sub fixDenominacion {
  my $denominacion = shift;
  return $denominacion;
}