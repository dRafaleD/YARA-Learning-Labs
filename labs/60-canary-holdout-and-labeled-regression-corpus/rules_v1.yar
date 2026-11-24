/* Harmless training tokens only. */
rule Toy_Blue {
    strings:
        $b = "BLUE-TOKEN" ascii fullword
    condition:
        $b
}
