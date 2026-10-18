rule Lab24_Document_Marker : training
{
 strings:
  $a = "TRAINING_LAB24"
  $b = "document_record"
 condition:
  filesize < 2KB and all of them
}
