rule Lab34_BoundedRegex {
 strings:
  $id = /LAB34-[0-9]{4}-[A-Z]{2}/ ascii
 condition:
  filesize < 1024 and $id
}
