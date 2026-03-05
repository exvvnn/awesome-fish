

function colorPicker

    set -g Green (set_color green)
    set -g Red (set_color red)
    set -g Blue (set_color blue)
    set -g Yellow (set_color yellow)
    set -g Purple (set_color purple)
    set -g Cyan (set_color cyan)
    set -g White (set_color white)
    set -g Black (set_color black)
    set -g normal (set_color normal)

    set text_string $argv[1]
    set color $argv[2]

    switch $color
        case "Green"
           echo $Green$text_string$normal
        case "Red"
            echo $Red$text_string$normal
        case "Blue"
            echo $Blue$text_string$normal
        case "Yellow"
            echo $Yellow$text_string$normal
        case "Purple"
            echo $Purple$text_string$normal
        case "Cyan"
            echo $Cyan$text_string$normal
        case "White"
            echo $White$text_string$normal
        case "Black"
            echo $Black$text_string$normal
        case "*"
            echo "Invalid color"
    end

end

function main
    set -l text $argv[1]
    set -l color $argv[2]
    colorPicker $text $color
end

# Tricky one liner for parsing the same string twice. 
#  ex: colorPicker "Text string that will be passed" "Color"
main $argv[0..-2] $argv[-1]


