let last_sequence = -1
function check_sequence(current: number) {
    let expected: number;
    let gap: number;
    
    if (last_sequence != -1) {
        expected = last_sequence + 1
        if (current != expected) {
            gap = current - expected
        }
        
    }
    
    console.log("Missing " + ("" + gap) + " packet(s)")
    last_sequence = current
}

