rule Lab26_Explained_Training : educational
{
 meta:
  description = "Harmless training marker requiring context"
  confidence = "training_only"
 strings:
  $header = "LAB26_HEADER" ascii
  $context = "component=sample" ascii
 condition:
  filesize < 2048 and all of them
}
