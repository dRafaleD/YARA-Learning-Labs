private rule Lab32_Header {
 strings:
  $h = "LAB32_HEADER" ascii
 condition:
  $h at 0
}

private rule Lab32_Body {
 strings:
  $b = "LAB32_BODY" ascii
 condition:
  $b
}

rule Lab32_Composed {
 condition:
  filesize < 1024 and Lab32_Header and Lab32_Body
}
