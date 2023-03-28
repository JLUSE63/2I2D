<?php
$_POST['name'] = 'chute_velo';
require(str_repeat("../", count(explode('/', str_replace($_SERVER['DOCUMENT_ROOT'], '', $_SERVER['SCRIPT_FILENAME'])))-2) . 'data/admin/log-db.php');
?>