<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Kalkulator Sederhana</title>
    <link rel="stylesheet" href="style.css">
</head>
<body>
    <div class="calculator">
        <h2>Kalkulator Sederhana</h2>
        <form method="POST" action="">
            <input type="text" name="display" id="display" readonly>
            <div class="buttons">
                <button type="button" onclick="appendToDisplay('7')">7</button>
                <button type="button" onclick="appendToDisplay('8')">8</button>
                <button type="button" onclick="appendToDisplay('9')">9</button>
                <button type="button" onclick="appendToDisplay('+')">+</button>
                <button type="button" onclick="appendToDisplay('4')">4</button>
                <button type="button" onclick="appendToDisplay('5')">5</button>
                <button type="button" onclick="appendToDisplay('6')">6</button>
                <button type="button" onclick="appendToDisplay('-')">-</button>
                <button type="button" onclick="appendToDisplay('1')">1</button>
                <button type="button" onclick="appendToDisplay('2')">2</button>
                <button type="button" onclick="appendToDisplay('3')">3</button>
                <button type="button" onclick="appendToDisplay('*')">*</button>
                <button type="button" onclick="appendToDisplay('0')">0</button>
                <button type="button" onclick="clearDisplay()">C</button>
                <button type="button" onclick="calculateResult()">=</button>
                <button type="button" onclick="appendToDisplay('/')">/</button>
            </div>
        </form>
    </div>

    <script>
        function appendToDisplay(value) {
            document.getElementById('display').value += value;
        }

        function clearDisplay() {
            document.getElementById('display').value = '';
        }

        function calculateResult() {
            try {
                document.getElementById('display').value = eval(document.getElementById('display').value);
            } catch (error) {
                document.getElementById('display').value = 'Error';
            }
        }
    </script>
</body>
</html>
