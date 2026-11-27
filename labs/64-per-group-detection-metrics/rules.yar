/* Synthetic training text only. */
rule Toy_Blue_Marker {
    strings:
        $blue = "BLUE-TOKEN" ascii fullword
    condition:
        $blue
}
