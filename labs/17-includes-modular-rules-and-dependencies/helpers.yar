private rule Lab17_Helper_Training_Header
{
    strings:
        $header = "LAB17"
    condition:
        $header at 0
}

private rule Lab17_Helper_Two_Markers
{
    strings:
        $a = "alpha17"
        $b = "beta17"
        $c = "gamma17"
    condition:
        2 of them
}
