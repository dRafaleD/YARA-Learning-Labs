rule Lab29_ContextualTraining {
 strings:
  $head = "LAB29_HEADER" ascii
  $marker = "EVENT" ascii
 condition:
  filesize < 1024 and $head at 0 and #marker >= 2 and @marker[2] > @marker[1]
}
