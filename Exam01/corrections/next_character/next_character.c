
char next_character(char c) {
    if (c >= 'A' && c < 'Z') {
        return c + 1;
    } else if (c == 'Z') {
        return 'A';
    } else if (c >= 'a' && c < 'z') {
        return c + 1;
    } else if (c == 'z') {
        return 'a';
    }
}
