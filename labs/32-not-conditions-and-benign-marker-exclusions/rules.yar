rule Lab32_NotBenign {
 strings:
  $bad = "LAB32_SUSPICIOUS" ascii
  $benign = "LAB32_BENIGN_VENDOR" ascii
 condition:
  filesize < 1024 and $bad and not $benign
}
