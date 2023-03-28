<!DOCTYPE html>
<html lang="fr">
<head>
  <meta charset="utf-8">
  <meta http-equiv="X-UA-Compatible" content="IE=edge">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Document</title>
  <link rel="stylesheet" href="./media/style.css">
  <script src="./media/modules/jquery.min (3.4.1).js"></script>
  <link rel="shortcut icon" href="./media/images/insigne.png" type="image/x-icon">
</head>
<body>
  <input type="button" value="Actualiser" onclick="actualiser()">
  <div class="parent">
    <div class="content-1 content">
      <h2>Avec localisation</h2>
      <?php require('./pages/data/avec.php') ?>
    </div>
    <div class="content-2 content">
      <h2>Sans localisation</h2>
      <?php require('./pages/data/sans.php') ?>
    </div>
  </div>
  <script>
    function archive(id) {
      $.ajax({
        type: 'POST',
        url: './pages/data/archive.php',
        data: `id=${id}`,
        success: function (data) {
          let input = document.getElementById(id);
          if(data == 'true') {
            input.remove();
          } else {
            input.value = 'Archiver (une erreur est survenue)';
          }
        }
      });
    }
    function actualiser() {
      let div = [document.getElementsByClassName("contents")].map(n => n)[0];
      for (let i = 0; i < div.length; i++) {
        setTimeout(() => {
          div[0].remove();
        }, 1);
      }

      $.ajax({
        type: 'POST',
        url: './pages/data/avec.php',
        success: function (data) {
          $('.content-1').append(data);
        }
      });
      $.ajax({
        type: 'POST',
        url: './pages/data/sans.php',
        success: function (data) {
          $('.content-2').append(data);
        }
      });
    }
  </script>
</body>
</html>