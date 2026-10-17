rule Lab23_Text_Encodings : training
{
    strings:
        $marker = "LAB23_MARKER" ascii wide
        $context = "training_context" ascii wide
    condition:
        filesize < 10KB and all of them
}
