<?php
if(!isset($bdd)) {
  require('../../admin/log-db.php');
}

$get = $bdd->prepare('SELECT * FROM `data` WHERE `alert`=1 AND `archive`=0 ORDER BY `id` DESC');
$get->execute();
$get = $get->fetchAll();

for ($i=0; $i < count($get); $i++) { 
  if($get[$i]['latitude'] == -1 && $get[$i]['longitude'] == -1 && $get[$i]['altitude'] == -1) {
    $t = $get[$i]['time'];
    $time = $t[0] . number_format($t[1]) + 1 . ':' . $t[2] . $t[3] . ':' . $t[4] . $t[5];
    echo '
    <div class="contents">
      <p id="id' . $get[$i]['id'] . '">' . $get[$i]['id'] . '</p>
      <p id="received">' . $get[$i]['datetime-auto'] . '</p>
      <p id="sent">Envoyé à</p>
      <p id="sent-time">' . $time . '</p>
      <input type="button" value="Archiver" id="' . $get[$i]['id'] . '" onclick="archive(`' . $get[$i]['id'] . '`);">
    </div>
    ';
  }
}
?>