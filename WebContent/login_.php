<!DOCTYPE html>
<html>
    <body>

        <?php
        echo "My first PHP script!";
        ?>
        
        <?php 
        $email = "";
        $password = "";
        
        if ($_SERVER["REQUEST_METHOD"] == "POST") {
            $email = test_input($_POST["email"]);
            $password = test_input($_POST["password"]);
        }
        
        function test_input($data) {
            $data = trim($data);
            $data = stripslashes($data);
            $data = htmlspecialchars($data);
            return $data;
        }
        
        if ($email === "test@test.com" && $password === "test") {
            header('Location: index.html');
        }
        else {
            echo '<script type="text/javascript">alert("Email or password wrong!");</script>';
            header('Location: login.html');
        }
        
        ?>

    </body>
</html>