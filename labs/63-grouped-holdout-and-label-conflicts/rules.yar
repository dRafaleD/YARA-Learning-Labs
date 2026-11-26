/* Harmless synthetic classification exercise. */
rule Toy_Training_Blue {
    strings:
        $marker = "BLUE-TOKEN" ascii fullword
    condition:
        $marker
}
