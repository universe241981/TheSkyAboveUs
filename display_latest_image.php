<?php
$page = $_SERVER['PHP_SELF'];
?>
<html>
<head>
<meta http-equiv="refresh" content="60" URL='<?php echo $page?>'">
<title>The Sky Above Us</title>
</head>
    <body bgcolor=black>
        <center><font size=8 color=white>The Sky Above Us</font><br><font size=5 color=white>Location = Somewhere On Earth | Owner = W.C.Observatory | </font>
        
        <br><font size=5 color=white>
                                                                 
        <?php
    
            $today = date(d-M-Y H:i:s");
            echo $today;
            
            ?>
            
        </font>
            
        <?php

            $files = glob('AllSkyData/*.*');
            $files = array_combine($files, array_map('filectime', $files));
            arsort($files);
            echo "<br><a href='" . key($files) . "' target='_blank'><img src='" . key($files) . "' height=100%></a>";

        ?>
        
        <br><font size=3 color=white>Powered by <a href="https://www.raspberrypi.org/" target="_blank"><font color=white>Raspberry Pi</a> and <a href="https://sites.google.com/site/meteotuxpi/home" target="_blank"><font color=white>Meteotux PI</a>.</font>
        <center><font size=3 color=white>Integrated by William Chin</font>
        

    </body>
</html>
