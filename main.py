last_sequence = -1
def check_sequence(current):
    global last_sequence
    if last_sequence != -1:
        expected = last_sequence + 1
        if current != expected:
            gap = current - expected
    print("Missing " + str(gap) + " packet(s)")
    last_sequence = current
        if not validate_packet(packet):
            corrupt_count += 1
            return # Reject
            if seq != expected:
                missing_count += (seq - expected)
    
                if len(parts) != 4:
                    error_count += 1
                    return
