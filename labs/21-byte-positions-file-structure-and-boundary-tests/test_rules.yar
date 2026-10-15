rule Lab21_Structured_Marker : training offset
{
 strings:
  $header = "YL21"
  $section = "SECTION=LAB"
  $version = "VERSION=1"
 condition:
  filesize >= 24 and filesize < 1KB and
  $header at 0 and $section in (4..40) and $version
}