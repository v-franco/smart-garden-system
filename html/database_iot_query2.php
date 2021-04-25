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
   <th>Temperatura (°C)</th>
   <th>Luminosidad</th>
   <th>Nivel de agua</th>
   <th>Sensor humedad I</th>
   <th>Sensor humedad II</th>
   <th>Sensor humedad III</th>
   <th>Fecha</th>
 </tr>
 <?php
 $conn = mysqli_connect("localhost", "rasp", "pi", "cultivo");
 if($conn-> connect_error){
    die("conexion fallida:". $conn-> connect_error);
 }
 
 $sql = "SELECT `Temperatura`,`Luminosidad`,`Nivel de agua`,`Sensor humedad 1`,`Sensor humedad 2`,`Sensor humedad 3`,`Hora` from Sensores";
 $result = $conn-> query($sql);
 
 if($result-> num_rows > 0){
    while($row = $result-> fetch_assoc()){
      echo "<tr><td>".$row["Temperatura"]."</td><td>".$row["Luminosidad"]."</td><td>".$row["Nivel de agua"]."</td><td>".$row["Sensor humedad 1"]."</td><td>".$row["Sensor humedad 2"]."</td><td>".$row["Sensor humedad 3"]."</td><td>".$row["Hora"]."</td></tr>";
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
    
