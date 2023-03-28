<?php
require('../admin/log-db.php');

if(isset($_GET['time'], $_GET['alt'], $_GET['lat'], $_GET['long'], $_GET['alert'])) {
  $variables = [$_GET['time'], $_GET['alt'], $_GET['lat'], $_GET['long'], $_GET['alert']];
  
  $input = $bdd->prepare('INSERT INTO `data` (`time`, `longitude`, `latitude`, `altitude`, `alert`, `archive`) VALUES (?, ?, ?, ?, ?, 0);');
  $input->execute(array($_GET['time'], $_GET['long'], $_GET['lat'], $_GET['alt'], $_GET['alert']));

  echo 'true';
} else {
  echo 'false';
}
?>