
close $fh;

print $cgi->header('text/html');

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
            width: auto;
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
        table {
            border-collapse: collapse;
            width: 100%;

        }

        table, th, td {
            border: 0.4rem solid yellow;
            box-shadow: 10px 10px 10px rgba(0, 0, 0, 0.3);
        }
        tr:nth-child(1) {
            color: black;
            background-color: orange;
        }
        tr:not(:first-child) {
            color: yellow;
            font-weight: bold;
        } 
        th, td {
            padding: 0.7rem;
            text-align: center;
        }
        table tr{
            font-size: 0.7rem;
        }
    </style>
</head>
<body>
    <section>
        <div>
            
        </div>
    </section>
</body>
</html>
HTML