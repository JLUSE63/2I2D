<?php
if(isset($_POST['un']) && isset($_POST['pw'])) {
  if($_POST['un'] == 'admin' && $_POST['pw'] == 'password123') {
    unset($_POST['un']);
    unset($_POST['pw']);
    session_start();
    $_SESSION['log'] = true;
    session_write_close();
  }
}
header("Location: ../");
?>