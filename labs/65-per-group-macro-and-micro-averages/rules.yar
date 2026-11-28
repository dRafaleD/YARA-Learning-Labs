/* Harmless synthetic text classifier. */
rule Toy_Blue_Practice {
    strings:
        $blue = "BLUE-TOKEN" ascii fullword
    condition:
        $blue
}
