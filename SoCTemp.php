<br><font size=5 color=white>
<?php
  $f = fopen("/sys/class/thermal/thermal_zone0/temp","r");
  $temp = fgets($f);
  echo 'SoC Temp. = '.round($temp/1000). '&#8451;</font>';
  fclose($f);
?>
</font>
