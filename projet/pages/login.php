<!DOCTYPE html>
<html lang="fr">
<head>
  <meta charset="utf-8">
  <meta http-equiv="X-UA-Compatible" content="IE=edge">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Login</title>
  <link rel="stylesheet" href="./media/style.css">
  <link rel="shortcut icon" href="./media/images/insigne.png" type="image/x-icon">
</head>
<body>
  <div class="login">
    <div class="form">
      <p>welcome</p>
      <form class="login-form" action="./pages/login/verif-mdp.php" method="POST">
        <input name="un" type="text" placeholder="username" required pattern="admin" value="admin" required>
        <input name="pw" type="password" placeholder="password" required>
        <button>login</button>
      </form>  
    </div>
  </div>
</body>
</html>

<!-- https://codepen.io/clln/pen/vYJWLqE -->