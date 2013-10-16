print """
Keywords

    and - Logical AND operation
    del- Deletes objects. These objects could be local variables, or even elements from a list. - References [1] [2]
    from - Used for importing elements from modules
    not - The logical NOT operation
    while - Used for looping until the condition in while remains true
    as - When used with the 'import' statement, the as keyword is used to rename the bound object. It can also be used with the 'with' statement... though I am not sure what that statement does.
    elif - 'else if'
    global - This causes a local variable to be visible outside of it's scope. Ref [1]
    or - The logical OR operation
    with - This seems like a more convenient alternative to try...finally when there is a setup, execution, and teardown cycle to be performed. Ref [1]
    assert - The 'assert' statement is used to put error checking in your code. It seems to be very similar to what 'assert' does in Java
    else - 'else' part of a conditional
    if - Conditional
    pass - The 'pass' statement does nothing. It is used when a statement is required syntactically, but nothing needs to be done. Ref [1]
    yield - The yield statement causes a function to return a generator. When this generator is run, it will return a value specified by the yield statement and will do so every time it is run until the function runs out of values. This is also akin to continuations. Ref [1]. Do generators always return iterables ?
    break - The 'break' statement breaks out of the immediately enclosing 'for' or 'while' loop. Ref [1]
    except - The 'except' keyword is used as a counterpart to the 'try' keyword. It has a similar function to the 'catch' keyword in Java. Ref [1]
    import - Used for importing modules and their elements
    print - Used for printing something to the console
    class - Used for defining a class
    exec - Supports dynamic execution of Python code
    in - The inclusion operator
    raise - Raising an exception
    continue - Continue back to the start of the loop
    finally - The cleanup block after a try...except statement. Ref [1]
    is - Used to determine if two values are stored in the same memory location. Ref [1]
    return - Used to return a value from a function
    def - Keyword used to define a function
    for - The for loop
    lambda - Used to create small anonymous functions. Ref [1]
    try - Used to enclose code which could throw Exceptions. It must be followed by an 'except' statement.

Notes:
This webpage says that the 'del' keyword deletes objects. What exactly does that mean? Does it delete objects from lists, sequences, etc, or does it also delete objects from within other objects, or entire objects ?

Data Types

For data types, write out what makes up each one. For example, with strings write out how you create a string. For numbers write out a few numbers.

    True - The boolean true value
    False - The boolean false value
    None - Represents nothing... looks like it is similar to the 'null' keyword in Java
    strings - The string datatype which is a sequence of characters
    numbers - Python supports several numeric data types
    floats - Represents floating point numbers as per the IEEE 854-1987 standard
    lists - An ordered collection of items

String Escapes Sequences

For string escape sequences, use them in strings to make sure they do what you think they do.

    \\ - Result is a single backslash
    \' - Result is the ' character
    \" - Result is the " character
    \a - Result is the ASCII bell
    \b - ACSII backspace
    \f - ASCII formfeed
    \n - ASCII linefeed
    \r - ASCII carriage return
    \t - ASCII horizontal tab
    \v - ASCII vertical tab


String Formats

Same thing for string formats: use them in some strings to know what they do.

    %d - signed decimal
    %i - signed integer decimal
    %o - signed octal value
    %u - Obsolete type now... identical to %d
    %x - Signed hexadecimal lowercase
    %X - Signed hexadecimal uppercase
    %e - Floating point exponential format (lowercase)
    %E - Floating point exponential format (uppercase)
    %f - Floating point decimal format
    %F - Floating point decimal format
    %g - Floating point format. Uses lowercase format if exponent is less than -4 or not less than precision. Decimal otherwise
    %G - Floating point format. Uses uppercase format if exponent is less than -4 or not less than precision. Decimal otherwise
    %c - Single character. Accepts integer or single character string
    %r - Any Python object
    %s - String
    %% - Results in the % character... no argument is converted


Operators

Some of these may be unfamiliar to you, but look them up anyway. Find out what they do, and if you still can't figure it out, save it for later.

    + - addition operator
    - - subtraction operator
    * - multiplication operator
    ** - The power operator. a ** b will give a to the power b
    / - The division operator
    // - Floor division. 9 //2 is 4
    % - Modulus operator
    < - Less than
    > - Greater than
    <= - Less than equal to
    >= - Greater than equal to
    == - Equality
    != - Not equal to
    <> - Not equal to
    ( ) - Parenthesis for defining proper precedence
    [ ] - Used for defining lists
    { } - Used for defining maps ?
    @ - Decorator
    , - Used to separate values in a tuple
    : - Used to delimit the key and value in map entries
    . - Used to identify a method on a referenced object or module
    = - Assignment operator
    ; - Combines multiple statements into one. See [1]
    += - Add and assign (the ones below are similar... do something and assign)
    -=
    *=
    /=
    //=
    %=
    **=
    
    """
