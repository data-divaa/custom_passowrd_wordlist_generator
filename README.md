# custom_passowrd_wordlist_generator
This is a password wordlist generator that generates password combinations for brute force with inputs such as 
- name
- birthyear
- phone number
- current year

Humans have always preferred passcodes to be as personal as possible. They combine names, DOBs, ID numbers, years, etc. when choosing a passcode.
This mentality has not changed over the years and has helped security researchers prove this weak link during pen testing assignments.

This tool generates a very basic wordlist for brute-forcing by generating a non-random, very personal alphanumeric set of passcodes that might give you a hit.

# Usage
- Git clone this repository to your Windows or Linux machine ( should have a Python 3.x )
- run the Python file that will prompt you for details.
- All these fields ( except name ) are optional.
- It will finally create a wordlist in the same directory that could be directly used as a wordlist input in FFuF, Hydra, etc.

This tool will be updated in the future and more modules will be added.
