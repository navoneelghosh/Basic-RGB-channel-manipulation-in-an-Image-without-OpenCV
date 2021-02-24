# Basic RGB channel manipulation in an Image without OpenCV

<html>

<head>
    <meta name="viewport" content="width=device-width, initial-scale=1.0"> 
    <!-- The title tag sets the title bar of the web bar -->
</head>

<body width = "device-width" bgcolor="#ffffff">
    <!-- The <body> tag lets the browser know that we are beginning the body of the web page.  The bgcolor option sets the background color to the web page -->

    <h1>Basic RGB channel manipulation in an Image without OpenCV</h1>

    <p>
    <ol>
        <li>
            Original Image -
            <br>
            <img src="./Images/Design_01.jpg" style="height: auto; width: 24%;">
            <br><br>
        </li>
        <li>
            Grayscale Image -
            <br>
            <img src="./Images/Grayscale_Design_01.jpg" style="height: auto; width: 24%;">
            <br><br>
            Formula used for grayscale -
            <br>
            gray = integer(0.2126R + 0.7152G + 0.0722B), where R,G,B are the respective colour channel values.
            <br>
            While a grayscale image can be obtained in numerous ways, this are the colour coefficiants recommended by
            <a href="https://en.wikipedia.org/wiki/Rec._709">ITU-R BT.709-6 Recommendation.</a>
            <br>
            This is done because the human eye has different sensitivity to different colours and therefore, the RGB
            channels are weighted.
            <br><br>
        </li>
        <li>
            Selective Grayscaling - Convert every other colour in the image except the shades and hues of Blue -
            <br>
            <img src="./Images/Blue_Only_Grayscale_Design_01.jpg" style="height: auto; width: 24%;">
            <br><br>
            This was achieved by applying the grayscaling formula to all pixels except the pixels <br>
            where the Blue channel value was both greater than 43 and the Red and Green channel values. <br>
            It was specifically set to be greater than 43 because anything less than that results in <br>
            shades of gray or eventually black and not shades of blues.
            <br><br>
        </li>
        <li>
            Negative Image -
            <br>
            <img src="./Images/Negative_Design_01.jpg" style="height: auto; width: 24%;">
            <br><br>
            This was achieved by replacing the R, G, B values with (255-R), (255-G), (255-B) respectively.
            <br><br>
        </li>
        <h3>Additional Examples - </h3>
        <br>
        <img src="./Images/Design_01.jpg" style="height: auto; width: 24%;">
        <img src="./Images/Grayscale_Design_01.jpg" style="height: auto; width: 24%;">
        <img src="./Images/Blue_Only_Grayscale_Design_01.jpg" style="height: auto; width: 24%;">
        <img src="./Images/Negative_Design_01.jpg" style="height: auto; width: 24%;">
        <br>
        <img src="./Images/Design_02.jpg" style="height: auto; width: 24%;">
        <img src="./Images/Grayscale_Design_02.jpg" style="height: auto; width: 24%;">
        <img src="./Images/Blue_Only_Grayscale_Design_02.jpg" style="height: auto; width: 24%;">
        <img src="./Images/Negative_Design_02.jpg" style="height: auto; width: 24%;">
        <br>
        <img src="./Images/Design_03.jpg" style="height: auto; width: 24%;">
        <img src="./Images/Grayscale_Design_03.jpg" style="height: auto; width: 24%;">
        <img src="./Images/Blue_Only_Grayscale_Design_03.jpg" style="height: auto; width: 24%;">
        <img src="./Images/Negative_Design_03.jpg" style="height: auto; width: 24%;">
        <br>
        <img src="./Images/Design_04.jpg" style="height: auto; width: 24%;">
        <img src="./Images/Grayscale_Design_04.jpg" style="height: auto; width: 24%;">
        <img src="./Images/Blue_Only_Grayscale_Design_04.jpg" style="height: auto; width: 24%;">
        <img src="./Images/Negative_Design_04.jpg" style="height: auto; width: 24%;">
        <br>
        <img src="./Images/Design_05.jpg" style="height: auto; width: 24%;">
        <img src="./Images/Grayscale_Design_05.jpg" style="height: auto; width: 24%;">
        <img src="./Images/Blue_Only_Grayscale_Design_05.jpg" style="height: auto; width: 24%;">
        <img src="./Images/Negative_Design_05.jpg" style="height: auto; width: 24%;">
        <br>
        <img src="./Images/Design_06.jpg" style="height: auto; width: 24%;">
        <img src="./Images/Grayscale_Design_06.jpg" style="height: auto; width: 24%;">
        <img src="./Images/Blue_Only_Grayscale_Design_06.jpg" style="height: auto; width: 24%;">
        <img src="./Images/Negative_Design_06.jpg" style="height: auto; width: 24%;">
    </ol>
    <br>
    </p>

</body>

</html>
 
