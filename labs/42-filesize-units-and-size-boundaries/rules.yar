rule Lab42_SizeWindow {
 strings:
  $m = "LAB42" ascii
 condition:
  $m at 0 and filesize > 1KB and filesize < 4KB
}
