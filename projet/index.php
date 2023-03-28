<?php
require('./admin/log-db.php');
session_start();

if(isset($_SESSION['log']) && $_SESSION['log'] == true) {
  require('./pages/data.php');
} else {
  require('./pages/login.php');
}

session_destroy();
?>