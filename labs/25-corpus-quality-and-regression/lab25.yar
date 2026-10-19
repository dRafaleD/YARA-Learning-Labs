rule Lab25_Training_Indicators : training {
 strings:
  $a = "LAB25_DOCUMENT" ascii
  $b = "component=parser" ascii
  $c = "version=5" ascii
 condition:
  filesize < 4096 and all of them
}
