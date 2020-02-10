<?php
  $f = fopen("/sys/class/thermal/thermal_zone0/temp","r");
  $temp = fgets($f);
  echo 'SoC Tempt = '.round($temp/1000). '&#8451;</font>';
  fclose($f);
?>
