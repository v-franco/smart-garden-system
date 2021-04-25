<!DOCTYPE html>
<html>
<head>
 <title>Tabla con base de datos</title>
 <style type="text/css">
  table{
     border-collapse: collapse;
     width: 100%;
     color: #CD214F;
     font-family: monospace;
     font-size: 25px;
     text-align: center;
  }
  th{
     background-color: #CD214F;
     color: white;
  }
  tr:nth-child(even) {background-color: #f2f2f2}
 </style>
</head>
<body>
<table>
 <tr>
   <th>Electrovalvula I</th>
   <th>Temperatura (°C)</th>
   <th>Sensor humedad I</th>
   <th>Fecha</th>
 </tr>
 <?php
 $conn = mysqli_connect("localhost", "rasp", "pi", "cultivo");
 if($conn-> connect_error){
    die("conexion fallida:". $conn-> connect_error);
 }
 
 $sql = "SELECT `Electrovalvula 1`,`Temperatura`,`Sensor humedad 1`,`Hora` from Sensores";
 $result = $conn-> query($sql);
 
 if($result-> num_rows > 0){
    while($row = $result-> fetch_assoc()){
      echo "<tr><td>".$row["Electrovalvula 1"] ."</td><td>".$row["Temperatura"]."</td><td>".$row["Sensor humedad 1"]."</td><td>".$row["Hora"]."</td></tr>";
    }
    echo "</table>";
 }
 else{
    echo "No hay resultados";
 }
 
 $conn->close();
 ?>
</table>
</body>
</html>
    
