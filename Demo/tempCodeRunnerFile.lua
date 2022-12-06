-- Define the calculator function
function calculator(num1, num2, op)
    -- Check the operator and perform the appropriate calculation
    if op == "+" then
        return num1 + num2
    elseif op == "-" then
        return num1 - num2
    elseif op == "*" then
        return num1 * num2
    elseif op == "/" then
        return num1 / num2
    else
        -- If the operator is not recognized, return an error message
        return "Invalid operator"
    end
end

-- Prompt the user for the numbers and operator
print("Enter first number:")
num1 = io.read()
print("Enter second number:")
num2 = io.read()
print("Enter operator (+, -, *, /):")
op = io.read()

-- Call the calculator function and print the result
result = calculator(num1, num2, op)
print("Result: " .. result)