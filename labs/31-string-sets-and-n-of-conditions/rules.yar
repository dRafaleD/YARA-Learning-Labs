rule Lab31_TwoOfThree {
 strings:
  $a = "LAB31_ALPHA" ascii
  $b = "LAB31_BETA" ascii
  $c = "LAB31_GAMMA" ascii
 condition:
  filesize < 1024 and 2 of ($a, $b, $c)
}
