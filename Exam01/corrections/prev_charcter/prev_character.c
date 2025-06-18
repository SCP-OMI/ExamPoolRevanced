
char prev_character(char c) {
    if (c > 'A' && c <= 'Z') {
        return c - 1;
    } else if (c == 'A') {
        return 'Z';
    } else if (c > 'a' && c <= 'z') {
        return c - 1;
    } else if (c == 'a') {
        return 'z';
    }
}
