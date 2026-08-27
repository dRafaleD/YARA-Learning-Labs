rule Hello_YARA
{
    strings:
        $text = "HELLO_YARA"

    condition:
        $text
}
