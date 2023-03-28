<?php
require('../../admin/log-db.php');

if(isset($_POST['id'])) {  
  $update = $bdd->prepare('UPDATE `data` SET `archive`=1 WHERE `id`=?;');
  $update->execute(array($_POST['id']));

  echo 'true';
} else {
  echo 'false';
}
?>