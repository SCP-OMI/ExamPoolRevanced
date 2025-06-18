int ft_pow(int num, int pow) {
    if (pow == 0) {
        return 1;
    }
    if (pow < 0) {
        return 0;
    }
    
    int result = 1;
    for (int i = 0; i < pow; i++) {
        result *= num;
    }
    return result;
}